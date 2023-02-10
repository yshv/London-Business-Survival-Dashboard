from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
#login_manager = LoginManager()
csrf = CSRFProtect()
csrf._exempt_views.add('dash.dash.dispatch')


def create_app(config_classname):
    """
    Initialise the Flask application.
    :type config_class_name: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """

    app = Flask(__name__)

    app.config.from_object(config_classname)
    db.init_app(app)
    #login_manager.init_app(app)
    csrf = CSRFProtect(app)
    csrf._exempt_views.add('dash.dash.dispatch')

    with app.app_context():
        # Import Dash application
        from dash_app import init_dashboard
        app = init_dashboard(app)

    from auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app