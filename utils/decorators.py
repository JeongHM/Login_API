import json
from flask import request, Response


def response_format(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)

        if result:
            res['result'] = result

        resp = json.dumps(res, ensure_ascii=False, default=str).encode('utf-8')
        return Response(response=resp, content_type='application/json; charset:utf-8')
    return wrapper
