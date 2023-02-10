from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

from dash import Dash
import dash_bootstrap_components as dbc

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
csrf._exempt_views.add('dash.dash.dispatch')
mail = Mail()
jwt = JWTManager()


def create_app(config_classname):
    """
    Initialise the Flask application.
    :type config_class_name: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """

    app = Flask(__name__)

    app.config.from_object(config_classname)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'COMP0045.reset@gmail.com'
    app.config['MAIL_PASSWORD'] = 'test123test'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True


    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'Login to view.'
    csrf = CSRFProtect(app)
    csrf._exempt_views.add('dash.dash.dispatch')
    register_dashapp(app)
    jwt.init_app(app)
    mail.init_app(app)

    

    with app.app_context():
        from models import User
        db.create_all()
    
    from auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

def register_dashapp(app):
    from my_dash_app.layout import layout
    from my_dash_app.callbacks import init_callbacks

    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp = Dash(__name__,
                    server=app,
                    url_base_pathname='/dash_app/',
                    meta_tags=[meta_viewport],
                    external_stylesheets=[dbc.themes.SANDSTONE])

    with app.app_context():
        dashapp.title = 'Dashboard'
        dashapp.layout = layout
        init_callbacks(dashapp)

    _protect_dash_views(dashapp)


def _protect_dash_views(dash_app):
    for view_func in dash_app.server.view_functions:
        if view_func.startswith(dash_app.config.routes_pathname_prefix):
            dash_app.server.view_functions[view_func] = login_required(dash_app.server.view_functions[view_func])

