from app import create_app, db
from flask_migrate import Migrate
from alembic import command
from alembic.config import Config

app = create_app()
migrate = Migrate(app, db)

with app.app_context():
    alembic_cfg = Config("migrations/alembic.ini")
    alembic_cfg.set_main_option("script_location", "migrations")
    command.revision(alembic_cfg, autogenerate=True, message="Add date_joined to User model")
    command.upgrade(alembic_cfg, "head")

print("Migration complete")