from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.blueprints.main import main_bp
    from app.blueprints.health import health_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)

    return app