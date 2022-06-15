const express = require('express');
const router = express.Router();

router.use('/python',require("./python"));

console.log("여기 실행됨")

module.exports = router;
