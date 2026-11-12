import { defineConfig } from 'astro/config';
// Local: SITE_URL=https://organisation.github.io BASE_PATH=/nom-du-depot npm run build
const base = process.env.BASE_PATH || '/';

export default defineConfig({
  site: process.env.SITE_URL || 'https://maison-de-la-simulation.github.io',
  base,
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/tiledviz-2/': `${base.replace(/\/+$/, '')}/hive-sa/`,
  },
});
