from flask import Flask
from flask_login import LoginManager
from .config import Config
from .models import db, User
from .views import init_views

def create_app():
    

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    init_views(app)

    return app