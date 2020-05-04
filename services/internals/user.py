import re
import hashlib

from models.model import db, Users


class UserService(object):
    def __init__(self, body):
        self._body = body

    def __repr__(self):
        return f'self._body : {self._body}'

    def validate_body(self):
        """
        Validate Body (회원가입에 필요한 필수값 확인)
        :return: Boolean
        """
        body = self._body

        if not body.get('name') or not body.get('nick_name') or not body.get('email') \
                or not body.get('phone') or not body.get('password'):
            return None
        return True

    def validate_name(self):
        """
        Validate Name Form (이름 형식)
        :return: Boolean
        """
        name = self._body.get('name').strip()

        if not name:
            return False
        pattern = r"[가-힣a-zA-Z]+"
        result = re.match(pattern=pattern, string=name)

        if not result:
            return False
        return True

    def validate_nick_name(self):
        """
        Validate Nick Name Form (닉네임 형식)
        :return: Boolean
        """
        nick_name = self._body.get('nick_name').strip()

        if not nick_name:
            return False

        pattern = r"[a-z]+$"
        result = re.match(pattern=pattern, string=nick_name)

        if not result:
            return False
        return True

    def validate_email(self):
        """
        Validate Email Form (이메일 형식)
        :return: Boolean
        """
        email = self._body.get('email').strip()

        if not email:
            return False

        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        result = re.match(pattern=pattern, string=email)

        if not result:
            return False
        return True

    def validate_phone(self):
        """
        Validate Phone number Form (숫자)
        :return: Boolean
        """
        phone = self._body.get('phone')

        if not phone:
            return False

        pattern = r"((\d{2}|\(\d{2}\)|\d{3}|\(\d{3}\))(\d{3}|\d{4})(\d{4}))"
        result = re.match(pattern=pattern, string=phone)

        if not result:
            return False
        return True

    def validate_password(self):
        """
        Validate Password Form (영문 대문자, 영문소문자, 특수문자, 숫자 각 1개 이상씩 포함)
        :return: Boolean
        """
        password = self._body.get('password').strip()

        if not password:
            return False

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{10,}"
        result = re.match(pattern=pattern, string=password)

        if not result:
            return False

        return True

    @staticmethod
    def encrypt_password(password):
        sha_signature = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return sha_signature

    def create_user(self):
        """
        회원가입한 유저 정보 DB에 저장
        :return: Boolean
        """
        name = self._body.get('name')
        nickname = self._body.get('nick_name')
        password = self._body.get('password')
        phone = self._body.get('phone')
        email = self._body.get('email')
        gender = self._body.get('gender')

        password = self.encrypt_password(password=password)
        session = db.session()

        try:
            user = Users(name=name,
                         nickname=nickname,
                         password=password,
                         phone=phone,
                         email=email,
                         gender=gender)
            session.add(user)

        except Exception as e:
            print(f'err : {e}')
            session.rollback()
            return False

        else:
            session.commit()
            session.close()
            return True
