from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'

    from app.auth.routes import auth
    from app.dashboard.routes import dashboard

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)

    return app
