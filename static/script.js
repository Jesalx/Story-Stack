/* eslint-disable no-unused-vars */
function validLogin(email, password) {
  let errMsg = '';
  if (email.length === 0 || password.length === 0) {
    errMsg = 'Please fill in all fields.';
    return errMsg;
  }
  return errMsg;
}

function meetsLoginConditions() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const errMsg = document.getElementById('messages');

  const error = validLogin(email, password);

  if (error === '') {
    errMsg.innerText = '';
    return true;
  }

  errMsg.innerText = error;
  return false;
}

function validSignup(email, username, password, repassword) {
  let errMsg = '';
  if (email.length === 0 || username.length === 0
    || password.length === 0 || repassword.length === 0) {
    errMsg = 'Please fill in all fields.';
    return errMsg;
  }

  // How to use regular expressions in Javascript from:
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
  const emailRe = /^[0-9a-zA-Z]+\.?[0-9a-zA-Z]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/;
  if (!email.match(emailRe)) {
    errMsg = 'Please provie a valid email.';
    return errMsg;
  }

  const usernameRe = /^[0-9a-zA-Z]+$/;
  if (!username.match(usernameRe)) {
    errMsg = 'Username may only contain alphanumeric characters.';
    return errMsg;
  }

  const passwordRe = /^[0-9a-zA-Z!@#$]+$/;
  if (!password.match(passwordRe)) {
    errMsg = 'Password may only contain alphanumeric characters and !, @, #, $';
    return errMsg;
  }

  if (username.length > 32) {
    errMsg = 'Username must be 32 or less characters.';
    return errMsg;
  }

  if (password.length <= 4) {
    errMsg = 'Password must be 5 or more characters.';
    return errMsg;
  }

  if (password.length > 128) {
    errMsg = 'Password must be 128 or less characters.';
    return errMsg;
  }

  if (password !== repassword) {
    errMsg = 'Passwords must match.';
    return errMsg;
  }

  if (username === password) {
    errMsg = 'Username and password must not match.';
    return errMsg;
  }

  return errMsg;
}

function meetsSignupConditions() {
  const email = document.getElementById('email').value;
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const repassword = document.getElementById('repassword').value;
  const errMsg = document.getElementById('messages');

  const error = validSignup(email, username, password, repassword);

  if (error === '') {
    errMsg.innerText = '';
    return true;
  }

  errMsg.innerText = error;
  return false;
}

module.exports.validLogin = validLogin;
module.exports.validSignup = validSignup;
