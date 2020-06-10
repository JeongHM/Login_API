from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME, INTEGER
from . import db


class Tokens(db.Model):
    __tablename__ = 'tokens'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }

    id = db.Column(BIGINT(11), primary_key=True)
    key = db.Column(VARCHAR(255), nullable=False, comment='키')
    access_token = db.Column(VARCHAR(255), nullable=False, comment='토큰')
    expired_at = db.Column(BIGINT(11), nullable=False, comment='만료시간')
    created_at = db.Column(DATETIME, nullable=False,
                           server_default=db.func.current_timestamp(),
                           comment='생성 시간')
