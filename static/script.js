function meetsLoginConditions() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let err_msg = document.getElementById("messages");

    if (username.length === 0 || password.length === 0) {
        err_msg.innerText = "Please fill in all fields.";
        return false;
    }

    return true;
}

function meetsSignupConditions() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let repassword = document.getElementById("repassword").value;
    let err_msg = document.getElementById("messages");

    if (username.length === 0 || password.length === 0 || repassword.length === 0) {
        err_msg.innerText = "Please fill in all fields.";
        return false;
    }

    // How to use regular expressions in Javascript from:
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
    const username_re = /^[0-9a-zA-Z]+$/;
    if (!username.match(username_re)) {
        err_msg.innerText = "Username may only contain alphanumeric characters.";
        return false;
    }

    const password_re = /^[0-9a-zA-Z!@#$]+$/
    if (!password.match(password_re)) {
        err_msg.innerText = "Password may only contain alphanumeric characters and !, @, #, $";
        return false;
    }

    if (username.length > 32) {
        err_msg.innerText = "Username must be 32 or less characters.";
        return false;
    }

    if (password.length <= 4) {
        err_msg.innerText = "Password must be 5 or more characters.";
        return false;
    }

    if (password.length > 128) {
        err_msg.innerText = "Password must be 128 or less characters.";
        return false;
    }

    if (password !== repassword) {
        err_msg.innerText = "Passwords must match.";
        return false;
    }

    if (username === password) {
        err_msg.innerText = "Username and password must not match.";
        return false;
    }

    return true;
}
