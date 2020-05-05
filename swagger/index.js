const express = require('express');
const swaggerJSDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const app = express();

const swaggerDefinition = {
  info: {
    title: 'Login API',
    version: '0.0.1',
    description: '로그인, 로그아웃, 회원정보 조회 API',
  },
  host: '127.0.0.1:5000',
  basePath: '/',
};


const options = {

  swaggerDefinition,

  apis: ['./docs/**/*.yaml'],
};

const swaggerSpec = swaggerJSDoc(options);


app.use('/docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));


const server = app.listen(process.env.PORT || 3000, () => {
    console.log(`'Listening on port '${server.address().port}`);
  });