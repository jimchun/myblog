from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Post
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)
admin = Blueprint('admin', __name__)

@main.route('/')
@login_required
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash('用户名已存在')
            return redirect(url_for('auth.register'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('注册成功，请登录')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('登录失败，请检查用户名和密码')
    
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('博文已发布')
        return redirect(url_for('main.index'))
    return render_template('post.html')

@main.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', title=post.title, post=post)

@admin.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('您没有管理员权限')
        return redirect(url_for('main.index'))
    user_count = User.query.count()
    post_count = Post.query.count()
    latest_user = User.query.order_by(User.id.desc()).first()
    return render_template('admin/dashboard.html', user_count=user_count, post_count=post_count, latest_user=latest_user)

@admin.route('/admin/users')
@login_required
def admin_users():
    if not current_user.is_admin:
        flash('您没有管理员权限')
        return redirect(url_for('main.index'))
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin.route('/admin/posts')
@login_required
def admin_posts():
    if not current_user.is_admin:
        flash('您没有管理员权限')
        return redirect(url_for('main.index'))
    posts = Post.query.all()
    return render_template('admin/posts.html', posts=posts)