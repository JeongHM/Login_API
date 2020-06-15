import os
import json
from flask import request, Response

from copy import deepcopy
from utils.response_code import RESPONSE_CODE


def response_format(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)

        if result:
            res_copy = deepcopy(res)
            res_copy['result'] = result
            res = res_copy

        resp = json.dumps(res, ensure_ascii=False, default=str).encode('utf-8')
        return Response(response=resp, content_type='application/json; charset:utf-8')
    return wrapper


def header_required(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('Api-Key')

        if not api_key and (api_key != os.getenv('API_KEY')):
            return RESPONSE_CODE['MISSING_REQUIRED_HEADER']

        return func(*args, **kwargs)
    return wrapper


def token_required(func):
    def wrapper(*args, **kwargs):
        access_token = dict(request.headers).get('Access-Token')

        if not access_token:
            return RESPONSE_CODE['MISSING_TOKEN_HEADER']
        return func(*args, **kwargs)
    return wrapper
