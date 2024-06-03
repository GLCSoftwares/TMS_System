from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)

    # Import các blueprint
    from .routes import auth_bp
    from .route_Admin import admin_bp

    # Đăng ký các blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app
