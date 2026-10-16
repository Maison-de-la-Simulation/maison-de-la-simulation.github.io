/** Prefix local links with the GitHub Pages base path. */
export function href(path: string): string {
  return import.meta.env.BASE_URL + path.replace(/^\//, '');
}

export function localize(html: string): string {
  return html.replaceAll('__BASE__', import.meta.env.BASE_URL);
}

export function escapeHtml(value: string): string {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}
