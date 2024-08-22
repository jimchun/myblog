from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

def create_admin():
    with app.app_context():
        # 检查是否已存在管理员用户
        admin = User.query.filter_by(username='admin').first()
        if admin:
            print("管理员用户已存在")
            return

        # 创建新的管理员用户
        hashed_password = generate_password_hash('admin888')
        new_admin = User(
            username='admin',
            email='admin@example.com',
            password_hash=hashed_password,
            is_admin=True
        )

        # 将新用户添加到数据库
        db.session.add(new_admin)
        db.session.commit()

        print("管理员用户已成功创建")

if __name__ == '__main__':
    create_admin()