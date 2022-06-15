const express = require('express');
const path = require('path');
// const models=require("./models");
const session  = require('express-session');
const indexrouter = require("./routes/index");
const morgan = require("morgan");
const cookieParser = require('cookie-parser');
var os = require('os');


const app = express();//서버생성
app.use(session({ secret: 'somevalue' }));
app.set('port',process.env.PORT || 3000);
app.use(morgan('dev'));
app.use('/', express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({extended:false}));
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(session({
      resave:false,
      saveUninitialized: false,
      secret: process.env.COOKIE_SECRET,
      cookie:{
            httpOnly:true,
            secure:false,
      },
      name:'sesion-cookie'
}));
function getServerIp() {
      var ifaces = os.networkInterfaces();
      var result = '';
      for (var dev in ifaces) {
          var alias = 0;
          ifaces[dev].forEach(function(details) {
              if (details.family == 'IPv4' && details.internal === false) {
                  result = details.address;
                  ++alias;
              }
          });
      }
      return result;
  }
  
  console.log(getServerIp());

app.get('/', (req,res)=>{
      res.send('Hello, Express');
      console.log("app 까지 왔다");
});

app.listen(app.get('port'), () =>{
      console.log(app.get('port'), '번 포트에서 대기중');
});

// models.sequelize.sync().then( () => {
//       console.log(" DB 연결 성공");
//     }).catch(err => {
//       console.log("연결 실패");
//       console.log(err);
//     });

app.use('/index',indexrouter);