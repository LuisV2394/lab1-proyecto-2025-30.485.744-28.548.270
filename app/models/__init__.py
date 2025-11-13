# Import models so Flask-Migrate / Alembic can detect them
from app.models.user import User
from app.models.professional import Professional
from app.models.unit import Unit

__all__ = ["User", "Professional", "Unit"]