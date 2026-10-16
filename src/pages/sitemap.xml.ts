import { content } from '../lib/content';
export function GET({site}: {site:URL}) {
 const base=import.meta.env.BASE_URL;
 const paths=new Set([...content.map(p=>p.path),'/', '/recherche/', '/logiciels/', '/laboratoire/','/actualites/','/contact/','/formations/','/sources/','/recherche-site/','/plan-du-site/','/laboratory/','/training/','/software/','/news/','/search/','/site-map/','/credits/']);
 const xml='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+[...paths].map(path=>'<url><loc>'+new URL(base+path.replace(/^\//,''),site).href.replaceAll('&','&amp;')+'</loc></url>').join('')+'</urlset>';
 return new Response(xml,{headers:{'Content-Type':'application/xml; charset=utf-8'}});
}
