import sys
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

path = Path(__file__)

print(path.parent.absolute())

sys.path.insert(0, path.parent.absolute().__str__())

from flask import Flask, g
from flask_cors import CORS
from config import DevelopmentConfig, ProductionConfig
from flask_jwt_extended import JWTManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app(config_name='development'):
    print('hello world')
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)

    elif config_name == 'production':
        app.config.from_object(ProductionConfig)
                               
    mail = Mail(app)

    # Enable CORS for all routes
    CORS(app)
    db.init_app(app)
    mail.init_app(app)
    
    jwt = JWTManager(app)


    from routes import auth_bp, finance_bp
    
    blueprints = [auth_bp, finance_bp]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    with app.app_context():
        db.create_all()


    return app
