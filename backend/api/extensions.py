from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()
mail = Mail()