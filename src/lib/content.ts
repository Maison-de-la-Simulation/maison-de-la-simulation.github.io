import type { MarkdownInstance } from 'astro';
import { decodeHTML } from 'entities';
import archiveRoutes from '../data/archive-routes.json';
import publication from '../data/publication.json';
import { createMemberProfiles, members, memberSearchText } from './members';

export { href, localize } from './paths';

type Heading = { id: string; title: string };

type PageMetadata = {
  path: string;
  title: string;
  kind?: string;
  intro?: string;
  editorial?: boolean;
  classes?: string[];
  toc?: Heading[];
  eventDate?: string;
  label?: string;
};

export type Page = {
  path: string;
  title: string;
  kind: string;
  intro: string;
  html: string;
  text: string;
  searchText: string;
  classes: string[];
  toc: Heading[];
  eventDate: string;
  label: string;
  isEditorial: boolean;
};

function plainText(html: string): string {
  return decodeHTML(
    html.replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1>/gi, ' ').replace(/<[^>]*>/g, ' '),
  )
    .replace(/\s+/g, ' ')
    .trim();
}

function makePage(meta: PageMetadata, html = ''): Page {
  if (!meta.path?.startsWith('/') || !meta.path.endsWith('/') || !meta.title?.trim()) {
    throw new Error(
      `Each Markdown page needs a title and a path such as /my-page/: ${JSON.stringify(meta)}`,
    );
  }

  const text =
    meta.kind === 'directory' ? members.map(memberSearchText).join(' ') : plainText(html);
  const intro = meta.intro || '';

  return {
    path: meta.path,
    title: meta.title,
    kind: meta.kind || 'page',
    intro,
    html,
    text,
    searchText: `${text} ${intro}`,
    classes: meta.classes || [],
    toc: meta.toc || [],
    eventDate: meta.eventDate || '',
    label: meta.label || '',
    isEditorial: meta.editorial ?? true,
  };
}

const files = import.meta.glob<MarkdownInstance<PageMetadata>>('../content/**/*.md', {
  eager: true,
});

const markdownPages = await Promise.all(
  Object.values(files).map(async (file) =>
    makePage(
      {
        ...file.frontmatter,
        toc:
          file.frontmatter.toc ??
          file
            .getHeadings()
            .filter((heading) => heading.depth === 2)
            .map((heading) => ({ id: heading.slug, title: heading.text })),
      },
      await file.compiledContent(),
    ),
  ),
);

const archives = archiveRoutes.map((route) => {
  const shared = route.contentFrom
    ? markdownPages.find((page) => page.path === route.contentFrom)
    : undefined;
  if (route.contentFrom && !shared) {
    throw new Error(`Missing shared page ${route.contentFrom} for ${route.path}`);
  }
  return shared
    ? { ...shared, path: route.path, title: route.title, kind: 'archive' }
    : makePage({ ...route, kind: 'archive', editorial: false });
});

const sourcePages = [...markdownPages, ...archives];
const paths = new Set<string>();
for (const page of sourcePages) {
  if (paths.has(page.path)) throw new Error(`Two content files use the same path: ${page.path}`);
  paths.add(page.path);
}

const memberProfiles = createMemberProfiles(paths).map((profile) =>
  makePage({ ...profile, editorial: false }, profile.html),
);

/** Only the featured workshop is retained from the former seminar section. */
function isPublished(page: Page): boolean {
  return (
    publication.included_paths.includes(page.path) ||
    (!publication.excluded_kinds.includes(page.kind) &&
      !publication.excluded_paths.includes(page.path))
  );
}

export const content = [
  ...sourcePages.sort((a, b) => (a.path < b.path ? -1 : a.path > b.path ? 1 : 0)),
  ...memberProfiles,
].filter(isPublished);

export function getPage(path: string): Page | undefined {
  return content.find((page) => page.path === path);
}
