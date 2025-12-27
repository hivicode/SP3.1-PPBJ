// Header Component - Shared across all pages
function loadHeader(activePage = '') {
  const headerHTML = `
    <nav class="navbar">
      <div class="logo-container">
        <img
          class="logo-img"
          src="https://api.builder.io/api/v1/image/assets/TEMP/88ae49d6ac3aea10d5fc2fd10a544b233d5bedc1?width=72"
          alt="Phoning Logo"
        />
        <a href="index.html" class="logo-text">Phoning</a>
      </div>
  
      <div class="nav-links">
        <a href="about.html" ${activePage === 'about' ? 'class="active"' : ''}>About us</a>
        <a href="services.html" ${activePage === 'services' ? 'class="active"' : ''}>Services</a>
        <a href="subscribe.html" ${activePage === 'subscribe' ? 'class="active"' : ''}>Subscribe</a>
      </div>
  
      <a href="login.html" class="login-btn">Login</a>
      <div class="hamburger"><i class="ti ti-menu-2"></i></div>
    </nav>
  `;
  
  return headerHTML;
}

// Auto-load header when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  const headerContainer = document.getElementById('header-container');
  if (headerContainer) {
    const activePage = headerContainer.getAttribute('data-page');
    headerContainer.innerHTML = loadHeader(activePage);
  }
});

