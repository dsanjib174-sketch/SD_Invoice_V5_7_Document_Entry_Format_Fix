from flask import Flask
def create_app():
    app = Flask(__name__)
    app.secret_key = "dev-secret"
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp
    from .routes.superadmin import superadmin_bp
    from .routes.client import client_bp
    from .routes.masters import masters_bp
    from .routes.documents import documents_bp
    from .routes.reports import reports_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(superadmin_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(masters_bp)
    app.register_blueprint(documents_bp)
    app.register_blueprint(reports_bp)
    return app
