function login(event) {
    event.preventDefault();
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMsg = document.getElementById("error-message");
  
    if (username === "admin" && password === "123") {
      localStorage.setItem("isLogin", "true");
      window.location.href = "dashboard.html";
    } else {
      errorMsg.textContent = "Username atau password salah!";
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
