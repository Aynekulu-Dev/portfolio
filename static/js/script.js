// Smooth scroll for navbar links
document.querySelectorAll('.navbar-nav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({behavior: 'smooth'});
  });
});

// Fade-in effect on scroll
const faders = document.querySelectorAll('.fade-in');
const appearOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
const appearOnScroll = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, appearOptions);

faders.forEach(fader => appearOnScroll.observe(fader));
