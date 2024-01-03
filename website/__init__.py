from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "db_name"  # Change this to your MySQL database name
DB_USER = "root"  # Change this to your MySQL username
DB_PASSWORD = "8054535730"  # Change this to your MySQL password
DB_HOST = "localhost"  # Change this to your MySQL host (if not localhost)
DB_PORT = "3306"  # Change this to your MySQL port (if not the default)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfghjkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
