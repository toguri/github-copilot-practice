// このファイルはテスト用のファイルです
function main() {
    console.log('test');
    // Express server on port 3000
var express = require('express');
var app = express();
app.get('/', function(req, res) {
  res.send('Hello World');
});
app.listen(3000);

}

// fizzbuzz.js
// このファイルはfizzbuzzを実行するファイルです
function fizzbuzz() {
 for (var i = 1; i <= 100; i++) {
   if (i % 15 === 0) {
     console.log('FizzBuzz');
   } else if (i % 3 === 0) {
     console.log('Fizz');
   } else if (i % 5 === 0) {
     console.log('Buzz');
   } else {
     console.log(i);
   }
 } 
}

// うるうどしを計算する関数
function isLeapYear(year) {
  if (year % 4 === 0 && year % 100 !== 0) {
    return true;
  } else if (year % 400 === 0) {
    return true;
  } else {
    return false;
  } 
}

// fizz buzzを実行する関数
// 引数には開始年と終了年を指定する
// 例: fizzBuzz(2011, 2012)
// 2011年から2012年までのfizz buzzを実行する
function fizzBuzz(startYear, endYear) {
  for (var i = startYear; i <= endYear; i++) {
    if (i % 15 === 0) {
      console.log('FizzBuzz');
    } else if (i % 3 === 0) {
      console.log('Fizz');
    } else if (i % 5 === 0) {
      console.log('Buzz');
    } else {
      console.log(i);
    }
  } 
}

// fizz buzzを実行する関数
function fizzBuzz(startYear, endYear) {
  for (var i = startYear; i <= endYear; i++) {
    if (i % 15 === 0) {
      console.log('FizzBuzz');
    } else if (i % 3 === 0) {
      console.log('Fizz');
    } else if (i % 5 === 0) {
      console.log('Buzz');
    } else {
      console.log(i);
    }
  } 
}

function calculateDayBetweenDates(begin, end){
  var beginDate = new Date(begin);
  var endDate = new Date(end);
  var diff = endDate.getTime() - beginDate.getTime();
  var diffDays = diff / (1000 * 3600 * 24);
  return diffDays;
}

// うるう年を計算する関数
function isLeapYear(year) {
  if (year % 4 === 0 && year % 100 !== 0) {
    return true;
  } else if (year % 400 === 0) {
    return true;
  } else {
    return false;
  } 
}

