import flask

from simple_downloader import views

__version__ = "1.2"


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)
    app.config["SECRET_KEY"] = "jGa7jSevicjvhXtUGhpkLKxfpvghFu5e"
    app.register_blueprint(views.mod)
    return app
