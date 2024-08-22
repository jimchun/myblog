from app import create_app, db
from app.models import User
from datetime import datetime

app = create_app()

def update_users():
    with app.app_context():
        users = User.query.all()
        for user in users:
            if user.date_joined is None:
                user.date_joined = datetime.utcnow()
        db.session.commit()
        print("已更新所有现有用户的 date_joined 字段")

if __name__ == '__main__':
    update_users()