import os
from flask import Flask
from flask_cors import CORS
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), './config.ini')))


def create_app():
    """
    Create Flask Object (init), init DB, register Blueprint
    :return: app Object
    """
    # App Setting
    app = Flask(__name__)
    CORS(app)
    app.secret_key = os.urandom(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['APP']['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'

    # DB Setting
    from models.model import db
    db.init_app(app=app)
    db.create_all(app=app)

    from controllers.user import user_blueprint
    from controllers.token import token_blueprint
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=token_blueprint, url_prefix='/token')

    return app


application = create_app()


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=5000, debug=True)
