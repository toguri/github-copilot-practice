// Jestをインポート
const { main, fizzbuzz, isLeapYear, fizzBuzz, calculateDayBetweenDates } = require('./test.js');

// main関数のテスト
test('main function', () => {
  console.log = jest.fn();
  main();
  expect(console.log).toHaveBeenCalledWith('test');
});

// fizzbuzz関数のテスト
test('fizzbuzz function', () => {
  console.log = jest.fn();
  fizzbuzz();
  expect(console.log).toHaveBeenCalledTimes(100);
});

// isLeapYear関数のテスト
test('isLeapYear function', () => {
  expect(isLeapYear(2000)).toBe(true);
  expect(isLeapYear(2001)).toBe(false);
  expect(isLeapYear(2004)).toBe(true);
  expect(isLeapYear(2100)).toBe(false);
});

// fizzBuzz関数のテスト
test('fizzBuzz function', () => {
  console.log = jest.fn();
  fizzBuzz(1, 15);
  expect(console.log).toHaveBeenCalledTimes(15);
});

// calculateDayBetweenDates関数のテスト
test('calculateDayBetweenDates function', () => {
  expect(calculateDayBetweenDates('2022-01-01', '2022-01-31')).toBe(30);
  expect(calculateDayBetweenDates('2022-01-01', '2022-02-01')).toBe(31);
});