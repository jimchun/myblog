from app import create_app, db
from app.models import User, Post

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()

        # 创建管理员用户
        admin = User(username='admin', email='admin@example.com', is_admin=True)
        admin.set_password('adminpassword')
        db.session.add(admin)

        # 创建普通用户
        user = User(username='user', email='user@example.com')
        user.set_password('userpassword')
        db.session.add(user)

        # 创建一些博文
        post1 = Post(title='第一篇博文', content='这是第一篇博文的内容。', author=user)
        post2 = Post(title='第二篇博文', content='这是第二篇博文的内容。', author=user)
        db.session.add(post1)
        db.session.add(post2)

        db.session.commit()

if __name__ == '__main__':
    init_db()
    print("数据库初始化完成")