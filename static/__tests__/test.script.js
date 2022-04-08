const { test, expect } = require('@jest/globals');
const script = require('../script');

const { validLogin, validSignup } = script;

// validLogin tests
test('Login: Regular Email, Regular Password', () => {
  expect(validLogin('username@website.com', 'RegularPassword42')).toBe('');
});

test('Login: No Email, Regular Password', () => {
  expect(validLogin('', 'RegularPassword42')).toBe('Please fill in all fields.');
});

test('Login: Regular Email, No Password', () => {
  expect(validLogin('username@website.com', '')).toBe('Please fill in all fields.');
});

test('Login: No Email, No Password', () => {
  expect(validLogin('', '')).toBe('Please fill in all fields.');
});

// validSignup tests
test('Signup: Regular Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('');
});

test('Signup: No Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('Please fill in all fields.');
});

test('Signup: Regular Email, No Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', '', 'RegularPassword42', 'RegularPassword42')).toBe('Please fill in all fields.');
});

test('Signup: Regular Email, Regular Username, No Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', 'Username', '', 'RegularPassword42')).toBe('Please fill in all fields.');
});

test('Signup: Regular Email, Regular Username, Regular Password, No Repassword', () => {
  expect(validSignup('username@website.com', 'Username', 'RegularPassword42', '')).toBe('Please fill in all fields.');
});

test('Signup: firstname.lastname Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('jesal.patel@example.com', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('');
});

test('Signup: One Word Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('fake', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('Please provie a valid email.');
});

test('Signup: Multiple Period Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('jesal.h.patel@example.com', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('Please provie a valid email.');
});

test('Signup: Just Periods Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('........@example.com', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('Please provie a valid email.');
});

test('Signup: Nothing after @ Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('jesalpatel@', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('Please provie a valid email.');
});

test('Signup: Nothing after *@*. Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('jesalpatel@example', 'Username', 'RegularPassword42', 'RegularPassword42')).toBe('Please provie a valid email.');
});

test('Signup: Regular Email,"/" Character Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', '/', 'RegularPassword42', 'RegularPassword42')).toBe('Username may only contain alphanumeric characters.');
});

test('Signup: Regular Email, "*" Containing Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', '*username', 'RegularPassword42', 'RegularPassword42')).toBe('Username may only contain alphanumeric characters.');
});

test('Signup: Regular Email, Long Username, Regular Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'RegularPassword42', 'RegularPassword42')).toBe('Username must be 32 or less characters.');
});

test('Signup: Regular Email, Regular Username, Short Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', 'Username', 'abc', 'abc')).toBe('Password must be 5 or more characters.');
});

test('Signup: Regular Email, Regular Username, Different Password, Different Repassword', () => {
  expect(validSignup('username@website.com', 'Username', 'FirstPassword', 'SecondPassword')).toBe('Passwords must match.');
});

test('Signup: Regular Email, Matching Password Username, Matching Username Password, Regular Repassword', () => {
  expect(validSignup('username@website.com', 'Password', 'Password', 'Password')).toBe('Username and password must not match.');
});
