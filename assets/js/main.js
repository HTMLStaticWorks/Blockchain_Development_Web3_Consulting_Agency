/**
 * Blockchain Development & NodeX Consulting Agency - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initRTLToggle();
  initBackToTop();
  initFormValidation();
});

/**
 * Theme Toggle (Light/Dark Mode)
 */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('theme-toggle');
  if (!themeToggleBtn) return;

  const currentTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', currentTheme);

  themeToggleBtn.addEventListener('click', () => {
    let theme = document.documentElement.getAttribute('data-theme');
    let targetTheme = theme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', targetTheme);
    localStorage.setItem('theme', targetTheme);
  });
}

/**
 * RTL Toggle
 */
function initRTLToggle() {
  const rtlToggleBtn = document.getElementById('rtl-toggle');
  if (!rtlToggleBtn) return;

  const currentDir = localStorage.getItem('dir') || 'ltr';
  document.documentElement.setAttribute('dir', currentDir);

  rtlToggleBtn.addEventListener('click', () => {
    let dir = document.documentElement.getAttribute('dir');
    let targetDir = dir === 'ltr' ? 'rtl' : 'ltr';
    
    document.documentElement.setAttribute('dir', targetDir);
    localStorage.setItem('dir', targetDir);
  });
}

/**
 * Back to Top Button
 */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTop');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  });

  backToTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/**
 * Client-Side Form Validation
 */
function initFormValidation() {
  const forms = document.querySelectorAll('.needs-validation');

  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });
}
