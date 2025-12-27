function login(event) {
    event.preventDefault();
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMsg = document.getElementById("error-message");
  
    if (username === "722@dor.com" && password === "banheesoo") {
      localStorage.setItem("isLogin", "true");
      window.location.href = "dashboard.html";
    } else {
      errorMsg.textContent = "Wrong email or password!";
      errorMsg.style.display = "block";
      
      setTimeout(() => {
        errorMsg.style.display = "none";
      }, 3000);
    }
  }
  
  function checkLogin() {
    if (localStorage.getItem("isLogin") !== "true") {
      window.location.href = "login.html";
    }
  }
  
function logout() {
  localStorage.removeItem("isLogin");
  window.location.href = "login.html";  
}
  