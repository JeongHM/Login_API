from flask import Blueprint, request

from utils.decorators import response_format, token_required
from utils.response_code import RESPONSE_CODE
from services.internals.user import UserService
from services.internals.token import TokenService

user_blueprint = Blueprint(name='user', import_name=__name__)


@user_blueprint.route('/registration', methods=['POST'], endpoint='user_registration')
@response_format
def user_registration():
    body = dict(request.json)

    user = UserService(body=body)

    if not user.validate_body():
        return RESPONSE_CODE[400], None

    if not user.validate_name():
        return RESPONSE_CODE[800], None

    if not user.validate_nick_name():
        return RESPONSE_CODE[801], None

    if not user.validate_email():
        return RESPONSE_CODE[802], None

    if not user.validate_phone():
        return RESPONSE_CODE[803], None

    if not user.validate_password():
        return RESPONSE_CODE[804], None

    if not user.create_user():
        return RESPONSE_CODE[400], None

    return RESPONSE_CODE[200], None


@user_blueprint.route('/login', methods=['POST'], endpoint='user_login')
@response_format
def user_login():
    body = dict(request.json)

    user = UserService(body=body)

    res, user_id = user.login()
    if not res:
        return RESPONSE_CODE[805], None

    token = TokenService(user_id=user_id)
    access_token = token.create_token()

    if not access_token or not isinstance(access_token, dict):
        return RESPONSE_CODE[400], None

    return RESPONSE_CODE[200], access_token


@user_blueprint.route('/logout', methods=['POST'], endpoint='user_logout')
@token_required
@response_format
def user_logout():
    header = dict(request.headers)
    access_token = header.get('Access-Token')

    res = TokenService.delete_token(access_token=access_token)

    if not res:
        return RESPONSE_CODE[404]

    return RESPONSE_CODE[200], None


@user_blueprint.route('/detail', methods=['GET'], endpoint='user_detail')
@token_required
@response_format
def user_detail():
    header = dict(request.headers)
    access_token = header.get('Access-Token')

    res, user_id = TokenService.get_user_id_by_token(access_token=access_token)
    if not res:
        return RESPONSE_CODE[404], None

    user = UserService.get_user_detail(user_id=user_id)

    return RESPONSE_CODE[200], user


@user_blueprint.route('/details', methods=['GET'], endpoint='user_details')
@token_required
def user_details():
    return RESPONSE_CODE[200], None

