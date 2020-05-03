from flask import Blueprint, request

user_blueprint = Blueprint(name='user', import_name=__name__)


@user_blueprint.route('/registration', methods=['POST'], endpoint='user_registration')
def user_registration():
    pass


@user_blueprint.route('/login', methods=['POST'], endpoint='user_login')
def user_login():
    pass


@user_blueprint.route('/logout', methods=['POST'], endpoint='user_logout')
def user_logout():
    pass


@user_blueprint.route('/<int:user_id>/detail', methods=['GET'], endpoint='user_detail')
def user_detail():
    pass


@user_blueprint.route('/details', methods=['GET'], endpoint='user_details')
def user_details():
    pass