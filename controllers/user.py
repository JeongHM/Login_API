from flask import Blueprint, request

from utils.decorators import response_format
from utils.response_code import RESPONSE_CODE
from services.internals.user import UserService

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
def user_login():
    body = dict(request.json)

    user = UserService(body=body)

    res, user_id = user.login()
    if not res:
        return RESPONSE_CODE[805], None


    return RESPONSE_CODE[200], None


@user_blueprint.route('/logout', methods=['POST'], endpoint='user_logout')
def user_logout():
    return RESPONSE_CODE[200], None


@user_blueprint.route('/<int:user_id>/detail', methods=['GET'], endpoint='user_detail')
def user_detail():
    return RESPONSE_CODE[200], None


@user_blueprint.route('/details', methods=['GET'], endpoint='user_details')
def user_details():
    return RESPONSE_CODE[200], None

