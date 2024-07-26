from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    if not app.debug:
        handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)

    db.init_app(app)

    # Test the DB connection
    with app.app_context():
        try:
            db.engine.connect()
            app.logger.info("Database connection successful")
        except Exception as e:
            app.logger.error(f"Database connection failed: {e}")
            raise



    from app.controllers.retreat_controller import retreat_bp
    from app.controllers.booking_controller import booking_bp

    app.register_blueprint(retreat_bp)
    app.register_blueprint(booking_bp)

    return app
