(() => {
  const body = document.body;
  const header = document.querySelector('[data-header]');
  const navToggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');

  const onScroll = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) {
        nav.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.04 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }

  document.querySelectorAll('[data-copy]').forEach((button) => {
    button.addEventListener('click', async () => {
      const container = button.closest('pre, .example-code, .install-card');
      const code = container ? container.querySelector('code') : null;
      if (!code) return;
      const text = code.innerText.trim();
      try {
        await navigator.clipboard.writeText(text);
      } catch {
        const area = document.createElement('textarea');
        area.value = text;
        area.style.position = 'fixed';
        area.style.opacity = '0';
        document.body.appendChild(area);
        area.select();
        document.execCommand('copy');
        area.remove();
      }
      const original = button.textContent;
      button.textContent = '已复制';
      button.classList.add('is-copied');
      window.setTimeout(() => {
        button.textContent = original;
        button.classList.remove('is-copied');
      }, 1600);
    });
  });

  const search = document.querySelector('[data-search-input]');
  const cards = [...document.querySelectorAll('[data-plugin]')];
  const chips = [...document.querySelectorAll('[data-filter]')];
  const resultLine = document.querySelector('[data-result-line]');
  const empty = document.querySelector('[data-empty]');
  let activeDomain = 'all';

  const applyFilter = () => {
    const query = (search?.value || '').trim().toLowerCase();
    let visible = 0;
    cards.forEach((card) => {
      const domainMatch = activeDomain === 'all' || card.dataset.domain === activeDomain;
      const textMatch = !query || card.dataset.search.includes(query);
      const show = domainMatch && textMatch;
      card.hidden = !show;
      if (show) visible += 1;
    });
    if (resultLine) {
      const domainName = activeDomain === 'all' ? '' : ` · ${chips.find((c) => c.dataset.filter === activeDomain)?.textContent.replace(/\d+/g, '').trim() || ''}`;
      resultLine.textContent = `显示 ${visible} 个技能${domainName}`;
    }
    if (empty) empty.hidden = visible !== 0;
  };

  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      activeDomain = chip.dataset.filter;
      chips.forEach((item) => item.classList.toggle('is-active', item === chip));
      applyFilter();
      document.querySelector('#plugins')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
  search?.addEventListener('input', applyFilter);

  document.querySelectorAll('[data-domain-jump]').forEach((link) => {
    link.addEventListener('click', () => {
      const id = link.dataset.domainJump;
      const chip = chips.find((item) => item.dataset.filter === id);
      if (chip) chip.click();
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && search && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      event.preventDefault();
      search.focus();
    }
  });

  document.querySelectorAll('[data-copy], [data-copy-page]').forEach((button) => {
    if (button.dataset.copyPage) {
      button.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(window.location.href);
          button.textContent = '链接已复制';
        } catch {
          button.textContent = window.location.href;
        }
      });
    }
  });
})();
