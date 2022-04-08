function validLogin(email, password) {
    err_msg = "";
    if (email.length === 0 || password.length === 0) {
        err_msg = "Please fill in all fields.";
        return err_msg;
    }
    return err_msg
}

function meetsLoginConditions() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let err_msg = document.getElementById("messages");

    error = validLogin(email, password);

    if (error === "") {
        return true
    } else {
        err_msg.innerText = error;
        return false;
    }
}

function validSignup(email, username, password, repassword) {
    err_msg = "";
    if (email.length === 0 || username.length === 0 || password.length === 0 || repassword.length === 0) {
        err_msg = "Please fill in all fields.";
        return err_msg;
    }

    // How to use regular expressions in Javascript from:
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
    const email_re = /^[0-9a-zA-Z]+\.?[0-9a-zA-Z]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/;
    if (!email.match(email_re)) {
        err_msg = "Please provie a valid email.";
        return err_msg;
    }

    const username_re = /^[0-9a-zA-Z]+$/;
    if (!username.match(username_re)) {
        err_msg = "Username may only contain alphanumeric characters.";
        return err_msg;
    }

    const password_re = /^[0-9a-zA-Z!@#$]+$/
    if (!password.match(password_re)) {
        err_msg = "Password may only contain alphanumeric characters and !, @, #, $";
        return err_msg;
    }

    if (username.length > 32) {
        err_msg = "Username must be 32 or less characters.";
        return err_msg;
    }

    if (password.length <= 4) {
        err_msg = "Password must be 5 or more characters.";
        return err_msg;
    }

    if (password.length > 128) {
        err_msg = "Password must be 128 or less characters.";
        return err_msg;
    }

    if (password !== repassword) {
        err_msg = "Passwords must match.";
        return err_msg;
    }

    if (username === password) {
        err_msg = "Username and password must not match.";
        return err_msg;
    }

    return err_msg;
}

function meetsSignupConditions() {
    let email = document.getElementById("email").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let repassword = document.getElementById("repassword").value;
    let err_msg = document.getElementById("messages");

    error = validSignup(email, username, password, repassword);

    if (error === "") {
        return true
    } else {
        err_msg.innerText = error;
        return false;
    }
}

module.exports.validLogin = validLogin
module.exports.validSignup = validSignup
