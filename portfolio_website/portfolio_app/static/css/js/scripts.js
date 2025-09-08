document.addEventListener('DOMContentLoaded', () => {
  if (window.gsap) {
    // Fancy card entrance
    gsap.from('[data-gsap="card"]', {
      y: 40,
      opacity: 0,
      scale: 0.95,
      rotation: (i) => (i % 2 === 0 ? 2 : -2), // alternate tilt
      stagger: 0.15,
      duration: 0.9,
      ease: 'power3.out'
    });

    // Add hover interaction
    document.querySelectorAll('[data-gsap="card"]').forEach(card => {
      card.addEventListener('mouseenter', () => {
        gsap.to(card, {scale: 1.05, boxShadow: '0 12px 24px rgba(0,0,0,0.15)', duration: 0.3});
      });
      card.addEventListener('mouseleave', () => {
        gsap.to(card, {scale: 1, boxShadow: '0 6px 12px rgba(0,0,0,0.08)', duration: 0.3});
      });
    });
  }

  // Animate progress bars when visible
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('.bar').forEach(bar => {
          const level = bar.closest('.skill-card')?.dataset.level || bar.dataset.level || 70;

          // Animate width and color
          gsap.fromTo(bar,
            {width: '0%', backgroundColor: '#ccc'},
            {
              width: level + '%',
              backgroundColor: gsap.utils.random(['#4cafef', '#ff6f61', '#9c27b0', '#4caf50']),
              duration: 1.2,
              ease: 'elastic.out(1, 0.6)'
            }
          );
        });
        obs.unobserve(entry.target);
      }
    });
  }, {threshold: 0.25});

  document.querySelectorAll('.skills-grid, .skill-card').forEach(el => observer.observe(el));
});
