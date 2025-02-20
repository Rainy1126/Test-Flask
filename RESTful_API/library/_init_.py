from flask import Flask
from .books.controller import books
from .category_author.controller import author, category
from .borrow.controller import borrow
from .students.controller import student
from .users.controller import users
from .login_attempts.controller import logins
from .extension import db, ma
import os


def create_db(app):
    with app.app_context():
        if not os.path.exists("/library/library.db"):
            db.create_all()
            print("Database created")


blueprints = [books, author, category, borrow, student, users, logins]

def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    ma.init_app(app)
    db.init_app(app)
    create_db(app)
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    return app

