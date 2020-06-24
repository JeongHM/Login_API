import os
import logging

from flask import Flask, current_app, request
from flask_cors import CORS
from logging.handlers import RotatingFileHandler


def create_app():
    """
    Create Flask Object (init), init DB, register Blueprint
    :return: app Object
    """
    # App Setting
    app = Flask(__name__)

    app.secret_key = os.urandom(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_DATABASE')
    )

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Loggin 설정
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    logger_formatter = logging.Formatter(fmt='[%(asctime)s] %(pathname)s:%(lineno)d %(levelname)s - %(message)s')
    logger_handler = RotatingFileHandler(filename='./application.log',
                                         mode='a',
                                         maxBytes=1024 * 1024 * 5,
                                         backupCount=5,
                                         encoding='utf-8')
    logger_handler.setFormatter(fmt=logger_formatter)
    logger.addHandler(hdlr=logger_handler)

    app.logger.addHandler(logger_handler)
    app.logger.setLevel(logging.INFO)

    CORS(app)

    # Blueprint 설정
    from controllers.user import user_blueprint
    from controllers.token import token_blueprint
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=token_blueprint, url_prefix='/token')

    with app.app_context():
        # DB 설정
        from models import db
        db.init_app(app=app)
        db.create_all()

    return app


application = create_app()


@application.before_request
def before_request():
    method = request.environ.get('REQUEST_METHOD')
    host = request.environ.get('HTTP_HOST')
    path = request.environ.get('PATH_INFO')
    param = dict(request.args) if request.args else None
    body = dict(request.json) if request.json else None

    current_app.logger.info(f'[{method}] {host}{path} params: {param} body: {body}')


@application.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    return 'Hello Login API'


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5050)
