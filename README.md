# Modifier le site Maison de la Simulation

Le contenu est réparti dans des fichiers lisibles. Les textes des pages sont en Markdown ;
l’annuaire, les logiciels et les partenaires utilisent des données JSON. Les composants Astro
s’occupent de l’affichage.

## Où modifier quoi ?

| Modification                                                              | Fichier                                     |
| ------------------------------------------------------------------------- | ------------------------------------------- |
| Ajouter une personne, modifier son nom, sa fonction, sa photo ou son lien | `src/data/members.json`                     |
| Renommer ou ajouter un groupe, modifier la photo d’équipe                 | `src/data/member-groups.json`               |
| Titre et introduction de Members                                          | `src/content/pages/members.md`              |
| Présentation du laboratoire                                               | `src/content/pages/laboratory.md`           |
| Research / Science of Computing                                           | `src/content/pages/science-of-computing.md` |
| Expertise / Science by Computing                                          | `src/content/pages/science-by-computing.md` |
| Formations et cartes universitaires                                       | `src/content/pages/training.md`             |
| Accès au laboratoire                                                      | `src/content/pages/visit.md`                |
| Recrutement                                                               | `src/content/pages/jobs.md`                 |
| Workshop sur l’IA agentique                                               | `src/content/events/agentic-ai-workshop.md` |
| Choisir ou masquer l’événement Featured de l’accueil                      | `src/data/featured.json`                    |
| Autres textes et blocs de l’accueil                                       | `src/pages/index.astro`                     |
| Biographies personnelles existantes                                       | `src/content/profiles/`                     |
| Portraits historiques                                                     | `src/content/portraits/`                    |
| Cartes des logiciels                                                      | `src/data/software.json`                    |
| Partenaires, liens et logos                                               | `src/data/partners.json`                    |
| Logos des tutelles                                                        | `src/data/tutelles.json`                    |
| Menu et pied de page                                                      | `src/layouts/Base.astro`                    |
| Couleurs, tailles et mise en page                                         | `src/styles/global.css`                     |

Les anciens fichiers `editorial.json`, `pages.json`, `translations.en.json` et
`member-profiles.json` sont conservés dans `migration/legacy-content/` comme archives. Les
modifications du site se font dans les fichiers indiqués ci-dessus.

## Ajouter un membre

Ouvrir `src/data/members.json` et ajouter un objet dans le tableau, à l’endroit où la carte doit
apparaître dans son groupe :

```json
{
  "id": "prenom-nom",
  "name": "Prénom NOM",
  "group": "soc",
  "role": "Research engineer"
}
```

Mettre une virgule entre deux objets du tableau. Le dernier objet n’a pas de virgule après lui. Les
noms de champs et les chaînes JSON utilisent des guillemets doubles.

- `id` : identifiant unique, en minuscules, sans accent ni espace, avec des tirets si nécessaire. Le
  conserver quand le nom affiché change pour garder la même adresse de fiche.
- `name` : nom tel qu’il doit apparaître sur la carte.
- `group` : groupe choisi dans le tableau ci-dessous.
- `role` : fonction affichée ; ce champ est facultatif.

Une nouvelle carte apparaît au prochain build. Les compteurs, les initiales, le texte utilisé par la
recherche et le lien vers `/member/prenom-nom/` sont calculés automatiquement. Une fiche locale est
créée à partir du groupe et de la fonction lorsqu’il n’existe pas déjà de biographie.

### Groupes disponibles

| Valeur de `group` | Emplacement                          |
| ----------------- | ------------------------------------ |
| `leadership`      | Direction et assistance de direction |
| `sbc`             | Permanents — Science by Computing    |
| `soc`             | Permanents — Science of Computing    |
| `coordination`    | Permanents — Coordination team       |
| `external`        | Collaborateurs extérieurs            |
| `postdocs`        | Contrats temporaires — Postdocs      |
| `engineers`       | Contrats temporaires — Engineers     |
| `fixed-term`      | Autres CDD                           |
| `phd`             | Doctorants                           |
| `trainees`        | Stagiaires                           |
| `alumni`          | Anciens membres                      |

Changer `group` déplace la carte. Par exemple, passer à `"group": "alumni"` la place parmi les
anciens membres. L’ordre des objets dans `members.json` détermine l’ordre des cartes dans chaque
groupe. Les groupes et leur ordre sont définis dans `member-groups.json`.

### Photo, page personnelle et badge

Ajouter les champs facultatifs utiles :

```json
{
  "id": "prenom-nom",
  "name": "Prénom NOM",
  "group": "sbc",
  "role": "Research engineer",
  "image": "media/prenom-nom.jpg",
  "url": "https://exemple.fr/page-personnelle/",
  "badge": "Team leader"
}
```

Pour la photo, déposer le fichier dans `public/media/prenom-nom.jpg`. Dans le JSON, utiliser
`media/prenom-nom.jpg`, sans `public/`. Sans photo, les initiales sont affichées.

Sans `url`, la carte renvoie vers la fiche locale automatique. Avec `url`, elle renvoie vers
l’adresse indiquée : une URL `https://...` ou un chemin interne comme `/member/prenom-nom/`. Le
badge est facultatif ; utiliser par exemple `Team leader` pour un responsable.

Les champs `anchor` et `initials` présents sur certaines anciennes entrées servent respectivement
aux liens directs existants et à des initiales particulières. Ils sont facultatifs.

### Rédiger une biographie

Pour personnaliser une fiche automatique, créer `src/content/profiles/prenom-nom.md` :

```markdown
---
path: '/member/prenom-nom/'
title: 'Prénom NOM'
kind: 'member'
---

## Activities

Description des activités, en anglais pour le site public.

[Personal website](https://exemple.fr/)
```

Cette fiche prend la place de la fiche automatique. Les fichiers existants dans
`src/content/profiles/` peuvent être modifiés directement. Pour une personne qui a déjà une
biographie rédigée, mettre aussi son texte à jour si sa fonction ou sa situation change.

## Modifier un texte

Ouvrir le fichier `.md` de la page. Le bloc entre les deux lignes `---` contient le titre,
l’introduction et les réglages. Le texte de la page se trouve juste après :

```markdown
---
path: '/my-page/'
title: 'Page title'
intro: 'A short introduction.'
---

## Section title

A paragraph with **important words** and a [link](https://exemple.fr/).

- First item
- Second item
```

Une ligne vide sépare deux paragraphes. `##` crée un titre de section, `###` un sous-titre. Les
résumés utilisés par la recherche sont extraits automatiquement du contenu : aucun champ `text` ni
champ `data-search` n’est à recopier.

### Liens et images

Dans un fichier Markdown, préfixer les liens internes et les médias locaux avec `__BASE__` pour que
le site fonctionne aussi dans un sous-dossier GitHub Pages :

```markdown
[Members](__BASE__members/)

[Contact](__BASE__contact/#contact-form)

<img src="__BASE__media/illustration.png" alt="Description of the illustration" />
```

Les liens externes gardent leur URL complète. Dans `members.json`, les URL internes commencent
simplement par `/` ; dans les champs `image` des fichiers de données, utiliser le chemin depuis
`public/`, par exemple `media/photo.jpg`.

## Ajouter une section à une page

Copier ce bloc dans la page Markdown, après une autre section :

```markdown
<section class="editorial-section" id="new-topic">

## New topic

Description of this topic.

[Project website](https://exemple.fr/)

</section>
```

Conserver une ligne vide après la balise d’ouverture et avant la fermeture pour que le texte soit
interprété comme du Markdown. Choisir un `id` unique sur la page.

Quand un bloc `toc:` est présent en tête du fichier, ajouter une entrée si la nouvelle section doit
apparaître dans le sommaire :

```yaml
- id: 'new-topic'
  title: 'New topic'
```

Si un titre de section change, modifier aussi son `title` dans le bloc `toc` existant.

Sans bloc `toc`, le sommaire se construit à partir des titres Markdown de niveau 2. Il apparaît
quand il contient plus de deux entrées.

## Ajouter une carte

Les pages conservent quelques blocs HTML pour leurs grilles, logos et illustrations. Dans une grille
`editorial-cards`, ajouter un bloc `article` :

```html
<div class="editorial-cards">
  <article>
    <h3>New project</h3>
    <p>Description of the project.</p>
    <a href="https://exemple.fr/">Project details →</a>
  </article>
</div>
```

Si la grille existe déjà, copier seulement le bloc `<article>...</article>` dedans. Pour une
formation universitaire, copier une carte `university-card` dans `training.md`, puis modifier son
titre, son établissement, sa description et son lien. Donner un `data-programme` différent à chaque
carte.

Les cartes des logiciels et des partenaires viennent de leurs fichiers JSON : copier un objet de
`software.json` ou `partners.json` et modifier ses champs. Déposer le logo correspondant dans
`public/` et utiliser son chemin relatif dans `image`.

## Ajouter une page

Créer un fichier comme `src/content/pages/my-project.md` avec l’exemple de métadonnées et de texte
ci-dessus. Le champ `path` définit l’adresse ; il doit commencer et finir par `/` et être unique. Le
nom du fichier peut être différent de l’adresse publique.

La page apparaît automatiquement dans la recherche et les plans du site après compilation. Pour la
rendre accessible depuis une page existante, ajouter un lien :

```markdown
[My project](__BASE__my-page/)
```

Pour un lien dans le menu principal, modifier la liste `nav` dans `src/layouts/Base.astro`.

## Modifier l’événement Featured

Le contenu du workshop actuel se trouve dans `src/content/events/agentic-ai-workshop.md`. Modifier
`title` ou `eventDate` actualise aussi le titre et la date du bandeau de l’accueil. Utiliser une
date ISO entre guillemets, par exemple `eventDate: '2026-12-03'`.

`src/data/featured.json` choisit la page mise en avant et le libellé du bandeau. Mettre
`"enabled": false` masque le bloc Featured. Pour un autre événement, créer sa page Markdown et
indiquer son `path` dans ce fichier.

Les anciennes annonces et la rubrique séminaires restent filtrées par `src/data/publication.json`.
Pour un nouvel événement ordinaire, utiliser `kind: 'page'` et `label: 'Scientific workshop'` ; le
champ `eventDate` reste disponible. Le workshop historique sur l’IA agentique est l’exception
explicitement conservée dans `included_paths`.

## Mettre en forme et vérifier

```bash
npm ci
npm run format
npm run format:check
npm run build
npm run dev
```

`format` remet en forme les sources Astro, TypeScript, CSS, JSON et Markdown. Les snapshots
historiques et les médias sont exclus. `build` signale notamment une adresse en double, un
identifiant de membre incorrect ou un groupe inconnu. `dev` lance la prévisualisation locale.

Pour les contrôles des liens et du contenu, après le build :

```bash
python3 -m pip install beautifulsoup4
python3 scripts/audit-site.py
python3 scripts/verify-editorial.py
```

Après modification, committer les fichiers concernés, ainsi que `package-lock.json` si des
dépendances ont changé. Le workflow GitHub Pages existant se charge de la publication.
