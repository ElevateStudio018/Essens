// Mobile menu
const nav = document.querySelector('.nav');
document.querySelector('.burger')?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  document.querySelector('.burger').setAttribute('aria-expanded', open);
});

// Reveal on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// Project filter
document.querySelectorAll('.filters button').forEach((btn) => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filters button').forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    document.querySelectorAll('[data-cat]').forEach((card) => {
      card.classList.toggle('hide', f !== 'alla' && !card.dataset.cat.split(' ').includes(f));
    });
  });
});

// Lightbox
const lb = document.querySelector('.lb');
if (lb) {
  const lbImg = lb.querySelector('img');
  document.querySelectorAll('.gallery figure img').forEach((img) => {
    img.addEventListener('click', () => { lbImg.src = img.src; lbImg.alt = img.alt; lb.classList.add('open'); });
  });
  const close = () => lb.classList.remove('open');
  lb.addEventListener('click', (e) => { if (e.target !== lbImg) close(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
}

// Contact form: opens the visitor's mail client with the request prefilled
document.querySelector('#forfragan')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const d = new FormData(e.target);
  const typ = d.getAll('typ').join(', ');
  const body = [
    `Namn: ${d.get('namn')}`,
    `E-post: ${d.get('epost')}`,
    `Telefon: ${d.get('telefon') || '-'}`,
    `Adress/plats: ${d.get('adress') || '-'}`,
    `Typ av projekt: ${typ || '-'}`,
    '',
    d.get('beskrivning'),
  ].join('\n');
  location.href = `mailto:kontakt@essensarkitektur.se?subject=${encodeURIComponent('Projektförfrågan – ' + d.get('namn'))}&body=${encodeURIComponent(body)}`;
});
