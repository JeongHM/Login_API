from flask import Blueprint, request

token_blueprint = Blueprint(name='token', import_name=__name__)


@token_blueprint.route('/refresh', methods=['POST'], endpoint='token_refresh')
def token_refresh():
    return 'hello world'