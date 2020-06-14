from sqlalchemy.dialects.mysql import BIGINT, TINYINT, VARCHAR, DATETIME
from . import db


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }

    id = db.Column(BIGINT(11), primary_key=True)
    name = db.Column(VARCHAR(20), nullable=False, comment='이름')
    nickname = db.Column(VARCHAR(30), nullable=False, comment='닉네임')
    password = db.Column(VARCHAR(255), nullable=False, comment='비밀번호')
    phone = db.Column(VARCHAR(20), nullable=False, comment='전화번호')
    email = db.Column(VARCHAR(100), nullable=False, comment='이메일')
    gender = db.Column(TINYINT(1), nullable=True, default=0, comment='성별')
    created_at = db.Column(DATETIME, nullable=False,
                           server_default=db.func.current_timestamp(),
                           comment='생성 시간')
    updated_at = db.Column(DATETIME, nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           comment='수정 시간')

    @property
    def serialize(self):
        return {
            'name': self.name,
            'nick_name': self.nickname,
            'phone': self.phone,
            'email': self.email,
            'gender': self.gender,
            'created_at': self.created_at
        }