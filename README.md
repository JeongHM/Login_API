# Login API

## Spec
1. Python 3.7 
2. Flask
3. Docker
4. MySQL
5. Node.js (Swagger Server)

## File Struct
```
├── controllers
│   └── 컨트롤러 관련 파일
├── models
│   └── 모델 관련 파일
├── services
│   └── 비지니스 로직 관련 파일
├── swagger
│   └── 스웨거
├── utils
│   └── API 내 공통으로 사용 관련 파일
│
├── application.py
├── requirements.txt
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── 00_build.sh # 처음 실행 시 해당 스크립트를 실행시켜주세요
└── README.md
```

### 파일 실행
1. 00_build.sh 를 이용하여 docker build 실행 
2. 실행 후 mysql server, API server 동작
3. swagger 서버를 사용하기위해 /swagger 내에서 `npm install` -> `node index.js` 실행
4. API 명세에 맞게 API 사용

```bash
$ git clone https://github.com/JeongHM/Login_API.git

$ sh 00_build.sh


# 새로운 탭을 열어주세요
$ cd swagger
$ npm install
$ node index.js  # 127.0.0.1:3000/docs 접속
```