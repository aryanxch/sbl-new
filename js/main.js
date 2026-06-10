// ============ NAV SCROLL ============
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 30) navbar.classList.add('scrolled');
  else navbar.classList.remove('scrolled');
});

// ============ MOBILE BURGER ============
const burger = document.getElementById('burger');
const navMenu = document.querySelector('.nav-menu');
burger?.addEventListener('click', () => {
  navMenu.classList.toggle('open');
});
document.querySelectorAll('.nav-menu a').forEach(a => {
  a.addEventListener('click', () => navMenu.classList.remove('open'));
});

// ============ REVEAL ON SCROLL ============
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// ============ STAT COUNTERS ============
const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const suffix = el.textContent.includes('%') ? '%' : '+';
      let current = 0;
      const duration = 1800;
      const start = performance.now();
      const tick = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        current = Math.floor(eased * target);
        el.textContent = current + (progress === 1 ? suffix : '');
        if (progress < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      statObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-num[data-target]').forEach(el => statObserver.observe(el));

// ============ CYCLING PRODUCT BADGE ============
// Rotates through brand names on product pages where a list was supplied.
document.querySelectorAll('.prod-img-badge[data-brands]').forEach(badge => {
  let brands;
  try { brands = JSON.parse(badge.dataset.brands); } catch { return; }
  if (!Array.isArray(brands) || brands.length < 2) return;
  const nameEl = badge.querySelector('.badge-name');
  if (!nameEl) return;
  let i = 0;
  setInterval(() => {
    i = (i + 1) % brands.length;
    nameEl.style.opacity = '0';
    nameEl.style.transform = 'translateY(6px)';
    setTimeout(() => {
      nameEl.textContent = brands[i];
      nameEl.style.opacity = '1';
      nameEl.style.transform = 'translateY(0)';
    }, 220);
  }, 2200);
});

// ============ ROTATING PRODUCT IMAGE ============
// Cross-fades through a list of images on product pages where data-images was supplied.
document.querySelectorAll('.prod-img-frame[data-images]').forEach(frame => {
  let images;
  try { images = JSON.parse(frame.dataset.images); } catch { return; }
  if (!Array.isArray(images) || images.length < 2) return;
  const imgEl = frame.querySelector('img');
  if (!imgEl) return;
  images.forEach(src => { const pre = new Image(); pre.src = src; }); // preload
  imgEl.style.transition = 'opacity .5s ease, transform .6s ease';
  let i = 0;
  setInterval(() => {
    i = (i + 1) % images.length;
    imgEl.style.opacity = '0';
    setTimeout(() => {
      imgEl.src = images[i];
      imgEl.style.opacity = '1';
    }, 500);
  }, 3500);
});

// ============ SMOOTH ANCHOR SCROLL OFFSET ============
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', (e) => {
    const id = a.getAttribute('href');
    if (id.length > 1) {
      const tgt = document.querySelector(id);
      if (tgt) {
        e.preventDefault();
        const offset = 80;
        const top = tgt.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    }
  });
});
