import jwt
from datetime import datetime, timedelta
from Cryptodome import Random

from models import db
from models.tokens import Tokens


class TokenService(object):
    def __init__(self, user_id):
        self._user_id = user_id
        self._key_len = 12

    def create_token(self):
        """
        JWT Token 생성 및 토큰 정보 DB 저장
        :return: Boolean Object OR Token Object
        """
        key = Random.new().read(self._key_len).hex()
        expired_at = int((datetime.utcnow() + timedelta(minutes=10000)).timestamp())
        payload = {'user_id': self._user_id, 'exp': expired_at}
        access_token = jwt.encode(payload=payload, key=key, algorithm='HS256').decode('utf-8')
        session = db.session()

        try:
            token = Tokens(access_token=access_token, key=key, expired_at=expired_at)
            session.add(token)

        except Exception as e:
            session.rollback()
            return False

        else:
            session.commit()
            session.close()
            result = {'access_token': access_token}
            return result

    @staticmethod
    def delete_token(access_token):
        """
        로그아웃으로 인한 토큰 정보 삭제
        :return: Boolean Object
        """
        session = db.session()

        try:
            Tokens.query.filter_by(access_token=access_token).delete()

        except Exception as e:
            session.rollback()
            return False

        else:
            session.commit()
            session.close()
            return True

    @staticmethod
    def get_user_id_by_token(access_token):
        """
        Access Token을 가지고 user id 값 추출
        :param access_token: JWT Token
        :return: Boolean OR User ID
        """
        try:
            token = Tokens.query.filter_by(access_token=access_token).first()
            key = token.key
            payload = jwt.decode(jwt=access_token, key=key)
            user_id = payload.get('user_id')

        except jwt.ExpiredSignatureError:
            return False, None

        except jwt.InvalidTokenError:
            return False, None

        else:
            return True, user_id
