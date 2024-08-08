from decouple import config
from flask import Flask
from flask_login import LoginManager 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.accounts.models import User


app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager() 
login_manager.init_app(app) 
login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
