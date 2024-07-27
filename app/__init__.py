from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')


    # log_configuration_values(app)

    app_logger(app)

    db.init_app(app)

    verify_db_connection(app)

    from app.controllers.retreat_controller import retreat_bp
    from app.controllers.booking_controller import booking_bp
    from app.controllers.user_controller import user_bp

    app.register_blueprint(retreat_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(user_bp)

    return app

def log_configuration_values(app):
    print("Logging Configuration Values:")
    for key, value in app.config.items():
        print(f"{key} = {value}")

def app_logger(app):
    if not app.debug:
        handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)


def verify_db_connection(app):
    with app.app_context():
        # Import models to ensure they are registered
        from app.models.retreat_model import Retreat
        from app.models.user_model import User
        from app.models.booking_model import Booking

        try:
            db.engine.connect()
            app.logger.info("Database connection successful")
        except Exception as e:
            app.logger.error(f"Database connection failed: {e}")
            raise

        db.create_all()
        app.logger.info("Tables created (if they did not already exist)")

