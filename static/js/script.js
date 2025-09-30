// Smooth scroll for navbar links
document.querySelectorAll('.navbar-nav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href')) || document.querySelector(this.getAttribute('href').replace('#', ''));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
  });
});

// Fade-in effect on scroll
const faders = document.querySelectorAll('.fade-in');
const appearOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
const appearOnScroll = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, appearOptions);
faders.forEach(fader => appearOnScroll.observe(fader));

// Mode Toggle
document.getElementById('modeToggle').addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
  document.body.classList.toggle('light-mode');
  document.cookie = `mode=${document.body.classList.contains('dark-mode') ? 'dark' : 'light'}; path=/`;
});

// Animate skill bars on load
window.addEventListener('load', () => {
  document.querySelectorAll('.progress-bar').forEach(bar => {
    bar.style.width = bar.getAttribute('aria-valuenow') + '%';
  });
});