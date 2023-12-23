import sys
from pathlib import Path
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from flask import Flask
from flask_cors import CORS
from api.config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask_jwt_extended import JWTManager

from api.extensions import db, mail, migrate
from api.models import User

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)

    elif config_name == 'production':
        app.config.from_object(ProductionConfig)

    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
                               
    # Enable CORS for all routes
    CORS(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    
    jwt = JWTManager(app)


    from api.routes import auth_bp, finance_bp
    
    blueprints = [auth_bp, finance_bp]


    with app.app_context():
        db.create_all()

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    return app
