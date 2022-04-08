const { test } = require('@jest/globals');
const script = require('../script');
const validLogin = script.validLogin
const validSignup = script.validSignup

// validLogin tests
test('Regular Email, Regular Password', () => {
  expect(validLogin("username@website.com", "RegularPassword42")).toBe("");
});

test('No Email, Regular Password', () => {
  expect(validLogin("", "RegularPassword42")).toBe("Please fill in all fields.");
});

test('Regular Email, No Password', () => {
  expect(validLogin("username@website.com", "")).toBe("Please fill in all fields.");
});

test('No Email, No Password', () => {
  expect(validLogin("", "")).toBe("Please fill in all fields.");
});

// validSignup tests
test('Regular Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "Username", "RegularPassword42", "RegularPassword42")).toBe("");
});

test('No Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("", "Username", "RegularPassword42", "RegularPassword42")).toBe("Please fill in all fields.");
});

test('Regular Email, No Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "", "RegularPassword42", "RegularPassword42")).toBe("Please fill in all fields.");
});

test('Regular Email, Regular Username, No Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "Username", "", "RegularPassword42")).toBe("Please fill in all fields.");
});

test('Regular Email, Regular Username, Regular Password, No Repassword', () => {
  expect(validSignup("username@website.com", "Username", "RegularPassword42", "")).toBe("Please fill in all fields.");
});

test('firstname.lastname Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("jesal.patel@example.com", "Username", "RegularPassword42", "RegularPassword42")).toBe("");
});

test('One Word Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("fake", "Username", "RegularPassword42", "RegularPassword42")).toBe("Please provie a valid email.");
});

test('Multiple Period Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("jesal.h.patel@example.com", "Username", "RegularPassword42", "RegularPassword42")).toBe("Please provie a valid email.");
});

test('Just Periods Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("........@example.com", "Username", "RegularPassword42", "RegularPassword42")).toBe("Please provie a valid email.");
});

test('Nothing after @ Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("jesalpatel@", "Username", "RegularPassword42", "RegularPassword42")).toBe("Please provie a valid email.");
});

test('Nothing after *@*. Email, Regular Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("jesalpatel@example", "Username", "RegularPassword42", "RegularPassword42")).toBe("Please provie a valid email.");
});

test('Regular Email, "/" Character Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "/", "RegularPassword42", "RegularPassword42")).toBe("Username may only contain alphanumeric characters.");
});

test('Regular Email, "*" Containing Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "*username", "RegularPassword42", "RegularPassword42")).toBe("Username may only contain alphanumeric characters.");
});

test('Regular Email, Long Username, Regular Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "RegularPassword42", "RegularPassword42")).toBe("Username must be 32 or less characters.");
});

test('Regular Email, Regular Username, Short Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "Username", "abc", "abc")).toBe("Password must be 5 or more characters.");
});

test('Regular Email, Regular Username, Different Password, Different Repassword', () => {
  expect(validSignup("username@website.com", "Username", "FirstPassword", "SecondPassword")).toBe("Passwords must match.");
});

test('Regular Email, Matching Password Username, Matching Username Password, Regular Repassword', () => {
  expect(validSignup("username@website.com", "Password", "Password", "Password")).toBe("Username and password must not match.");
});
