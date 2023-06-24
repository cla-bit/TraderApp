const logo = document.querySelector(".logo");
const login = document.querySelector(".login");
const signup = document.querySelector(".signup");
const loginAndReg = document.querySelector(".login-and-reg");
const goSignUp = document.querySelector(".login span span");
const goSignIn = document.querySelector(".signup span span");
// const loginBtn = document.querySelector(".login-btn");
const loginForm = document.querySelector(".login form");
const signupForm = document.querySelector(".signup form");
console.log(loginForm);

// window.onload = () => {
document.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => {
    logo.style.display = "none";
    loginAndReg.style.display = "block";
  }, 4000);
});
// };

goSignUp.onclick = () => {
  login.style.display = "none";
  signup.style.display = "block";
};

goSignIn.onclick = () => {
  login.style.display = "block";
  signup.style.display = "none";
};

// loginBtn.onclick = () => {};

loginForm.onsubmit = (e) => {
  e.preventDefault();
  location.href = "./pages/dashboard.html";
};

signupForm.onsubmit = (e) => {
  e.preventDefault();
};
