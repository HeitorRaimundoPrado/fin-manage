from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    FRONTEND_DOMAIN = os.getenv('FRONTEND_DOMAIN')
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS=True
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
    MAIL_USE_SSL=False
    

    # Other common configuration options

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific configuration options

class ProductionConfig(Config):
    # Production-specific configuration options
    pass
