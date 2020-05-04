import jwt
import hashlib
import base64
from datetime import datetime, timedelta
from Cryptodome import Random


class TokenService(object):
    def __init__(self, body):
        self._body = body
        self._key_len = 12

    def create_token(self):
        try:
            key = Random.new().read(self._key_len).hex()
            expired_at = datetime.utcnow() + timedelta(minutes=30)

            payload = {
                'user_id': None,
                'exp': expired_at
            }
            access_token = jwt.encode(payload=payload, key=key, algorithm='HS256')

        except Exception as e:
            return False

        else:
            result = {'access_token': access_token}
            return result

