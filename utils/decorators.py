import json
from flask import request, Response
from utils.response_code import RESPONSE_CODE


def response_format(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)

        if result:
            res['result'] = result

        resp = json.dumps(res, ensure_ascii=False, default=str).encode('utf-8')
        return Response(response=resp, content_type='application/json; charset:utf-8')
    return wrapper


def token_required(func):
    def wrapper(*args, **kwargs):
        access_token = dict(request.headers).get('Access-Token')

        if not access_token:
            return RESPONSE_CODE[401]
        return func(*args, **kwargs)
    return wrapper
