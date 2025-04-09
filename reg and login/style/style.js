const loginBox = document.getElementById("login");
const registerBox = document.getElementById("register");
const loginToregisterLink = document.getElementById("login_to_register");
const registerToLoginLink = document.getElementById("register_to_login");

loginToregisterLink.addEventListener("click",function(e) {
    e.preventDefault();
    loginBox.style.display = "none";
    registerBox.style.display = "block";
});

registerToLoginLink.addEventListener("click",function(e) {
    e.preventDefault();
    registerBox.style.display = "none";
    loginBox.style.display = "block";
});