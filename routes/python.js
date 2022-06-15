const express = require('express');
const fs = require('fs');
const router = express.Router();



router.get('/lottepos',async(req,res)=>{

    fs.readFile('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/롯데긍정리뷰.png', function(error, data){
      res.writeHead(200, {'Content-Type': 'lottepos.html'});
      res.end(data);
      console.log(data);
    })
})

router.get('/lotteneg',async(req,res)=>{
  fs.readFile('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/롯데부정리뷰.png', function(error, data){
    res.writeHead(200, {'Content-Type': 'lotteneg.html'});
    res.end(data);
    console.log(data);
  })
})
router.get('/orakaipos',async(req,res)=>{

  fs.readFile('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/오라카이긍정리뷰.png', function(error, data){
    res.writeHead(200, {'Content-Type': 'orakaipos.html'});
    res.end(data);
    console.log(data);
  })
})

router.get('/orakaineg',async(req,res)=>{
  fs.readFile('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/오라카이부정리뷰.png', function(error, data){
    res.writeHead(200, {'Content-Type': 'orakaineg.html'});
    res.end(data);
    console.log(data);
  })
})
router.get('/mondrianpos',async(req,res)=>{

  fs.readFile('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/몬드리안긍정리뷰.png', function(error, data){
    res.writeHead(200, {'Content-Type': 'mondrianpos.html'});
    res.end(data);
    console.log(data);
  })
})

router.get('/mondrianneg',async(req,res)=>{
  fs.readFile('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/몬드리안부정리뷰.png', function(error, data){
    res.writeHead(200, {'Content-Type': 'mondrianneg.html'});
    res.end(data);
    console.log(data);
  })
})
  // router.get('/',async(req,res)=>{

  //   var filename ='wordcloud.jpg';
     
     // const 파일명 = 'file.ext';  
    //  res.setHeader('content-type', 'image/jpg');
    //  res.setHeader('Content-Disposition', `attachment; filename=${filename}`); // 이게 핵심 
    //  res.send('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/wordcloud.png');


     // const spawn = require('child_process').spawn;

     // const result = spawn('python', ['./routes/print.py']);

     // result.stdout.on('data', function(data) {
     // console.log(data.toString());


     

     // });

//  })

module.exports = router;
