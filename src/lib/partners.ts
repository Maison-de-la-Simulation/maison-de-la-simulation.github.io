import partners from '../data/partners.json';
const escape = (text: string) =>
  text
    .replaceAll('&', '&amp;')
    .replaceAll('"', '&quot;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
export function renderPartners() {
  const base = import.meta.env.BASE_URL;
  return (
    '<div class="partner-grid" aria-label="Scientific partners">' +
    partners
      .map(
        (partner) =>
          '<a class="partner-logo-card" data-partner="' +
          escape(partner.id) +
          '" href="' +
          escape(partner.url) +
          '"><div><img src="' +
          base +
          escape(partner.image) +
          '" alt="' +
          escape(partner.name) +
          ' official logo" loading="lazy"/></div><span>' +
          escape(partner.name) +
          ' <span aria-hidden="true">↗</span></span></a>',
      )
      .join('') +
    '</div>'
  );
}
