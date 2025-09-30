// Animate skill progress bars when in view
function animateSkillBars() {
  const progressEls = document.querySelectorAll('.skill-progress');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target.querySelector('.progress-bar');
        const level = entry.target.dataset.level || 0;
        bar.style.width = level + '%';
        bar.textContent = level + '%';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  progressEls.forEach(el => observer.observe(el));
}

// Project modal handling
function setupProjectModal() {
  const modalEl = document.getElementById('projectModal');
  if (!modalEl) return;
  const modal = new bootstrap.Modal(modalEl);

  function openModal(title, desc, image) {
    document.getElementById('projectModalTitle').textContent = title;
    const imgEl = document.getElementById('projectModalImage');
    imgEl.src = image;
    imgEl.alt = title;
    document.getElementById('projectModalDesc').textContent = desc;
    modal.show();
  }

  document.querySelectorAll('.card-img-clickable, .view-more-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const title = e.currentTarget.dataset.title;
      const desc = e.currentTarget.dataset.desc;
      const image = e.currentTarget.dataset.image;
      openModal(title, desc, image);
    });
  });
}

// Contact form basic client-side validation
function setupContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    const name = form.querySelector('[name=name]');
    const email = form.querySelector('[name=email]');
    const message = form.querySelector('[name=message]');
    let valid = true;

    // simple checks
    if (!name.value.trim()) {
      name.classList.add('is-invalid');
      valid = false;
    } else {
      name.classList.remove('is-invalid');
    }

    if (!email.value.trim() || !email.value.includes('@')) {
      email.classList.add('is-invalid');
      valid = false;
    } else {
      email.classList.remove('is-invalid');
    }

    if (!message.value.trim()) {
      message.classList.add('is-invalid');
      valid = false;
    } else {
      message.classList.remove('is-invalid');
    }

    if (!valid) {
      e.preventDefault();
      return false;
    }
    // otherwise allow normal submit (server handles saving/email)
  });
}

// Smooth scroll for anchor links (optional)
function setupSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
  });
}

// Init on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  animateSkillBars();
  setupProjectModal();
  setupContactForm();
  setupSmoothScroll();
});
