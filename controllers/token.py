from flask import Blueprint, request

from utils.decorators import token_required, header_required, response_format
from utils.response_code import RESPONSE_CODE

token_blueprint = Blueprint(name='token', import_name=__name__)


@token_blueprint.route('/validate', methods=['POST'], endpoint='token_validate')
@header_required
@token_required
@response_format
def token_validate():
    return RESPONSE_CODE['SUCCESS'], None


@token_blueprint.route('/refresh', methods=['POST'], endpoint='token_refresh')
@header_required
@token_required
@response_format
def token_refresh():
    return RESPONSE_CODE['SUCCESS'], None