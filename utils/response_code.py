RESPONSE_CODE = {
    'SUCCESS': {
        'status_code': 200,
        'message': '요청이 정상 처리 되었습니다.'
    },
    'MISSING_REQUIRED_VALUE': {
        'status_code': 400,
        'message': '필수값 누락입니다. 필수값을 확인해주세요.'
    },
    'MISSING_REQUIRED_HEADER': {
        'status_code': 401,
        'message': '인증에 실패하였습니다. 헤더 필수값이 없습니다.'
    },
    'MISSING_TOKEN_HEADER': {
        'status_code': 401,
        'message': '인증에 실패하였습니다. 토큰값이 없습니다.'
    },
    'NOT_FOUND': {
        'status_code': 404,
        'message': '데이터가 없거나 잘못된 경로 입니다.'
    },
    'INVALID_NAME_FORMAT': {
        'status_code': 800,
        'message': '이름에 띄어쓰기가 있거나 형식이 맞지 않습니다.'
    },
    'INVALID_NICK_NAME_FORMAT': {
        'status_code': 801,
        'message': '닉네임에 띄어쓰기가 있거나 형식이 맞지 않습니다.'
    },
    'INVALID_EMAIL_FORMAT': {
        'status_code': 802,
        'message': '이메일에 띄어쓰기가 있거나 형식이 맞지 않습니다.'
    },
    'INVALID_PHONE_FORMAT': {
        'status_code': 803,
        'message': '전화번호에 띄어쓰기가 있거나 형식이 맞지 않습니다.'
    },
    'INVALID_PASSWORD_FORMAT': {
        'status_code': 804,
        'message': '비밀번호에 띄어쓰기가 있거나 형식이 맞지 않습니다.'
    },
    'LOGIN_FAIL': {
        'status_code': 805,
        'message': '로그인에 실패하였습니다. 이메일 혹은 패스워드를 정확히 입력해주세요.'
    },
    'TOKEN_EXPIRED': {
        'status_code': 806,
        'message': '토큰이 만료되었습니다. 다시 로그인 및 토큰 재발급을 해주세요.'
    }
}