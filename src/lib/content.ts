import pages from '../data/pages.json';
import translations from '../data/translations.en.json';
import editorial from '../data/editorial.json';
import memberProfiles from '../data/member-profiles.json';
import publication from '../data/publication.json';
type Override = { title?: string; intro?: string; html?: string; text?: string; toc?: {id:string,title:string}[]; originalHtml?: string; originalLabel?: string; showOriginal?: boolean; eventDate?: string; label?: string };
const edits=editorial as Record<string,Override>;
const english=translations as Record<string,Override>;
const roles:Record<string,string>={'alumni':'Alumni','assistante-de-direction':'Executive assistants','associate-professor':'Associate professors','deputy-director':'Deputy directors','director':'Directors','engineer':'Engineers','intern':'Interns','member':'Members','phd':'PhD students','postdoc':'Postdoctoral researchers','professor':'Professors','project-manager':'Project managers','research-director':'Research directors','research-engineer':'Research engineers','membres':'Members','post-doc':'Postdoctoral researchers','phd-students':'PhD students','executive-assistant':'Executive assistants'};
export const content=[...pages,...memberProfiles].filter(source=>!publication.excluded_kinds.includes(source.kind)&&!publication.excluded_paths.includes(source.path)).map(source=>{
 const translated=english[source.path]||{};
 const edit=edits[source.path]||{};
 const page={...source,...translated,...edit};
 let title=edit.title||source.title;
 if(page.kind==='archive'&&!edit.title){
  const key=page.path.split('/').filter(Boolean).at(-1)||'';
  if(page.path.startsWith('/member_'))title=roles[key]||'Directory';
  else if(page.path==='/member/')title='Member profiles';
  else if(page.path==='/glossary/'||page.path.startsWith('/tooltips_categories/'))title='Portraits';
  else if(page.path.startsWith('/category/'))title=({'job':'Vacancies','thesis':'PhD positions','member':'Members','non-classe':'Other publications','seminar':'Seminars','seminaire-futur':'Upcoming seminars','seminaire-passe':'Past seminars'} as Record<string,string>)[key]||'Archives';
 }
 return {...page,title,isEditorial:Boolean(edit.html),intro:edit.intro||'',text:page.text||'',searchText:(page.text||'')+' '+(edit.intro||''),originalHtml:edit.originalHtml||'',originalLabel:edit.originalLabel||'Additional information',showOriginal:edit.showOriginal!==false,eventDate:edit.eventDate||'',label:edit.label||''};
});
export const getPage=(path:string)=>content.find(page=>page.path===path);
export const localize=(html:string)=>html.replaceAll('__BASE__',import.meta.env.BASE_URL);
export const href=(path:string)=>import.meta.env.BASE_URL+path.replace(/^\//,'');
