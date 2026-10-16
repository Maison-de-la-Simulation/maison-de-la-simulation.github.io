import people from '../data/members.json';
import directory from '../data/member-groups.json';
import { escapeHtml } from './paths';

export type Member = {
  id: string;
  name: string;
  group: string;
  role?: string;
  badge?: string;
  image?: string;
  url?: string;
  anchor?: string;
  initials?: string;
};

export type MemberGroup = {
  id: string;
  anchor: string;
  title: string;
  url?: string;
  category?: string;
  location?: string;
  emptyText?: string;
};

export type MemberSection = {
  id: string;
  title: string;
  layout: 'leadership' | 'groups' | 'compact';
  groups: MemberGroup[];
};

export const directoryConfig = directory as {
  sections: MemberSection[];
  photo: {
    image: string;
    alt: string;
    width: number;
    height: number;
    caption: string;
  };
};

export const members = people as Member[];
const memberIds = new Map<string, string>();
const groupDetails = new Map(
  directoryConfig.sections.flatMap((section) =>
    section.groups.map((group) => [group.id, { section, group }] as const),
  ),
);

for (const member of members) {
  if (!member.name?.trim() || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(member.id)) {
    throw new Error(`Invalid name or id in src/data/members.json: ${JSON.stringify(member)}`);
  }
  if (!groupDetails.has(member.group)) {
    throw new Error(
      `Unknown group "${member.group}" for ${member.name}. Check src/data/member-groups.json.`,
    );
  }
  const existingName = memberIds.get(member.id);
  if (existingName && existingName !== member.name) {
    throw new Error(
      `The member id "${member.id}" is used by both ${existingName} and ${member.name}.`,
    );
  }
  memberIds.set(member.id, member.name);
}

export function membersInGroup(group: string): Member[] {
  return members.filter((member) => member.group === group);
}

export function memberUrl(member: Member): string {
  return member.url || `/member/${member.id}/`;
}

export function memberInitials(member: Member): string {
  const words = member.name.trim().split(/\s+/);
  return member.initials || words[0][0] + words[words.length - 1][0];
}

export function memberSearchText(member: Member): string {
  const { group, section } = groupDetails.get(member.group)!;
  return [
    member.name,
    member.role,
    group.title !== section.title ? group.title : '',
    section.title,
    member.badge,
    member.group === 'alumni' ? 'Alumni' : '',
  ]
    .filter(Boolean)
    .join(' ');
}

/** New directory entries get a local profile unless a custom URL is supplied. */
export function createMemberProfiles(existingPaths: Set<string>) {
  const seen = new Set(existingPaths);
  return members.flatMap((member) => {
    const path = `/member/${member.id}/`;
    if (seen.has(path) || (member.url && member.url !== path)) return [];
    seen.add(path);

    const { group, section } = groupDetails.get(member.group)!;
    const isFormer = member.group === 'alumni';
    const isTeam = ['sbc', 'soc', 'coordination'].includes(member.group);
    const classes = ['member', 'type-member', 'status-publish'];
    if (group.location) classes.push(`member_location-${group.location}`);
    if (group.category) classes.push(`member_category-${group.category}`);

    const details = [
      `<p><strong>Status:</strong> ${escapeHtml(section.title)}.</p>`,
      group.title !== section.title
        ? `<p><strong>${isTeam ? 'Team' : 'Group'}:</strong> ${escapeHtml(group.title)}.</p>`
        : '',
      member.role
        ? `<p><strong>${isFormer ? 'Role at the laboratory' : 'Role'}:</strong> ${escapeHtml(member.role)}.</p>`
        : '',
    ].join('');

    const html =
      '<div class="entry-content"><h2>At Maison de la Simulation</h2>' +
      details +
      `<p><a href="__BASE__members/#${escapeHtml(group.anchor)}">View this group in the directory →</a></p></div>`;

    return [{ path, title: member.name, kind: 'member', classes, html }];
  });
}
