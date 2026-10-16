import { defineConfig } from 'astro/config';
// Local: SITE_URL=https://organisation.github.io BASE_PATH=/nom-du-depot npm run build
export default defineConfig({
  site: process.env.SITE_URL || 'https://maison-de-la-simulation.github.io',
  base: process.env.BASE_PATH || '/',
  output: 'static',
  trailingSlash: 'always',
});
