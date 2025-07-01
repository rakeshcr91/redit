from flask import Flask
from .extensions import db, login_manager, migrate
from .auth.routes import auth_bp
from .main.routes import main_bp


def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///app.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if config_object:
        app.config.from_object(config_object)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
