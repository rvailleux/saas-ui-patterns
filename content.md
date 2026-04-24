# SaaS UI Design Patterns — Guide de référence

> Un guide pratique pour designers produit et développeurs front-end.  
> Chaque pattern est présenté avec sa démonstration, ses meilleurs exemples, et un guide d'implémentation.

---

## Comment utiliser ce guide

Chaque fiche suit la même structure :

- **Ce que c'est** — définition du pattern en une phrase
- **Pourquoi ça marche** — la logique UX derrière
- **Démo** — illustration textuelle du comportement
- **Meilleurs exemples** — références réelles
- **Guide d'implémentation** — ce qu'il faut faire
- **Pièges à éviter** — les erreurs fréquentes

---

## Sommaire

### Navigation & Structure
1. [Sidebar collapsible icon-rail](#1-sidebar-collapsible-icon-rail)
2. [Top nav + contextual left panel](#2-top-nav--contextual-left-panel)
3. [Breadcrumb dynamique](#3-breadcrumb-dynamique)
4. [Tabs persistants / pinnable](#4-tabs-persistants--pinnable)

### Layout & Workspace
5. [Right panel contextuel (détail)](#5-right-panel-contextuel-détail)
6. [Split view / panneau dual](#6-split-view--panneau-dual)
7. [Floating Action Button (FAB)](#7-floating-action-button-fab)
8. [Board & vue switcher](#8-board--vue-switcher)

### Commandes & Recherche
9. [Command palette (⌘K)](#9-command-palette-k)
10. [Omnibox / unified search](#10-omnibox--unified-search)
11. [Inline slash commands](#11-inline-slash-commands)
12. [Contextual right-click menu](#12-contextual-right-click-menu)

### Data & Tables
13. [Spreadsheet-like inline editing](#13-spreadsheet-like-inline-editing)
14. [Filtres persistants & URL-encodés](#14-filtres-persistants--url-encodés)
15. [Virtual scrolling](#15-virtual-scrolling)
16. [Column resizing & reordering](#16-column-resizing--reordering)

### Feedback & États
17. [Toast notification + undo](#17-toast-notification--undo)
18. [Optimistic UI](#18-optimistic-ui)
19. [Empty states actionnables](#19-empty-states-actionnables)
20. [Skeleton screens](#20-skeleton-screens)

### AI — Accès & Invocation
21. [AI sidebar persistante](#21-ai-sidebar-persistante)
22. [⌘K → AI intent](#22-k--ai-intent)
23. [Floating AI button contextuel](#23-floating-ai-button-contextuel)
24. [Inline slash AI commands](#24-inline-slash-ai-commands)

### AI — Génération & Édition
25. [Streaming text (typewriter)](#25-streaming-text-typewriter)
26. [Diff view accept/reject](#26-diff-view-acceptreject)
27. [Ghost text / inline autocomplete](#27-ghost-text--inline-autocomplete)
28. [Canvas / artifact panel](#28-canvas--artifact-panel)

### AI — Contexte & Mémoire
29. [@-mentions pour le contexte](#29--mentions-pour-le-contexte)
30. [Fil de conversation persistant](#30-fil-de-conversation-persistant)
31. [Memory / préférences utilisateur](#31-memory--préférences-utilisateur)
32. [Sources citées / grounding](#32-sources-citées--grounding)

### AI — Feedback & Contrôle
33. [Thinking / reasoning visible](#33-thinking--reasoning-visible)
34. [Regenerate + variantes](#34-regenerate--variantes)
35. [Agentic step tracker](#35-agentic-step-tracker)
36. [Confidence / uncertainty signal](#36-confidence--uncertainty-signal)

### AI — Prompt UX
37. [Suggested prompts / quick actions](#37-suggested-prompts--quick-actions)
38. [Prompt templates](#38-prompt-templates)
39. [Multimodal drop zone](#39-multimodal-drop-zone)
40. [Mode voix natif](#40-mode-voix-natif)

---

---

# Navigation & Structure

---

## 1. Sidebar collapsible icon-rail

**Ce que c'est** — La sidebar de navigation se réduit à une colonne d'icônes lorsqu'elle est fermée. Au survol ou au clic sur une icône, le label et les sous-éléments réapparaissent.

**Pourquoi ça marche**  
L'espace de travail est le bien le plus précieux d'une interface. La sidebar réduite libère de la largeur pour le contenu tout en maintenant la navigation accessible à tout moment. Les icônes seules suffisent aux utilisateurs réguliers ; les labels restent disponibles pour les nouveaux. C'est le meilleur compromis entre affordance et densité.

**Démo**

```
État ouvert (240px)          État réduit (48px)
┌──────────────────┐         ┌────┐
│ 📁  Projets      │         │ 📁 │
│ 📋  Tâches       │  ───►   │ 📋 │
│ 📊  Rapports     │         │ 📊 │
│ ⚙️  Paramètres   │         │ ⚙️ │
└──────────────────┘         └────┘
                               ▲
                         Hover → tooltip "Projets"
                         ou flyout avec sous-menu
```

**Meilleurs exemples**
- **Obsidian** — transition fluide, état mémorisé par vault
- **Linear** — icône rail avec flyout de sous-navigation au hover
- **Jira** — collapse partiel (icônes) + collapse total (rail invisible)
- **VS Code** — référence fondatrice du pattern dans les IDEs
- **SharePoint** — implémentation enterprise avec états persistants par user

**Guide d'implémentation**

1. **Largeur** : ouverte entre 200–260px, réduite entre 40–56px. Ne pas descendre sous 40px (zone de clic trop petite).
2. **Transition** : `transition: width 200ms ease-in-out` suffit. Éviter les animations de contenu (opacité des labels séparément) qui retardent l'affichage.
3. **État persistant** : sauvegarder l'état (ouvert/fermé) en `localStorage` ou côté serveur par utilisateur. Ne jamais reset à chaque visite.
4. **Tooltip** : en état réduit, un tooltip au hover est obligatoire — `title` HTML ou composant dédié avec delay de 300ms.
5. **Sous-navigation** : en état réduit, les sections avec sous-menus s'ouvrent en flyout (panneau flottant ancré sur l'icône), pas en accordion.
6. **Breakpoints** : sur mobile, la sidebar devient un drawer (overlay) plutôt qu'un icon-rail — le rail est un pattern desktop uniquement.

**Pièges à éviter**

- ❌ Masquer les icônes en état réduit — les icônes sont l'élément navigable, pas les labels
- ❌ Oublier le focus clavier — Tab doit traverser les icônes avec un outline visible
- ❌ Icônes trop génériques (étoile, point) qui perdent leur sens sans label — choisir des icônes sémantiquement fortes
- ❌ Déclencher le collapse au hover (sans clic) — crée des fermetures involontaires lors des déplacements de souris
- ❌ Animer width ET opacity en même temps — la surcharge d'animation perturbe la lecture

---

## 2. Top nav + contextual left panel

**Ce que c'est** — Une barre de navigation horizontale fixe en haut gère la navigation globale (entre grandes sections), tandis qu'un panneau gauche contextuel affiche la navigation secondaire propre à la section active.

**Pourquoi ça marche**  
Sépare clairement les deux niveaux hiérarchiques de navigation. Le top nav reste stable (ancrage cognitif), le left panel change selon le contexte sans perturber l'orientation de l'utilisateur. Particulièrement adapté aux applications avec des domaines fonctionnels très différents (ex : code vs issues vs settings dans GitHub).

**Démo**

```
┌─────────────────────────────────────────────┐
│  Logo  |  Code  |  Issues  |  Actions  |  ▼ │  ← Top nav (fixe)
├─────────┬───────────────────────────────────┤
│ Issues  │                                   │
│ ──────  │   #1234 Fix login bug             │
│ Open    │   ─────────────────────────────   │
│ Closed  │   Labels · Assignees · Milestone  │
│ Labels  │                                   │
│ Milest. │                                   │  ← Left panel contextuel
└─────────┴───────────────────────────────────┘
   ▲
   Change quand on clique sur "Actions" dans le top nav
```

**Meilleurs exemples**
- **GitHub** — référence absolue, top nav + left panel parfaitement coordonnés
- **Figma** — top nav (fichiers/équipes) + left panel (pages/layers) selon le contexte
- **GitLab** — déclinaison plus dense avec icônes dans le left panel
- **Salesforce** — enterprise avec top nav configurable par admin

**Guide d'implémentation**

1. **Hiérarchie stricte** : top nav = sections globales (max 6–8 items), left panel = navigation interne à la section. Ne pas mélanger les deux niveaux.
2. **Hauteur du top nav** : 48–64px. En dessous, les zones de clic sont trop petites sur desktop avec une souris imprécise.
3. **Indicateur actif** : dans le top nav, l'item actif doit être visuellement distinct (underline, background, couleur). Dans le left panel, un highlight de fond suffit.
4. **Left panel width** : 200–240px fixe. Éviter le redimensionnable sauf si c'est une feature explicite (ex : explorateur de fichiers).
5. **Scroll indépendant** : le left panel doit scroller indépendamment du contenu principal (`overflow-y: auto` sur le panel).

**Pièges à éviter**

- ❌ Trop d'items dans le top nav — au-delà de 7–8, utiliser un menu "Plus" ou revoir l'architecture IA
- ❌ Left panel qui disparaît ou change lors du scroll — il doit rester `position: sticky`
- ❌ Doublon de navigation entre top nav et left panel pour le même niveau
- ❌ Left panel sans état actif clairement visible — l'utilisateur perd son orientation

---

## 3. Breadcrumb dynamique

**Ce que c'est** — Un fil d'Ariane mis à jour en temps réel qui reflète la position exacte de l'utilisateur dans la hiérarchie, avec des segments interactifs (clic, sous-menu au hover).

**Pourquoi ça marche**  
Dans les applications avec une hiérarchie profonde (espace de travail > projet > dossier > document), le breadcrumb est le seul moyen de maintenir l'orientation sans occuper d'espace permanent. Le rendre cliquable et avec des sous-menus transforme un indicateur passif en outil de navigation rapide.

**Démo**

```
Acme Corp  ›  Produit  ›  Q4 2025  ›  Sprint 12
    ▲              ▲
    Clic → retour  Hover → dropdown des autres projets
    à l'accueil    ┌──────────────────┐
                   │ ✓ Produit        │
                   │   Marketing      │
                   │   Engineering    │
                   │ + Nouveau projet │
                   └──────────────────┘
```

**Meilleurs exemples**
- **Notion** — breadcrumb avec hover dropdown sur chaque segment, éditable inline
- **Confluence** — breadcrumb avec espaces, sections, pages imbriquées
- **AWS Console** — breadcrumb technique avec ARN raccourci, essentiel pour naviguer entre resources
- **Figma** — breadcrumb de fichier dans la top bar, clic = retour au project

**Guide d'implémentation**

1. **Troncature** : sur les chemins longs, tronquer les segments du milieu avec `…` cliquable qui révèle le chemin complet. Toujours afficher le premier et le dernier segment.
2. **Dernier segment** : le segment actuel (dernier) ne doit pas être un lien — c'est là où on est. Le styliser différemment (plus sombre, non souligné).
3. **Hover dropdown** : délai de 150ms avant ouverture pour éviter les ouvertures accidentelles. Max 8–10 items, avec scroll si plus.
4. **URL** : chaque segment doit correspondre à une URL propre et partageable.
5. **Accessibilité** : wrapper dans `<nav aria-label="Breadcrumb">` + `<ol>` avec `aria-current="page"` sur le dernier item.

**Pièges à éviter**

- ❌ Breadcrumb qui ne reflète pas l'URL réelle — crée une désorientation totale
- ❌ Trop de niveaux sans troncature (6+ segments) — illisible
- ❌ Breadcrumb statique non interactif — perd 80% de sa valeur
- ❌ Séparateur `>` sans espace — `›` ou `/` avec padding est plus lisible

---

## 4. Tabs persistants / pinnable

**Ce que c'est** — Des onglets dans l'espace de travail qui persistent entre sessions, peuvent être réorganisés, épinglés ou fermés — inspirés des onglets de navigateur ou d'IDE.

**Pourquoi ça marche**  
Les utilisateurs avancés travaillent simultanément sur plusieurs contextes. Les tabs persistants éliminent le coût cognitif de retrouver et rouvrir les mêmes éléments à chaque session. L'épinglage signale l'importance sans encombrer.

**Démo**

```
┌──────────┬────────────┬──────────────┬───┐
│ 📌 Home  │ #1234 Bug  │ Sprint Plan  │ + │
└──────────┴────────────┴──────────────┴───┘
    ▲              ▲
    Épinglé,     Clic droit → Pin / Close /
    non fermable  Close others / Close all
```

**Meilleurs exemples**
- **VS Code** — référence : tabs dot (non sauvegardé), preview tab en italique
- **Linear** — tabs par vue dans un projet, mémorisés
- **Penpot** — tabs de pages dans un fichier de design
- **Zed** — tabs avec preview mode (italique) avant édition réelle

**Guide d'implémentation**

1. **Preview tab** : ouvrir un item en "preview" (italique) par défaut. Il devient un vrai tab dès que l'utilisateur l'édite ou double-clique. Évite la prolifération de tabs.
2. **Dot indicateur** : afficher un point sur le tab si des modifications non sauvegardées existent.
3. **Overflow** : quand les tabs dépassent la largeur, utiliser un scroll horizontal ou un dropdown `+N autres` — ne jamais tronquer le titre sans indicateur.
4. **Clic droit** : menu contextuel avec au minimum : Épingler / Fermer / Fermer les autres.
5. **Drag & drop** : réorganisation par drag est attendue — utiliser une lib type `dnd-kit` ou équivalent.
6. **Persistance** : sauvegarder l'ordre et l'état épinglé côté serveur, pas seulement localStorage.

**Pièges à éviter**

- ❌ Tabs qui se ferment sans confirmation quand des modifications existent
- ❌ Plus de 8–10 tabs ouverts sans overflow géré — l'UI s'effondre
- ❌ Tabs identiques (même titre) sans différenciateur (chemin, icône)
- ❌ Oublier le raccourci `Ctrl+W` / `Cmd+W` pour fermer le tab actif

---

---

# Layout & Workspace

---

## 5. Right panel contextuel (détail)

**Ce que c'est** — Un panneau qui s'ouvre sur la droite de l'interface lorsque l'utilisateur sélectionne un élément dans une liste ou un board, affichant le détail et les actions sans changer de page.

**Pourquoi ça marche**  
Évite le coût de navigation aller-retour (liste → détail → retour à la liste). L'utilisateur garde le contexte de la liste tout en accédant aux détails. Particulièrement puissant pour les workflows de triage (issues, tickets, emails).

**Démo**

```
┌─────────────────────┬──────────────────────┐
│ LISTE               │ DÉTAIL               │
│ ──────────────────  │ ──────────────────   │
│ ▶ Bug login #1234   │ Bug login #1234      │
│   Task A            │ ─────────────────    │
│   Task B            │ Assigné : Alice      │
│                     │ Statut : In progress │
│                     │ Description...       │
│                     │ [Edit]  [Close]      │
└─────────────────────┴──────────────────────┘
                        ▲
              S'ouvre au clic sur un item,
              se ferme avec Échap ou X
```

**Meilleurs exemples**
- **Linear** — right panel avec édition complète inline, largeur ajustable
- **Jira** — "detail view" sur les issues en board et list
- **Asana** — right panel avec sous-tâches, commentaires, pièces jointes
- **HubSpot** — détail de contact/deal sans quitter la liste CRM

**Guide d'implémentation**

1. **Largeur** : 360–480px fixe ou redimensionnable. Fixer un minimum (320px) et un maximum (50% de l'écran).
2. **Animation** : slide-in depuis la droite, `transform: translateX(100%)` → `translateX(0)`, durée 200ms. Éviter les fades purs.
3. **Fermeture** : toujours possible via Échap, clic sur X, et clic en dehors du panneau (ou non — à définir selon le flux).
4. **Item actif** : mettre en évidence l'item sélectionné dans la liste (background, border-left colorée).
5. **URL** : l'ouverture du panneau doit idéalement mettre à jour l'URL (`?item=1234`) pour permettre le partage.
6. **Mobile** : sur mobile, le right panel devient une page entière ou un bottom sheet — jamais un panneau superposé.

**Pièges à éviter**

- ❌ Panneau qui couvre toute la liste sur les écrans < 1280px sans adaptation
- ❌ Pas de raccourci clavier pour naviguer entre items (↑/↓) depuis le panneau
- ❌ Panneau sans scroll interne — le contenu déborde
- ❌ Fermeture involontaire au clic en dehors sans confirmation si des modifications existent

---

## 6. Split view / panneau dual

**Ce que c'est** — Deux zones de travail côte à côte, redimensionnables par une poignée centrale, affichant deux vues du même contenu ou deux contenus différents.

**Pourquoi ça marche**  
Certains workflows nécessitent une comparaison simultanée (markdown source + preview, code + résultat, deux documents). Le split view élimine le alt-tab constant et donne les deux contextes en permanence.

**Démo**

```
┌───────────────────┬─┬───────────────────┐
│ # Mon document    │ │ Mon document       │
│                   │◄►│                  │
│ Voici un **titre**│ │ Voici un **titre** │
│ et du texte.      │ │ et du texte.       │
│                   │ │                   │
└───────────────────┴─┴───────────────────┘
         ▲           ▲
       Source    Poignée    Preview rendu
                drag pour resize
```

**Meilleurs exemples**
- **Notion** — split de pages en colonnes (drag & drop de blocs)
- **GitHub** — split diff (changes side-by-side vs unified)
- **Obsidian** — split de notes, horizontal et vertical, emboîtables
- **Raycast** — split list+preview dans les résultats de recherche

**Guide d'implémentation**

1. **Poignée** : zone de 8px avec curseur `col-resize`. Highlight au hover. Double-clic → reset à 50/50.
2. **Tailles min** : définir `min-width` sur chaque panneau (ex: 240px) pour éviter l'effondrement.
3. **Persistance** : sauvegarder le ratio en localStorage par contexte.
4. **Synchronisation** : si les deux panneaux affichent le même document (source/preview), le scroll peut être synchronisé — avec option pour désactiver.
5. **Collapse** : permettre de réduire un panneau à 0 (= fermer le split) en double-cliquant sur la poignée ou via un bouton.

**Pièges à éviter**

- ❌ Poignée trop fine (< 4px) — difficile à attraper
- ❌ Pas de minimum width — un panneau peut devenir invisible
- ❌ Split imposé sans possibilité de revenir en vue simple
- ❌ Les deux panneaux se scrollent ensemble sans option de désolidariser

---

## 7. Floating Action Button (FAB)

**Ce que c'est** — Un bouton d'action principal flottant, généralement en bas à droite de l'interface, qui déclenche l'action la plus fréquente ou ouvre un menu d'actions rapides.

**Pourquoi ça marche**  
Le FAB matérialise la loi de Fitts : zone de grand bouton, positionnée proche du pouce sur mobile, toujours accessible quel que soit le scroll. Il signale clairement "voilà ce que tu peux faire maintenant".

**Démo**

```
┌────────────────────────────────┐
│                                │
│   Liste de tâches...           │
│                                │
│                                │
│                          ╭───╮ │  ← Hover / tap
│                          │ + │ │     ↓
│                          ╰───╯ │  ╭─────────────╮
└────────────────────────────────┘  │ 📝 Nouvelle  │
                                    │ 📁 Dossier   │
                                    │ 📥 Importer  │
                                    ╰─────────────╯
```

**Meilleurs exemples**
- **Gmail mobile** — FAB compose, s'étend en options au long-press
- **Trello** — FAB contextuel selon la vue (board, timeline)
- **Monday.com** — FAB avec menu radial d'actions

**Guide d'implémentation**

1. **Position** : `position: fixed; bottom: 24px; right: 24px`. Prévoir un offset si une bottom navigation bar est présente.
2. **Taille** : 56px de diamètre (Material Design spec), 48px minimum.
3. **Ombre** : légère, sans être criarde. `box-shadow: 0 4px 12px rgba(0,0,0,0.15)`.
4. **Une seule action principale** : si le FAB ouvre un menu, limiter à 4–5 options max.
5. **Label au hover** : un tooltip ou label étendu (FAB étendu) améliore la découvrabilité.
6. **Masquer au scroll** : sur mobile, masquer le FAB quand l'utilisateur scrolle vers le bas, réafficher quand il remonte.

**Pièges à éviter**

- ❌ FAB qui couvre du contenu important (colonnes de tableau, dernière ligne de liste)
- ❌ Plusieurs FAB sur la même page — un seul par vue
- ❌ Icon ambigu (ex: étoile, cœur) — l'action principale doit être évidente
- ❌ FAB sur desktop sans équivalent dans la navigation principale

---

## 8. Board & vue switcher

**Ce que c'est** — Le même dataset affiché dans plusieurs représentations (board kanban, liste, tableau, calendrier, timeline), switchable via un sélecteur de vue persistant par utilisateur.

**Pourquoi ça marche**  
Différents utilisateurs ont des modèles mentaux différents. Le développeur veut la liste, le PM veut le board, le manager veut la timeline. Proposer plusieurs vues sur les mêmes données évite de dupliquer l'information et permet à chaque profil de travailler avec son paradigme.

**Démo**

```
[Board] [Liste] [Tableau] [Calendrier]   ← Switcher
   ▲
Vue active

Board view:
┌─────────┐  ┌──────────┐  ┌──────────┐
│ To do   │  │ In prog. │  │ Done     │
│ ─────── │  │ ──────── │  │ ──────── │
│ Task A  │  │ Task C   │  │ Task E   │
│ Task B  │  │ Task D   │  │          │
└─────────┘  └──────────┘  └──────────┘
```

**Meilleurs exemples**
- **Linear** — board/list/timeline, switcher en haut, préférence par project
- **Notion** — database views (board, table, gallery, calendar, list, timeline)
- **ClickUp** — 15+ vues, dont Gantt, Workload, Map
- **Airtable** — grid/gallery/kanban/calendar avec configs indépendantes par vue

**Guide d'implémentation**

1. **Persistance** : mémoriser la vue active par section et par utilisateur (pas globalement).
2. **URL** : encoder la vue dans l'URL (`?view=board`) pour le partage.
3. **Filtres indépendants** : chaque vue peut avoir ses propres filtres et groupements — ne pas forcer un filtre global qui casse certaines vues.
4. **Icônes + labels** : le switcher doit avoir icône ET label — les icônes seules ne sont pas suffisamment distinctives (board vs timeline sont souvent confondus).
5. **Transitions** : un fade rapide (100ms) entre les vues évite le flash de contenu.

**Pièges à éviter**

- ❌ Données qui changent selon la vue (ex: certains champs invisibles en board) sans indication
- ❌ Vue par défaut identique pour tous les utilisateurs sans possibilité de changer
- ❌ Drag & drop disponible seulement en board — les autres vues se sentent "dégradées"
- ❌ Trop de vues disponibles (> 6) sans hiérarchie — surcharge de choix

---

---

# Commandes & Recherche

---

## 9. Command palette (⌘K)

**Ce que c'est** — Une palette de commandes universelle, accessible par raccourci clavier, qui permet de déclencher n'importe quelle action, naviguer vers n'importe quelle page, ou rechercher n'importe quel contenu — sans souris.

**Pourquoi ça marche**  
C'est l'interface la plus efficace possible pour les utilisateurs avancés : une seule entrée pour tout. Élimine le besoin de connaître l'emplacement exact d'une feature dans l'UI. La recherche floue rend l'accès aux commandes rarement utilisées aussi rapide qu'aux commandes fréquentes.

**Démo**

```
         ┌────────────────────────────────────┐
         │ 🔍  Rechercher ou taper une commande│
         ├────────────────────────────────────┤
         │ 🕐 Récents                         │
         │    Sprint 12 Planning              │
         │    #1234 Bug login                 │
         ├────────────────────────────────────┤
         │ ⚡ Actions                          │
         │    Créer une tâche          ⌘N     │
         │    Changer de projet        ⌘P     │
         │    Inviter un membre               │
         └────────────────────────────────────┘
```

**Meilleurs exemples**
- **Linear** — référence UX : fuzzy search, actions contextuelles, raccourcis affichés
- **Raycast** — la command palette comme produit entier, avec extensions
- **Figma** — `⌘/` pour les actions, `⌘K` pour la navigation
- **Vercel** — navigation + déploiements + actions dans une palette unifiée
- **Notion** — `⌘K` avec recherche full-text et navigation imbriquée

**Guide d'implémentation**

1. **Raccourci** : `⌘K` sur Mac, `Ctrl+K` sur Windows/Linux. Documenter les deux. Ne pas utiliser un raccourci non standard.
2. **Fuzzy search** : utiliser une lib comme `fuse.js` ou `cmdk`. La recherche doit tolérer les fautes et les abréviations.
3. **Groupes** : organiser les résultats en sections (Récents, Navigation, Actions, Contenu) avec headers.
4. **Raccourcis affichés** : montrer les raccourcis keyboard à droite des actions — renforce l'apprentissage.
5. **Actions contextuelles** : les premières suggestions doivent être contextuelles (page actuelle, projet actif).
6. **Performance** : la palette doit s'ouvrir en < 50ms et les résultats apparaître en < 100ms.
7. **Fermeture** : Échap ferme, clic en dehors ferme, Enter exécute la première action.

**Pièges à éviter**

- ❌ Recherche qui ne couvre pas les actions, seulement les contenus (ou vice-versa)
- ❌ Résultats sans score de pertinence — les items les plus récents/fréquents doivent remonter
- ❌ Palette trop large ou trop haute — max 600px de large, max 400px de haut avec scroll
- ❌ Pas de mode clavier pur (↑/↓/Enter) — la palette doit fonctionner sans souris
- ❌ Ouvrir une modale au-dessus d'une autre modale existante

---

## 10. Omnibox / unified search

**Ce que c'est** — Une barre de recherche globale qui interroge simultanément plusieurs types de données (pages, objets, utilisateurs, actions) et présente les résultats groupés par type.

**Pourquoi ça marche**  
Dans les applications complexes, l'utilisateur ne sait souvent pas exactement où chercher. L'omnibox centralise toutes les sources et laisse les résultats guider. C'est le Google de votre application.

**Démo**

```
┌─────────────────────────────────────────┐
│ 🔍  "alice"                         ✕  │
├─────────────────────────────────────────┤
│ PERSONNES                               │
│ 👤 Alice Martin  — Engineering         │
│ 👤 Alice Dupont  — Marketing           │
├─────────────────────────────────────────┤
│ TICKETS                                │
│ 🎫 #1201 Assigné à Alice               │
│ 🎫 #987  Créé par Alice                │
├─────────────────────────────────────────┤
│ DOCUMENTS                              │
│ 📄 Rapport Alice Q3                    │
└─────────────────────────────────────────┘
```

**Meilleurs exemples**
- **Slack** — search unifié messages + channels + personnes + fichiers
- **HubSpot** — contacts + deals + companies + activités dans une barre
- **Intercom** — conversations + contacts + articles dans une recherche
- **Glean** — enterprise search unifié cross-apps (Confluence, Jira, Drive...)

**Guide d'implémentation**

1. **Debounce** : déclencher la recherche après 200–300ms sans frappe pour éviter les requêtes à chaque caractère.
2. **Minimum 2 caractères** avant de lancer une recherche réseau.
3. **Résultats groupés** : header par catégorie, max 3–4 résultats par catégorie avant "Voir tout".
4. **Highlighting** : mettre en gras le terme recherché dans les résultats.
5. **Recherche vide** : afficher les récents et les favoris quand la query est vide.
6. **Indexation** : côté serveur, utiliser ElasticSearch ou Typesense pour la recherche full-text avec ranking.

**Pièges à éviter**

- ❌ Recherche qui ne couvre qu'un seul type d'objet (ex: que les contacts)
- ❌ Résultats non triés par pertinence — les correspondances exactes d'abord
- ❌ Pas de résultat vide géré — toujours afficher "Aucun résultat pour X" avec suggestion
- ❌ Recherche qui bloque l'UI pendant la requête — toujours asynchrone avec skeleton

---

## 11. Inline slash commands

**Ce que c'est** — Taper `/` dans un éditeur de texte déclenche un menu contextuel d'insertion de blocs, de mise en forme, ou d'exécution d'actions — sans quitter le clavier.

**Pourquoi ça marche**  
Élimine le besoin de barres d'outils encombrantes. L'utilisateur reste dans son flux d'écriture. Le menu est contextuel (déclenché à la position du curseur) et filtrable par frappe, ce qui le rend rapide même avec une grande liste d'options.

**Démo**

```
J'écris mon document et je veux insérer...

/tab                   ← filtrage en temps réel
┌──────────────────────────────┐
│ 📊 Tableau           ↵       │
│ 📋 Template                  │
│ 📑 Table des matières        │
└──────────────────────────────┘
```

**Meilleurs exemples**
- **Notion** — référence fondatrice, 50+ types de blocs
- **Linear** — slash commands dans les descriptions de tickets
- **Coda** — slash commands pour formules, tables, boutons
- **Slack** — `/remind`, `/poll`, `/giphy` — commandes d'application

**Guide d'implémentation**

1. **Déclencheur** : `/` en début de ligne ou après un espace. Ne pas déclencher au milieu d'un mot.
2. **Filtrage** : fuzzy match sur le texte tapé après `/`. Fermer le menu si aucun résultat.
3. **Fermeture** : Échap ferme sans insérer. Backspace jusqu'au `/` ferme le menu.
4. **Position** : ancrer le menu au curseur, pas au coin de l'écran. Gérer l'overflow si le curseur est en bas de page.
5. **Catégories** : grouper les commandes (Texte, Médias, Structure, AI) avec headers.
6. **Raccourcis directs** : permettre `/h1`, `/h2`, `/table` pour les blocs fréquents — skip le menu.

**Pièges à éviter**

- ❌ Menu qui ne se ferme pas si l'utilisateur continue à écrire sans sélectionner
- ❌ Trop de commandes sans filtre (> 20 items) — la liste devient inutilisable
- ❌ Menu qui sort des limites de l'écran sans repositionnement
- ❌ Pas de preview du bloc au hover dans le menu

---

## 12. Contextual right-click menu

**Ce que c'est** — Un menu contextuel riche et cohérent déclenché par clic droit (ou long-press sur mobile), présentant les actions disponibles pour l'élément ciblé.

**Pourquoi ça marche**  
Remplace les barres d'outils toujours visibles par des actions disponibles à la demande. Réduit le bruit visuel tout en maintenant l'accessibilité des actions. Les utilisateurs expérimentés préfèrent le clic droit aux boutons dans la toolbar.

**Démo**

```
[Clic droit sur un calque dans Figma]

┌────────────────────────────┐
│ Copier                ⌘C   │
│ Coller ici            ⌘V   │
│ Dupliquer             ⌘D   │
├────────────────────────────┤
│ Grouper               ⌘G   │
│ Créer un composant         │
├────────────────────────────┤
│ Renommer              ⌘R   │
│ Supprimer             ⌫    │
└────────────────────────────┘
```

**Meilleurs exemples**
- **Figma** — contextual menu ultra-riche, différent selon le type d'objet sélectionné
- **Miro** — menu contextuel pour sticky notes, shapes, connexions
- **Airtable** — clic droit sur cellule, ligne, colonne avec actions distinctes
- **Penpot** — menu contextuel design avec raccourcis clavier affichés

**Guide d'implémentation**

1. **Contextualité** : les actions doivent changer selon l'objet ciblé (cellule vs header de colonne vs row dans un tableau).
2. **Séparateurs** : grouper les actions par famille (clipboard, organisation, suppression) avec des séparateurs.
3. **Raccourcis affichés** : toujours afficher les raccourcis keyboard à droite — renforce l'apprentissage.
4. **Sous-menus** : max 1 niveau de sous-menu. Au-delà, revoir l'architecture.
5. **Position** : calculer si le menu sort de l'écran et le repositionner (flip vertical ou horizontal).
6. **Fermeture** : clic en dehors, Échap, ou sélection d'une action.

**Pièges à éviter**

- ❌ Menu identique quelle que soit la sélection — perd toute la valeur contextuelle
- ❌ Actions destructives (Supprimer) sans confirmation ou sans undo disponible
- ❌ Menu trop long (> 12 items) sans séparateurs ni sous-menus
- ❌ Remplacer le menu natif du browser sur des éléments où le menu natif est utile (input texte)

---

---

# Data & Tables

---

## 13. Spreadsheet-like inline editing

**Ce que c'est** — Les cellules d'un tableau deviennent éditables au clic ou double-clic, avec des raccourcis clavier type tableur (Tab, Entrée, flèches) pour naviguer entre les champs.

**Pourquoi ça marche**  
Élimine le round-trip modal (cliquer pour ouvrir une modale, éditer, valider, fermer). Pour les workflows de data entry intensifs, la différence de vitesse est radicale. Les utilisateurs habitués à Excel/Sheets adoptent le pattern instantanément.

**Démo**

```
┌──────────────┬───────────┬────────────┐
│ Nom          │ Statut    │ Priorité   │
├──────────────┼───────────┼────────────┤
│ Bug login    │ [In prog▼]│ High       │  ← clic → dropdown inline
│ Fix CSS      │ Done      │[Medium   ▼]│  ← Tab navigue à la cellule suivante
│ [Nouvelle...│           │            │  ← Entrée en bas = nouvelle ligne
└──────────────┴───────────┴────────────┘
```

**Meilleurs exemples**
- **Airtable** — référence absolue, édition inline pour tous les types de champs
- **Notion databases** — inline editing avec types de champs riches
- **Attio** — CRM avec édition inline façon spreadsheet
- **Linear** — édition inline des propriétés dans les listes

**Guide d'implémentation**

1. **Déclencheur** : simple clic pour les selects/dates, double-clic pour le texte long (évite les éditions accidentelles au scroll).
2. **Navigation clavier** : Tab → cellule suivante, Shift+Tab → précédente, Entrée → ligne suivante, Échap → annuler l'édition.
3. **Types de champs** : chaque type a son widget inline — text input, select dropdown, date picker, checkbox, user picker.
4. **Validation** : valider à la perte de focus (blur), pas seulement à Entrée.
5. **Indicateur d'édition** : outline colored sur la cellule active + curseur `text` ou `pointer` selon le type.
6. **Undo** : `⌘Z` doit annuler la dernière modification cellule par cellule.

**Pièges à éviter**

- ❌ Édition déclenchée au survol — éditions accidentelles
- ❌ Pas de feedback visuel sur la cellule en cours d'édition
- ❌ Soumission uniquement via un bouton "Sauvegarder" — casse le flux tableur
- ❌ Champs texte long sans expansion de hauteur — le contenu est tronqué

---

## 14. Filtres persistants & URL-encodés

**Ce que c'est** — Les filtres actifs sont encodés dans l'URL, persistants entre sessions, et partageables — un lien filtré envoie le destinataire à la même vue filtrée.

**Pourquoi ça marche**  
Les vues filtrées sont souvent des "vues de travail" récurrentes. Les encoder dans l'URL permet : partager une vue précise par lien, sauvegarder une URL comme bookmark, et naviguer avec le bouton retour sans perdre ses filtres.

**Démo**

```
URL : /issues?status=open&assignee=alice&priority=high&sort=updated

┌──────────────────────────────────────────────────┐
│ Filtres actifs :  [Ouvert ✕]  [Alice ✕]  [High ✕]│
│                   + Ajouter un filtre             │
├──────────────────────────────────────────────────┤
│ Résultats (12)                         ↕ Récents  │
│ ...                                               │
└──────────────────────────────────────────────────┘
```

**Meilleurs exemples**
- **Linear** — filtres URL-encodés, vues sauvegardables avec nom
- **GitHub Issues** — query language puissant dans l'URL (`is:open assignee:alice`)
- **Retool** — filtres dynamiques URL-driven pour les apps internes
- **Metabase** — dashboards filtrables avec paramètres URL partageables

**Guide d'implémentation**

1. **Format URL** : query params standards (`?key=value&key2=value2`). Pour les valeurs multiples : `?status=open&status=in_progress` ou `?status[]=open`.
2. **Synchronisation** : l'état des filtres dans l'UI doit être entièrement dérivé de l'URL. L'URL est la source de vérité.
3. **Mise à jour URL** : utiliser `history.pushState` (nouvelle entrée d'historique) pour les changements significatifs, `history.replaceState` pour les changements de tri ou de pagination.
4. **Indicateur visuel** : afficher les filtres actifs sous forme de chips/tags avec bouton de suppression.
5. **Reset** : bouton "Effacer les filtres" qui remet l'URL à son état de base.
6. **Validation** : valider les paramètres URL à l'arrivée — des paramètres invalides ne doivent pas casser la page.

**Pièges à éviter**

- ❌ État de filtre en `useState` local uniquement — perdu au refresh
- ❌ URL trop longue (> 2000 caractères) avec de nombreux filtres — préférer les vues sauvegardées côté serveur
- ❌ Pas de décompte de résultats visible avec les filtres actifs
- ❌ Filtres qui s'appliquent uniquement à la vue actuelle mais pas aux données exportées

---

## 15. Virtual scrolling

**Ce que c'est** — Technique de rendu qui n'affiche que les éléments de liste visibles dans le viewport, même si la liste contient des milliers d'entrées.

**Pourquoi ça marche**  
Sans virtual scrolling, une liste de 10 000 items crée 10 000 nœuds DOM — le navigateur s'effondre. Avec le virtual scroll, seuls 20–50 nœuds existent à tout moment. L'utilisateur ne voit pas la différence mais les performances sont radicalement meilleures.

**Démo**

```
┌─────────────────────┐
│ Item 1              │  ← rendu
│ Item 2              │  ← rendu
│ Item 3              │  ← rendu
│ ...                 │
│ Item 20             │  ← rendu (dernier visible)
└─────────────────────┘
   │                     Items 21–10000 : non rendus,
   ▼ scroll              remplacés par un spacer div de
                         hauteur calculée
┌─────────────────────┐
│ Item 21             │  ← rendu (recycling du DOM)
│ Item 22             │
...
```

**Meilleurs exemples**
- **Slack** — messages history avec virtual scroll + sticky date headers
- **Gmail** — liste d'emails (milliers de threads sans lag)
- **Airtable** — grilles avec des dizaines de milliers de lignes
- **Figma** — panneau Layers avec virtual scroll sur les designs complexes

**Guide d'implémentation**

1. **Librairies** : `react-window`, `react-virtual` (TanStack Virtual), `vue-virtual-scroller`. Ne pas réimplémenter from scratch.
2. **Hauteur fixe vs variable** : hauteur fixe par item = simple et performant. Hauteur variable = nécessite une estimation initiale et mesure au rendu.
3. **Overscan** : rendre 3–5 items supplémentaires au-delà du viewport (en haut et en bas) pour éviter le flash au scroll rapide.
4. **Sticky headers** : compatibles avec le virtual scroll si implémentés séparément (position sticky sur un container wrappant le virtual list).
5. **Focus clavier** : le virtual scroll peut casser la navigation clavier — s'assurer que Tab et les flèches déclenchent le scroll vers les items non rendus.

**Pièges à éviter**

- ❌ Implémenter le virtual scroll pour des listes < 200 items — overhead inutile
- ❌ Animer les items au scroll (entrée/sortie) — crée des artifacts visuels
- ❌ `innerHTML` pour le recycling — toujours utiliser le virtual DOM du framework
- ❌ Oublier le `scrollRestoration` — l'utilisateur revient en haut après navigation

---

## 16. Column resizing & reordering

**Ce que c'est** — Les colonnes d'un tableau peuvent être redimensionnées par drag sur la bordure et réorganisées par drag & drop sur le header. Ces préférences sont mémorisées par utilisateur.

**Pourquoi ça marche**  
Les utilisateurs ont des workflows différents et valorisent des colonnes différentes. Donner le contrôle sur la disposition est un gage de respect de leur workflow. C'est la personnalisation minimale attendue de tout tableau de données professionnel.

**Démo**

```
         Poignée de resize
               ↓
┌──────────────╫──────────┬──────────────┐
│ Nom          ║ Statut   │ Date         │  ← drag header pour réordonner
├──────────────╫──────────┼──────────────┤
│              ║          │              │
│   drag →→→  ║          │              │
│              ║          │              │
└──────────────╫──────────┴──────────────┘
        curseur col-resize
```

**Meilleurs exemples**
- **Airtable** — resize + reorder + hide/show colonnes
- **Notion tables** — resize des colonnes, réorganisation par drag
- **HubSpot CRM** — colonnes configurables avec état mémorisé par user
- **Attio** — configuration avancée des colonnes par vue

**Guide d'implémentation**

1. **Resize** : zone de 6–8px sur la bordure droite du header, curseur `col-resize`. Largeur minimum par colonne (ex: 80px).
2. **Reorder** : drag sur le corps du header (pas la zone resize). Indicateur visuel de drop position (ligne verticale entre colonnes).
3. **Persistance** : sauvegarder largeurs et ordre en base côté serveur (pas seulement localStorage) — l'utilisateur retrouve sa config sur tous ses appareils.
4. **Colonnes fixes** : permettre d'épingler des colonnes à gauche (comme Excel freeze panes). Séparateur visuel entre colonnes fixes et scrollables.
5. **Menu de colonne** : clic sur header → dropdown avec Trier, Filtrer, Masquer, Épingler, Redimensionner à l'auto.

**Pièges à éviter**

- ❌ Resize qui affecte toutes les colonnes suivantes au lieu de juste celle ciblée
- ❌ Pas de largeur minimum — les colonnes peuvent disparaître
- ❌ Reorder qui se déclenche accidentellement pendant un clic simple sur le header (pour trier)
- ❌ Préférences perdues au refresh car uniquement en mémoire

---

---

# Feedback & États

---

## 17. Toast notification + undo

**Ce que c'est** — Une notification éphémère (toast) qui apparaît en bas de l'écran après une action, avec un bouton "Annuler" accessible pendant quelques secondes — remplaçant les modales de confirmation.

**Pourquoi ça marche**  
"Êtes-vous sûr ?" est le pattern UX le plus détesté : il interrompt, demande un effort cognitif, et n'empêche pas les erreurs (les utilisateurs cliquent "Oui" par réflexe). Le toast + undo est moins intrusif, aussi sûr, et plus rapide.

**Démo**

```
Action : supprimer un email

[Aucune modale de confirmation]

┌──────────────────────────────────┐
│  Email archivé    [Annuler]   ✕  │  ← toast, disparaît après 5s
└──────────────────────────────────┘
          ▲
    Clic "Annuler" → action reversée
    Laisser disparaître → action confirmée
```

**Meilleurs exemples**
- **Gmail** — référence absolue, archive/suppression avec undo
- **Linear** — toast sur toutes les actions de modification
- **Notion** — toast sur suppression de blocs avec undo
- **Slack** — toast sur archivage de channel

**Guide d'implémentation**

1. **Durée** : 4–6 secondes. Suffisant pour lire et réagir, pas assez long pour gêner.
2. **Position** : bas gauche ou bas centre de l'écran. Jamais en haut (couvre le contenu d'action).
3. **Stack** : si plusieurs toasts apparaissent en séquence, les empiler verticalement (le plus récent en bas).
4. **Pause au hover** : le timer de disparition se met en pause quand la souris est sur le toast.
5. **Action undo côté serveur** : l'undo doit fonctionner côté serveur si l'action a déjà été persistée (soft delete + restore, pas seulement côté client).
6. **Types** : success (vert), error (rouge), info (bleu), warning (orange) — avec icône correspondante.

**Pièges à éviter**

- ❌ Toast sans undo pour les actions destructives irréversibles
- ❌ Toast qui disparaît en < 3 secondes — trop court pour lire et réagir
- ❌ Empiler plus de 3 toasts simultanément — les regrouper
- ❌ Toast positionné devant un bouton d'action fréquent

---

## 18. Optimistic UI

**Ce que c'est** — L'interface se met à jour immédiatement après l'action de l'utilisateur, avant que le serveur confirme. Si le serveur retourne une erreur, l'UI revient à son état précédent silencieusement.

**Pourquoi ça marche**  
Élimine la latence perçue. Sur une bonne connexion, l'utilisateur ne voit jamais l'état de chargement. L'interface semble instantanée. La grande majorité des actions réussissant, le rollback reste un cas rare.

**Démo**

```
Utilisateur clique "Marquer comme fait"

Sans optimistic UI :            Avec optimistic UI :
☐ Tâche A                      ✓ Tâche A  ← immédiat
[spinner 300ms]                 (confirmation serveur arrive 300ms après,
✓ Tâche A                        invisible pour l'user)
```

**Meilleurs exemples**
- **Linear** — toutes les actions de statut, assignation, priorité
- **Figma** — déplacement d'objets, changement de propriétés
- **Superhuman** — archive, snooze, labels instantanés
- **Twitter/X** — likes, retweets (avec rollback visible si erreur réseau)

**Guide d'implémentation**

1. **Mutation locale d'abord** : mettre à jour le store/state local immédiatement, puis lancer la requête réseau en parallèle.
2. **Rollback sur erreur** : en cas d'erreur serveur, restaurer l'état précédent et afficher un toast d'erreur.
3. **Idempotence** : s'assurer que les actions sont idempotentes côté serveur — en cas de double soumission, le résultat doit être identique.
4. **Conflits** : gérer le cas où l'utilisateur effectue une deuxième action avant la confirmation de la première (queue ou annulation de la première).
5. **Librairies** : `react-query` / `TanStack Query` et `SWR` ont un support natif des mutations optimistes.

**Pièges à éviter**

- ❌ Optimistic UI sur des actions avec effets secondaires importants (paiement, envoi d'email) — réserver aux mutations simples
- ❌ Rollback sans notification à l'utilisateur — il ne comprend pas pourquoi l'état a changé
- ❌ Pas de gestion de l'état "pending" pour les actions qui prennent du temps (> 2s)
- ❌ Optimistic UI avec des données dérivées complexes — la cohérence est difficile à maintenir

---

## 19. Empty states actionnables

**Ce que c'est** — Quand une liste ou une vue est vide, afficher un état vide qui guide vers une action concrète plutôt qu'un message générique "Aucun résultat".

**Pourquoi ça marche**  
Un état vide est une opportunité d'onboarding. L'utilisateur est exactement là où il a besoin d'être pour commencer. Un bon empty state répond à "qu'est-ce que je fais maintenant ?" avec une action immédiate.

**Démo**

```
Vue "Mes projets" sans projet :

     ┌──────────────────────────┐
     │                          │
     │    🗂️                    │
     │                          │
     │  Aucun projet pour l'    │
     │  instant                 │
     │                          │
     │  Organisez votre travail │
     │  en projets pour mieux   │
     │  collaborer.             │
     │                          │
     │  [+ Créer un projet]     │
     │  [Importer depuis Jira]  │
     │                          │
     └──────────────────────────┘
```

**Meilleurs exemples**
- **Notion** — empty states avec templates suggérés et exemples cliquables
- **Linear** — empty states distincts selon le contexte (premier projet, filtre sans résultat, recherche vide)
- **Mailchimp** — empty states avec illustrations custom et guides d'action
- **Stripe Dashboard** — empty states avec données de test pour explorer

**Guide d'implémentation**

1. **Distinguer les types d'empty state** :
   - Première utilisation (onboarding) → action principale + option d'import
   - Filtre sans résultat → suggérer de modifier le filtre ou de l'effacer
   - Recherche sans résultat → afficher le terme et suggérer des alternatives
2. **Hiérarchie visuelle** : illustration ou icône → titre → description courte → CTA principal → CTA secondaire optionnel.
3. **Ton** : positif et orienté action. Éviter "Aucun X trouvé." Préférer "Commencez par créer votre premier X."
4. **Illustrations** : optionnel mais efficace — cohérent avec le design system, pas trop complexe.
5. **CTA unique** : un seul bouton principal. Deux maximum si les deux actions sont vraiment distinctes.

**Pièges à éviter**

- ❌ "Aucun résultat." sans plus d'information
- ❌ Même empty state pour tous les contextes — l'état post-filtre n'est pas l'état first-use
- ❌ Illustration trop grande qui pousse le CTA hors du viewport
- ❌ Empty state qui disparaît et réapparaît pendant le chargement — gérer l'ordre loading → data → empty

---

## 20. Skeleton screens

**Ce que c'est** — Pendant le chargement des données, afficher des silhouettes grises animées qui reproduisent la structure du contenu à venir, plutôt qu'un spinner centré.

**Pourquoi ça marche**  
Les skeleton screens réduisent la perception de latence en montrant que quelque chose arrive. Ils préviennent le layout shift (le contenu n'arrive pas en déplaçant l'UI) et maintiennent l'orientation spatiale de l'utilisateur pendant le chargement.

**Démo**

```
Chargement d'une liste de contacts :

┌────────────────────────────────────┐
│ ████  ████████████████  ████████   │  ← animation shimmer
│ ████  █████████  ████   ████       │    de gauche à droite
│ ████  ████████████████  ████████   │
│ ████  █████  ████████   █████      │
└────────────────────────────────────┘
```

**Meilleurs exemples**
- **LinkedIn** — skeleton parfaitement calqué sur la structure du feed
- **Slack** — skeleton de la liste de messages et du panneau de channels
- **GitHub** — skeleton sur les listes d'issues et pull requests
- **Stripe** — skeleton sur les tableaux du dashboard

**Guide d'implémentation**

1. **Structure fidèle** : le skeleton doit approximer la structure réelle (nombre de lignes, hauteurs relatives). Pas un rectangle unique.
2. **Animation shimmer** : gradient qui se déplace de gauche à droite en boucle. `@keyframes` sur `background-position`.
3. **Couleur** : `--color-background-secondary` pour les blocks, légèrement plus clair pour le shimmer. S'adapter au dark mode.
4. **Durée** : afficher le skeleton après 150–200ms (évite le flash pour les chargements rapides). Si les données arrivent en < 150ms, ne pas afficher le skeleton du tout.
5. **Transition** : fade out du skeleton (100ms) avant d'afficher le contenu pour éviter un flash brutal.

**Pièges à éviter**

- ❌ Skeleton qui ne ressemble pas à la structure réelle — le layout shift reste présent
- ❌ Skeleton affiché indéfiniment si la requête échoue — prévoir un état d'erreur
- ❌ Animation trop rapide (< 1s) ou trop lente (> 2s) — 1.5s est le sweet spot
- ❌ Skeleton sur des composants à chargement instantané (< 100ms) — ajoute de la complexité sans bénéfice

---

---

# AI — Accès & Invocation

---

## 21. AI sidebar persistante

**Ce que c'est** — Un panneau latéral dédié à l'IA, accessible depuis n'importe quelle vue de l'application, rétractable, qui maintient l'historique de conversation dans le contexte de la session de travail.

**Pourquoi ça marche**  
Évite de quitter l'application pour accéder à un outil AI externe. L'AI a accès au contexte de la vue courante (document ouvert, ticket sélectionné) sans que l'utilisateur ait à copier-coller. La persistance du fil permet de construire sur les échanges précédents.

**Démo**

```
┌──────────────────────┬───────────────────┐
│ CONTENU PRINCIPAL    │ AI Assistant      │
│                      │ ─────────────── │
│ # Mon ticket         │ 👤 Comment        │
│ Description...       │ améliorer cette   │
│                      │ description ?     │
│                      │                   │
│                      │ 🤖 Voici 3        │
│                      │ suggestions...    │
│                      │                   │
│                      │ ────────────────  │
│                      │ [Écrire...    ↑] │
└──────────────────────┴───────────────────┘
```

**Meilleurs exemples**
- **GitHub Copilot Chat** — sidebar contextuelle au fichier ouvert dans VS Code
- **Notion AI** — sidebar qui connaît le document en cours
- **HubSpot Breeze** — AI sidebar dans le CRM, accès aux données contact
- **Salesforce Einstein** — sidebar avec contexte CRM injecté automatiquement

**Guide d'implémentation**

1. **Largeur** : 320–400px. Rétractable avec le même pattern icon-rail (pattern #1).
2. **Contexte automatique** : injecter silencieusement dans le system prompt le contexte de la vue active (titre du document, statut du ticket, données du contact) sans que l'utilisateur ait à le préciser.
3. **Historique** : persister l'historique par session de travail (document, ticket, etc.) — idéalement côté serveur.
4. **Indicateur de contexte** : afficher visuellement quel contexte est injecté ("Je vois : Ticket #1234") pour la transparence.
5. **Actions rapides** : proposer des actions en un clic selon le contexte (Résumer, Améliorer, Traduire).

**Pièges à éviter**

- ❌ Sidebar qui perd son historique à chaque navigation
- ❌ Contexte injecté mais non visible — l'utilisateur ne comprend pas pourquoi l'AI "sait" des choses
- ❌ Largeur fixe non rétractable sur les petits écrans
- ❌ Sidebar qui ralentit le chargement de la page principale

---

## 22. ⌘K → AI intent

**Ce que c'est** — La command palette (pattern #9) détecte quand l'utilisateur saisit une question ou une commande en langage naturel plutôt qu'un terme de recherche, et bascule automatiquement vers un mode AI.

**Pourquoi ça marche**  
Un seul point d'entrée pour tout. L'utilisateur n'a pas besoin de choisir entre "rechercher" et "demander à l'AI" — la palette fait la distinction automatiquement. Réduit la friction d'adoption de l'AI en l'intégrant dans un pattern déjà familier.

**Démo**

```
⌘K →

Mode recherche :          Mode AI (détection automatique) :
┌──────────────────┐      ┌──────────────────────────────┐
│ 🔍 sprint 12     │      │ ✨ Résume les tickets ouverts │
│ ─────────────    │  vs  │ ─────────────────────────────│
│ 📋 Sprint 12     │      │ Appuyez sur Entrée pour      │
│ 🔍 Voir tout...  │      │ demander à l'AI              │
└──────────────────┘      └──────────────────────────────┘
```

**Meilleurs exemples**
- **Linear** — `⌘K` détecte les questions et propose une réponse AI
- **Raycast AI** — extension AI native dans la palette Raycast
- **Vercel v0** — prompt natural language → génération de composant
- **Coda** — `/` + question naturelle → AI response inline

**Guide d'implémentation**

1. **Détection d'intention** : heuristiques simples — query commençant par un verbe (Résume, Génère, Explique), contenant "?" ou "comment", dépassant 4 mots. Pas besoin de ML côté client.
2. **Indicateur visuel** : changer l'icône de loupe en icône sparkle/AI quand le mode bascule.
3. **Transition douce** : ne pas changer l'UI brutalement — animer la transition entre mode recherche et mode AI.
4. **Fallback** : si l'AI ne comprend pas, retomber sur la recherche classique.
5. **Raccourci explicite** : permettre aussi de forcer le mode AI avec un préfixe (ex: `?` ou `ai:`).

**Pièges à éviter**

- ❌ Basculer en mode AI trop agressivement (dès 2 mots) — perturbe la recherche normale
- ❌ Pas de moyen de forcer la recherche classique quand le mode AI est activé
- ❌ Latence visible lors du basculement de mode
- ❌ Réponse AI dans la palette qui nécessite un scroll — la palette doit rester compacte

---

## 23. Floating AI button contextuel

**Ce que c'est** — Un bouton ou menu AI qui apparaît à la sélection de texte ou d'un objet, ancré sur la sélection, proposant des actions contextuelles (améliorer, résumer, traduire, expliquer).

**Pourquoi ça marche**  
Le moment de sélection est le signal d'intention le plus fort : l'utilisateur a identifié un contenu sur lequel il veut agir. Proposer des actions AI exactement à ce moment, sans déplacement vers une autre interface, est le plus court chemin vers la valeur.

**Démo**

```
L'utilisateur sélectionne du texte :

"Cette fonctionnalité permettra aux utilisateurs de..."
 ═══════════════════════════════════════
              ┌───────────────────────────┐
              │ ✨ Améliorer  📝 Résumer  │
              │ 🌍 Traduire  💬 Expliquer │
              └───────────────────────────┘
```

**Meilleurs exemples**
- **Notion AI** — toolbar AI sur sélection de texte
- **Google Docs** — "Help me write" sur sélection
- **Grammarly** — suggestions sur sélection dans tout champ texte
- **Superhuman** — actions AI sur sélection d'email

**Guide d'implémentation**

1. **Déclencheur** : écouter l'event `mouseup` / `selectionchange`. N'afficher qu'après que la sélection est stable (debounce 100ms).
2. **Position** : au-dessus de la sélection par défaut, en dessous si la sélection est trop proche du haut du viewport.
3. **Actions** : limiter à 4–6 actions. Les plus fréquentes en icônes directes, les autres dans un "..." menu.
4. **Fermeture** : disparaît si la sélection est désélectionnée (click en dehors), si Échap est pressé.
5. **Résultat** : remplacer la sélection par le résultat AI, ou l'afficher dans un panel séparé avec accept/reject (pattern #26).

**Pièges à éviter**

- ❌ Toolbar qui apparaît sur des sélections accidentelles d'un mot
- ❌ Position fixe (coin de l'écran) non ancrée sur la sélection
- ❌ Actions trop génériques sans lien avec le type de contenu sélectionné
- ❌ Toolbar qui bloque le texte sélectionné

---

## 24. Inline slash AI commands

**Ce que c'est** — Extension du pattern slash commands (pattern #11) avec des commandes dédiées à l'AI : `/ai`, `/generate`, `/improve`, `/summarize` — qui déclenchent une génération inline dans l'éditeur.

**Pourquoi ça marche**  
Intègre l'AI directement dans le flux d'écriture sans sortir de l'éditeur. L'utilisateur reste dans son contexte cognitif. La génération se fait à la position du curseur, exactement là où le contenu est attendu.

**Démo**

```
# Mon rapport Q3

/améliore ce paragraphe

┌─────────────────────────────────────────┐
│ ✨ Améliorer le paragraphe ci-dessus... │
│ [Écrire des instructions...          ]  │
│                                [Générer]│
└─────────────────────────────────────────┘
```

**Meilleurs exemples**
- **Notion AI** — `/ai` ouvre un prompt inline avec contexte du document
- **Coda AI** — commandes AI intégrées dans l'éditeur de doc
- **Linear** — `/summarize` dans les commentaires de ticket
- **Confluence AI** — commandes AI dans l'éditeur de page

**Guide d'implémentation**

1. **Prompt inline** : après la commande slash, afficher un champ de saisie pour les instructions supplémentaires.
2. **Contexte** : injecter automatiquement le contenu environnant (paragraphe précédent, titre de section) dans le prompt.
3. **Streaming** : afficher le texte généré en streaming directement dans l'éditeur avec un curseur clignotant ou un fond de couleur distinct.
4. **Accept/reject** : toujours proposer d'accepter, modifier, ou annuler avant de committer le contenu généré.
5. **Annulation** : Échap annule la génération en cours et supprime le contenu partiellement généré.

**Pièges à éviter**

- ❌ Génération qui remplace immédiatement le contenu existant sans confirmation
- ❌ Pas d'indicateur de chargement pendant la génération
- ❌ Commandes AI qui ne fonctionnent qu'à certains endroits (début de ligne uniquement)
- ❌ Résultat non éditable après génération

---

---

# AI — Génération & Édition

---

## 25. Streaming text (typewriter)

**Ce que c'est** — La réponse de l'AI s'affiche progressivement, token par token, au lieu d'apparaître d'un bloc après un temps d'attente — donnant l'impression que l'AI "écrit" en temps réel.

**Pourquoi ça marche**  
Réduit massivement la perception de latence. L'utilisateur commence à lire pendant que la génération se poursuit. Le mouvement du texte signale que le système est actif. Psychologiquement, attendre une réponse partielle est moins frustrant qu'attendre une réponse complète.

**Démo**

```
[Requête envoyée]

Sans streaming :            Avec streaming :
                            Voici▌
[······ 3s ······]          Voici une▌
                            Voici une réponse▌
Voici une réponse           Voici une réponse complète▌
complète avec tous          Voici une réponse complète
les détails.                avec tous les détails.
```

**Meilleurs exemples**
- **Claude** — streaming avec affichage progressif du markdown rendu
- **ChatGPT** — streaming avec rendu progressif du markdown
- **Notion AI** — streaming dans l'éditeur de document
- **GitHub Copilot Chat** — streaming dans la sidebar VS Code

**Guide d'implémentation**

1. **SSE ou WebSocket** : utiliser Server-Sent Events (`EventSource`) pour les réponses unidirectionnelles. WebSocket si la bidirectionnalité est nécessaire.
2. **Rendu du markdown** : éviter de re-render tout le markdown à chaque token (coûteux). Stratégie : accumuler dans un buffer, re-render par chunks de 50–100ms.
3. **Curseur clignotant** : ajouter un curseur animé à la fin du texte en cours de streaming pour indiquer que l'écriture continue.
4. **Stop button** : toujours afficher un bouton d'arrêt pendant le streaming — l'utilisateur doit pouvoir interrompre.
5. **Scroll automatique** : faire scroller le conteneur pour suivre le dernier token généré, mais stopper si l'utilisateur scrolle manuellement vers le haut.

**Pièges à éviter**

- ❌ Re-render complet à chaque token — le scroll saute, l'UI tremble
- ❌ Pas de stop button — l'utilisateur est captif d'une mauvaise génération
- ❌ Cacher la réponse partielle derrière un skeleton pendant le streaming
- ❌ Scroll forcé qui ramène l'utilisateur en bas alors qu'il lisait plus haut

---

## 26. Diff view accept/reject

**Ce que c'est** — Les modifications suggérées par l'AI sont présentées en mode diff (ajouts en vert, suppressions en rouge), et l'utilisateur peut accepter ou rejeter globalement ou bloc par bloc.

**Pourquoi ça marche**  
Donne le contrôle total à l'utilisateur. Il voit exactement ce que l'AI veut changer avant que ça soit appliqué. La granularité (accepter ligne par ligne) permet de prendre le meilleur de la suggestion sans accepter l'entier. C'est le pattern qui convertit la méfiance envers l'AI en confiance.

**Démo**

```
┌─────────────────────────────────────────────────┐
│ - L'utilisateur peut modifier les paramètres.   │  ← rouge : supprimé
│ + L'utilisateur peut personnaliser les          │  ← vert : ajouté
│ + paramètres selon ses préférences.             │
│                                                 │
│   Le système enregistre les changements.        │  ← gris : inchangé
├─────────────────────────────────────────────────┤
│  [✓ Accepter tout]  [✗ Rejeter tout]  [Modifier]│
└─────────────────────────────────────────────────┘
```

**Meilleurs exemples**
- **GitHub Copilot** — diff view dans l'éditeur pour les suggestions de code
- **Cursor** — diff view avec accept/reject par hunk de code
- **Devin** — diff view sur les modifications de fichiers par l'agent
- **Windsurf** — diff view avec inline accept sur chaque ligne

**Guide d'implémentation**

1. **Niveau de granularité** : accept/reject global + accept/reject par bloc de changement (hunk). Le line-by-line est optionnel.
2. **Couleurs** : vert pour les ajouts (`#dcfce7` bg, `#16a34a` texte), rouge pour les suppressions (`#fee2e2` bg, `#dc2626` texte). Gris neutre pour l'inchangé.
3. **Lib de diff** : utiliser `diff` (npm) pour calculer le diff, `react-diff-viewer` ou équivalent pour l'affichage.
4. **Édition post-accept** : après acceptation, le contenu doit être éditable normalement.
5. **Raccourcis** : `Tab` pour naviguer entre les hunks, `Y` pour accepter, `N` pour rejeter (convention Git).

**Pièges à éviter**

- ❌ Diff illisible sur les changements de formatage purs (espaces, retours à la ligne)
- ❌ Pas de moyen d'accepter partiellement (seulement global accept/reject)
- ❌ Diff qui ne gère pas les déplacements de blocs (texte déplacé = tout supprimé + tout ajouté)
- ❌ Accept qui ne peut pas être annulé (⌘Z doit fonctionner)

---

## 27. Ghost text / inline autocomplete

**Ce que c'est** — Une suggestion de complétion grisée s'affiche dans le champ de saisie, après le curseur. L'utilisateur l'accepte en appuyant sur Tab, ou continue à taper pour l'ignorer.

**Pourquoi ça marche**  
Zéro friction : la suggestion est là, visible, acceptée en une touche. Pas de menu à ouvrir, pas de dialogue. Réduit considérablement le temps de saisie pour les utilisateurs qui trouvent les suggestions pertinentes. La touche Tab est le contrat universel — connu de tous depuis les IDEs.

**Démo**

```
Utilisateur tape : "Rédigez un email pour"
Suggestion AI  : " confirmer le rendez-vous du 15 janvier"

[Rédigez un email pour confirmer le rendez-vous du 15 janvier]
                      ↑ grisé, transparent
                      Tab → accepté
                      Toute autre touche → ignoré
```

**Meilleurs exemples**
- **GitHub Copilot** — référence fondatrice dans VS Code
- **Cursor** — ghost text sur tous les fichiers de code
- **Superhuman** — ghost text pour la complétion d'emails
- **Notion** — ghost text dans l'éditeur après quelques mots

**Guide d'implémentation**

1. **Déclencheur** : après une pause de frappe (300–500ms). Annuler et relancer à chaque frappe.
2. **Affichage** : couleur `--color-text-tertiary` (gris clair) pour la suggestion. Ne jamais la rendre aussi visible que le texte réel.
3. **Acceptance** : Tab accepte la suggestion complète. ⌘→ peut accepter mot par mot.
4. **Rejection** : Échap supprime la suggestion. Toute autre touche que Tab continue la saisie et ignore la suggestion.
5. **Longueur** : limiter la suggestion à 1–3 phrases. Les suggestions très longues ont un taux d'acceptation plus faible.
6. **Debounce + cancel** : annuler la requête en cours si l'utilisateur tape avant que la suggestion arrive.

**Pièges à éviter**

- ❌ Ghost text de même couleur que le texte réel — impossible à distinguer
- ❌ Suggestion qui remplace le texte existant au lieu de s'ajouter après
- ❌ Pas d'annulation quand l'utilisateur tape avant la fin de génération
- ❌ Tab qui accepte la suggestion et insère aussi une tabulation

---

## 28. Canvas / artifact panel

**Ce que c'est** — La réponse AI génère un objet riche (document, code, tableau, composant UI) dans un panneau séparé du chat, éditable directement, persistant entre les échanges.

**Pourquoi ça marche**  
Sort du paradigme "réponse texte dans le chat" pour créer un objet de travail réel. L'utilisateur peut itérer sur l'artefact ("rends ce tableau plus formel", "ajoute une colonne Total") sans perdre l'objet entre les échanges. Le chat devient un outil de manipulation de l'artefact, pas juste de réponse à des questions.

**Démo**

```
┌────────────────────────┬──────────────────────┐
│ CHAT                   │ CANVAS               │
│ ─────────────────────  │ ──────────────────── │
│ 👤 Génère un tableau   │ | Produit | Prix | Q │
│    des ventes Q3       │ | ─────── | ─── | ─ │
│                        │ | Widget  | 29€ | 42 │
│ 🤖 Voici le tableau.   │ | Gadget  | 49€ | 28 │
│    [Voir dans canvas→] │ | Truc    | 19€ | 67 │
│                        │ ──────────────────── │
│ 👤 Ajoute une colonne  │ Éditable directement │
│    Total               │ ──────────────────── │
│                        │ [Exporter] [Copier]  │
└────────────────────────┴──────────────────────┘
```

**Meilleurs exemples**
- **Claude Artifacts** — canvas pour code, HTML, SVG, React, Markdown
- **ChatGPT Canvas** — canvas pour documents et code avec edition collaborative
- **v0 (Vercel)** — canvas pour composants React avec preview live
- **Gemini Docs** — génération dans Google Docs directement

**Guide d'implémentation**

1. **Types d'artefacts** : définir les types supportés (Markdown, Code, HTML, JSON, Tableau) et les rendre extensibles.
2. **Iframe sandboxé** : pour les artefacts HTML/JS, utiliser un iframe sandbox pour l'isolation de sécurité.
3. **Synchronisation** : les modifications manuelles dans le canvas doivent être reflétées dans les échanges suivants (injection dans le contexte de conversation).
4. **Version history** : chaque génération/modification crée une version — permettre de revenir à une version précédente.
5. **Export** : toujours proposer copier dans le presse-papier + télécharger en format natif.

**Pièges à éviter**

- ❌ Canvas qui réinitialise à chaque message — l'artefact doit persister
- ❌ Pas de moyen d'éditer manuellement l'artefact — la génération AI ne peut pas être parfaite
- ❌ Canvas sans version history — les modifications accidentelles ne peuvent pas être annulées
- ❌ Sécurité insuffisante sur les artefacts exécutables (XSS si pas de sandbox)

---

---

# AI — Contexte & Mémoire

---

## 29. @-mentions pour le contexte

**Ce que c'est** — Mentionner `@fichier`, `@page`, `@utilisateur`, `@ticket` dans le prompt injecte le contenu référencé dans le contexte de la requête AI, de manière explicite et auditable.

**Pourquoi ça marche**  
Résout le problème du contexte de l'AI de manière transparente. L'utilisateur contrôle exactement quelles données sont envoyées. L'AI a le bon contexte sans que l'utilisateur copie-colle. La mention est visible dans le prompt — ce qui est injecté est connu.

**Démo**

```
[Prompt de l'utilisateur]

Résume les blocages de @Sprint-12 et
assigne les tâches critiques à @Alice

          ↓ résolution avant envoi à l'AI

[Prompt réel envoyé à l'API]
Résume les blocages de [contenu complet du Sprint 12]
et assigne les tâches critiques à [Alice Martin, alice@company.com]
```

**Meilleurs exemples**
- **GitHub Copilot** — `@workspace`, `@file`, `#selection` dans Copilot Chat
- **Cursor** — `@file`, `@folder`, `@code`, `@docs` dans le prompt
- **Notion AI** — `@page` pour référencer d'autres documents
- **Linear** — `@issue` dans les commentaires avec preview inline

**Guide d'implémentation**

1. **Déclencheur** : `@` ouvre un autocomplete de sélection. Fuzzy search sur les noms.
2. **Types supportés** : définir les types mentionnables (fichiers, pages, utilisateurs, issues) avec des icônes distinctes.
3. **Preview inline** : au hover sur une mention résolue, afficher un preview du contenu référencé.
4. **Limite de contexte** : calculer la taille du contenu injecté et avertir si la fenêtre de contexte est dépassée.
5. **Rendu** : les mentions résolues s'affichent comme des chips (badge coloré avec nom) dans le champ de saisie.

**Pièges à éviter**

- ❌ Injection silencieuse sans que l'utilisateur sache ce qui est envoyé à l'API
- ❌ Pas de limite sur la taille du contexte injecté — dépasser la fenêtre de contexte casse la réponse
- ❌ Mentions qui ne se résolvent pas (affichent `@fichier` en texte brut) sans indication d'erreur
- ❌ Pas d'autocomplete — l'utilisateur doit connaître l'exact nom du fichier

---

## 30. Fil de conversation persistant

**Ce que c'est** — L'historique des échanges AI est sauvegardé par objet de travail (document, ticket, projet) et reste accessible à la reprise, sans avoir à redonner le contexte.

**Pourquoi ça marche**  
Le contexte est une ressource précieuse. Reconstruire le contexte à chaque session est un coût cognitif et temporel. Les fils persistants permettent des workflows itératifs sur plusieurs jours — "reprends notre discussion d'hier sur la spec".

**Démo**

```
Lundi :
👤 Aide-moi à rédiger la spec de ce ticket
🤖 Voici une première version...

Mercredi (retour sur le même ticket) :
[Historique visible en grisé]

👤 Reprends la spec et ajoute une section erreurs
🤖 [En utilisant le contexte de lundi...] Voici la version mise à jour...
```

**Meilleurs exemples**
- **Linear AI** — fil par ticket, persistant entre sessions
- **Intercom Fin** — historique de conversation par contact client
- **HubSpot Breeze** — fil AI par deal/contact dans le CRM
- **Notion AI** — historique par page de document

**Guide d'implémentation**

1. **Scope du fil** : définir l'unité de contexte (par document, par ticket, par utilisateur) selon les usages métier.
2. **Injection dans le contexte** : les N derniers messages du fil sont injectés en context dans chaque nouvelle requête (fenêtre glissante).
3. **Résumé automatique** : pour les longs fils, générer un résumé automatique à intégrer au contexte plutôt que les messages bruts (économie de tokens).
4. **Visibilité** : afficher l'historique avec timestamps et noms d'utilisateurs. Multi-utilisateurs si la collaboration est supportée.
5. **Effacement** : permettre d'effacer le fil pour repartir d'un contexte vierge.

**Pièges à éviter**

- ❌ Fil qui s'efface à la fermeture de la session
- ❌ Injecter tout l'historique sans limite — dépasse la fenêtre de contexte pour les longs fils
- ❌ Fil partagé entre utilisateurs sans contrôle d'accès
- ❌ Pas de moyen de voir ce qui a été injecté dans le contexte

---

## 31. Memory / préférences utilisateur

**Ce que c'est** — L'AI retient des faits sur l'utilisateur (préférences de style, contexte professionnel, informations récurrentes) entre sessions et les réutilise proactivement dans les réponses suivantes.

**Pourquoi ça marche**  
Élimine la répétition. L'utilisateur ne devrait pas avoir à réexpliquer son rôle, son style préféré, ou ses conventions à chaque conversation. La mémoire transforme l'AI d'un outil générique en assistant personnel.

**Démo**

```
Session 1 :
👤 Je suis CPO dans une startup SaaS B2B.
🤖 [mémorisation silencieuse]

Session 2 (semaine suivante) :
👤 Aide-moi à rédiger un email de relance client
🤖 [sans que l'user ait réexpliqué] Voici un email 
   adapté à un contexte B2B SaaS, avec un ton
   professionnel mais accessible...
```

**Meilleurs exemples**
- **ChatGPT Memory** — mémoire explicite avec liste visible et éditable
- **Claude** — mémoire avec projets et instructions personnalisées
- **Rewind** — mémoire basée sur l'historique de l'ordinateur
- **Mem.ai** — notes transformées en mémoire structurée

**Guide d'implémentation**

1. **Transparence** : toujours montrer à l'utilisateur ce qui est mémorisé. Une page "Mes mémoires" avec liste éditable est obligatoire.
2. **Contrôle** : l'utilisateur peut ajouter, modifier, supprimer des mémoires manuellement.
3. **Mémorisation** : deux modes possibles — automatique (l'AI détecte ce qui mérite d'être retenu) ou explicite ("Souviens-toi que...").
4. **Injection** : les mémoires pertinentes sont injectées dans le system prompt de chaque conversation.
5. **RGPD** : droit à l'effacement de toutes les mémoires, export en JSON, pas de partage entre utilisateurs.

**Pièges à éviter**

- ❌ Mémoire invisible — l'utilisateur ne sait pas ce que l'AI "sait" sur lui
- ❌ Mémorisation de données sensibles (passwords, numéros de carte) sans protection
- ❌ Mémoires qui influencent les réponses sans rapport avec la question
- ❌ Pas de moyen d'effacer toutes les mémoires d'un coup

---

## 32. Sources citées / grounding

**Ce que c'est** — Chaque affirmation factuelle de l'AI est liée à une source dans le contexte (document, page web, entrée de base de données), affichée sous forme de référence cliquable.

**Pourquoi ça marche**  
Les hallucinations sont le principal frein à l'adoption de l'AI en entreprise. Citer les sources permet à l'utilisateur de vérifier, renforce la confiance, et déplace la responsabilité : l'AI ne "sait" pas, elle "cite". Les réponses ancrées sont perçues comme plus fiables même si le contenu est identique.

**Démo**

```
🤖 Le délai de livraison standard est de 5 jours ouvrés [1].
   Les commandes express sont livrées en 24h [2].

   Sources :
   [1] Conditions générales de vente, section 4.2
   [2] FAQ Livraison Express → voir page
```

**Meilleurs exemples**
- **Perplexity** — références numérotées sur chaque affirmation, sources en sidebar
- **Bing Copilot** — citations inline avec hover preview de la source
- **Notion AI Q&A** — réponses ancrées dans le workspace avec lien vers la page source
- **Glean** — enterprise search avec sources d'entreprise citées

**Guide d'implémentation**

1. **Format de citation** : numérotation `[1]`, `[2]` inline dans le texte + liste de sources en bas. Chaque source cliquable.
2. **Hover preview** : au survol d'une citation, afficher un extrait de la source dans un tooltip.
3. **Prompt engineering** : instruire le modèle à citer ses sources avec un format structuré (JSON ou XML) pour un parsing fiable.
4. **RAG** : utiliser Retrieval-Augmented Generation — récupérer les chunks pertinents, les injecter dans le contexte, et demander au modèle de citer les IDs de chunks.
5. **Confiance** : si aucune source ne couvre la question, l'AI doit l'indiquer explicitement plutôt que d'improviser.

**Pièges à éviter**

- ❌ Citations inventées (hallucination de sources) — pire que l'absence de citation
- ❌ Sources non cliquables ou introuvables
- ❌ Citer des sources non pertinentes pour paraître "sourcé"
- ❌ Trop de citations pour une seule phrase — dégrade la lisibilité

---

---

# AI — Feedback & Contrôle

---

## 33. Thinking / reasoning visible

**Ce que c'est** — Le raisonnement intermédiaire du modèle (chain-of-thought) est affiché dans une zone collapsable avant la réponse finale, montrant les étapes de réflexion de l'AI.

**Pourquoi ça marche**  
Augmente massivement la confiance dans les réponses complexes. L'utilisateur peut voir si l'AI a bien compris la question, identifié les bons paramètres, et suivi une logique cohérente. Un raisonnement transparent est aussi plus facile à débugger et corriger.

**Démo**

```
🤖 [Réflexion en cours...]                ← collapsable
┌─────────────────────────────────────┐
│ Je dois analyser les ventes Q3.     │
│ Paramètres : période juillet-sept,  │
│ comparaison avec Q3 2023...         │
│ Je vois que les revenus ont crû de  │
│ 23% mais les marges ont baissé...   │
└─────────────────────────────────────┘

**Analyse des ventes Q3** : La croissance du
chiffre d'affaires (+23%) masque une pression
sur les marges due à...
```

**Meilleurs exemples**
- **Claude** — `<thinking>` blocks avec reasoning visible avant la réponse
- **ChatGPT o1** — "Thinking" collapsable avec durée estimée
- **Perplexity** — étapes de recherche et de raisonnement visibles
- **Gemini 2.0 Flash Thinking** — reasoning steps affichés

**Guide d'implémentation**

1. **Collapsable par défaut** : le thinking est replié par défaut pour ne pas noyer la réponse finale. L'utilisateur l'ouvre s'il veut inspecter.
2. **Streaming du thinking** : streamer le thinking en temps réel (même pattern que la réponse) pour donner le sentiment de "voir l'AI penser".
3. **Séparation visuelle** : le thinking doit être visuellement distinct de la réponse (fond différent, italique, icône différente).
4. **Durée** : afficher la durée du raisonnement ("Réfléchi 8 secondes") — informe sur l'effort fourni.
5. **Ne pas exposer sur les requêtes simples** : le thinking n'a de valeur que sur les questions complexes. Sur les requêtes simples, le masquer entièrement.

**Pièges à éviter**

- ❌ Thinking trop long qui noie la réponse
- ❌ Thinking ouvert par défaut — la réponse est ce que l'utilisateur cherche, pas le raisonnement
- ❌ Thinking identique visuellement à la réponse — confusion entre les deux
- ❌ Afficher le thinking sur toutes les réponses y compris les plus triviales

---

## 34. Regenerate + variantes

**Ce que c'est** — Après une réponse AI, l'utilisateur peut relancer la génération (même prompt, seed différente) ou demander plusieurs variantes affichées en parallèle pour choisir.

**Pourquoi ça marche**  
La génération AI est non déterministe. Une réponse insatisfaisante n'est pas forcément la "bonne" réponse — une autre seed peut donner quelque chose de bien meilleur. Le regenerate offre une seconde chance sans effort. Les variantes parallèles permettent une comparaison rapide pour les décisions créatives.

**Démo**

```
🤖 [Première réponse générée]

[↺ Régénérer]  [⊞ 3 variantes]  [👍]  [👎]

─────────────────────────────────────────

Variante A          Variante B          Variante C
──────────          ──────────          ──────────
Ton formel          Ton direct          Ton amical
[Utiliser]          [Utiliser]          [Utiliser]
```

**Meilleurs exemples**
- **ChatGPT** — bouton regenerate natif, navigation entre versions
- **Claude** — regenerate avec navigation ←/→ entre les générations
- **Midjourney** — 4 variantes systématiques, U/V buttons pour upscale/vary
- **v0** — 3 variantes de composant UI en parallèle

**Guide d'implémentation**

1. **Navigation entre versions** : conserver toutes les versions générées (1/3, 2/3, 3/3) avec navigation ←/→.
2. **Variantes** : limiter à 2–4 variantes simultanées. Plus = difficile à comparer.
3. **Paramètre de variante** : pour guider la variante, permettre d'ajouter une instruction ("Plus formel", "Plus concis").
4. **Coût visible** : si l'application a un modèle de crédit, indiquer le coût d'un regenerate avant de l'exécuter.
5. **Conserver le contexte** : le regenerate utilise exactement le même prompt et contexte — il ne "repose pas la question".

**Pièges à éviter**

- ❌ Regenerate qui efface la réponse précédente sans possibilité de la retrouver
- ❌ Variantes affichées sans possibilité de les comparer côte à côte
- ❌ Pas de way d'indiquer pourquoi on regénère (la prochaine génération devrait être différente)
- ❌ Regenerate gratuit illimité sur des modèles coûteux sans rate limiting

---

## 35. Agentic step tracker

**Ce que c'est** — Pour les tâches longues exécutées par un agent autonome, un fil d'étapes affiche en temps réel ce que l'agent est en train de faire, avec un bouton Stop accessible à tout moment.

**Pourquoi ça marche**  
Un agent autonome qui "disparaît" pendant 30 secondes est anxiogène. L'utilisateur ne sait pas si c'est en train de fonctionner, bloqué, ou en train de faire quelque chose d'indésirable. Le step tracker maintient la confiance par la transparence totale sur les actions en cours.

**Démo**

```
🤖 Agent en cours...                    [⏹ Arrêter]

✅ Lecture du ticket #1234              2s
✅ Analyse des issues similaires        5s
⚙️  Rédaction de la solution...        ← en cours
⏳ Tests unitaires                      en attente
⏳ Création du PR                       en attente

[██████████░░░░░░░░░░] 45%
```

**Meilleurs exemples**
- **Devin** — step tracker complet avec logs détaillés par étape
- **Claude Code** — affichage des outils utilisés (read, write, bash) en temps réel
- **Replit Agent** — steps avec détail des fichiers modifiés
- **OpenAI Operator** — actions navigateur affichées étape par étape

**Guide d'implémentation**

1. **Granularité** : afficher des étapes métier (Lecture du ticket, Analyse, Rédaction) plutôt que des étapes techniques (HTTP GET /api/issues/1234). L'utilisateur n'est pas un développeur.
2. **États des étapes** : ✅ Terminé / ⚙️ En cours / ⏳ En attente / ❌ Erreur.
3. **Stop immédiat** : le bouton Stop doit interrompre l'agent sans délai. Utiliser des abort controllers ou des signaux d'annulation.
4. **Rollback sur stop** : définir clairement ce qui se passe si l'utilisateur arrête — les actions déjà effectuées sont-elles annulées ? L'informer.
5. **Logs détaillés** : les étapes techniques complètes disponibles dans un panneau collapsable pour les utilisateurs avancés.

**Pièges à éviter**

- ❌ Pas de bouton Stop — l'utilisateur est captif
- ❌ Steps trop granulaires (log de chaque appel HTTP) — illisible
- ❌ Progress bar sans estimation de temps — l'utilisateur ne sait pas combien de temps attendre
- ❌ Agent qui modifie des données en production sans confirmation préalable

---

## 36. Confidence / uncertainty signal

**Ce que c'est** — L'interface signale visuellement quand l'AI est peu confiante dans sa réponse — badge, nuance de couleur, disclaimer inline — au lieu d'afficher toutes les réponses avec la même assurance visuelle.

**Pourquoi ça marche**  
Une AI qui présente ses incertitudes avec la même confiance que ses certitudes est dangereuse. Signaler l'incertitude permet à l'utilisateur d'adapter son niveau de vérification. C'est aussi plus honnête — et la transparence sur les limites augmente la confiance globale dans le système.

**Démo**

```
Confiance élevée :
🤖 Le prix standard est 29€/mois. [📄 Grille tarifaire]

Confiance faible :
🤖 ⚠️ Je ne suis pas certain, mais je pense que
   la fonctionnalité X est disponible en plan Pro.
   [Vérifier dans la documentation]
   
Hors contexte :
🤖 ℹ️ Cette question dépasse mon contexte actuel.
   Je ne peux pas y répondre de manière fiable.
```

**Meilleurs exemples**
- **Perplexity** — distinction claire entre informations sourcées et inférences
- **Bing Copilot** — disclaimer sur les informations non vérifiables
- **Harvey AI** — niveaux de confiance sur les analyses juridiques
- **Glean** — score de pertinence des sources enterprise

**Guide d'implémentation**

1. **Niveaux de confiance** : définir 3 niveaux (Haute / Moyenne / Faible) avec représentation visuelle distincte pour chacun.
2. **Détection** : côté modèle, utiliser le log-probability des tokens ou demander explicitement au modèle d'évaluer sa confiance dans le prompt.
3. **Ton** : sur les réponses incertaines, changer le ton linguistique ("je pense que", "il me semble") en plus du signal visuel.
4. **Redirection** : toujours proposer une alternative (lien vers la doc, suggestion de vérifier, contact humain) sur les réponses incertaines.
5. **Pas de confiance par défaut** : ne pas afficher un badge "Haute confiance" systématiquement — c'est aussi trompeur que pas de signal du tout.

**Pièges à éviter**

- ❌ Signaler la faible confiance mais quand même donner la "réponse" de manière assertive
- ❌ Trop de warnings — si tout est marqué incertain, le signal perd sa valeur
- ❌ Confidence score affiché en chiffre (72%) sans calibration — les utilisateurs surinterpètent les chiffres précis
- ❌ Pas de lien vers une source plus fiable sur les réponses incertaines

---

---

# AI — Prompt UX

---

## 37. Suggested prompts / quick actions

**Ce que c'est** — L'état vide de l'interface chat est rempli de suggestions contextuelles cliquables, adaptées à l'objet de travail actuel, qui permettent de démarrer sans effort.

**Pourquoi ça marche**  
La page blanche est le principal obstacle à l'adoption. "Comment est-ce que je commence ?" est la question que pose chaque nouvel utilisateur. Les suggestions contextuelles répondent directement à cette question avec des actions immédiatement utiles — pas des exemples génériques.

**Démo**

```
[Interface AI vide, contexte : ticket de bug]

                   ✨ AI Assistant

    Que puis-je faire pour vous ?

    ┌──────────────────────────────────────┐
    │ 📝 Rédiger les étapes de reproduc.  │
    │ 🔍 Trouver des issues similaires    │
    │ ✅ Générer des critères d'acceptance │
    │ 🧪 Écrire des cas de test          │
    └──────────────────────────────────────┘

    [Écrire une instruction...          ↑]
```

**Meilleurs exemples**
- **ChatGPT** — suggestions contextuelles renouvelées à chaque session
- **Claude** — suggestions adaptées au type de conversation
- **Copilot Chat** — suggestions liées au fichier ouvert dans VS Code
- **Notion AI** — suggestions liées au type de document

**Guide d'implémentation**

1. **Contextualisation** : les suggestions doivent changer selon l'objet actif (ticket, document, contact, code). Pas les mêmes 4 suggestions partout.
2. **Nombre** : 3–6 suggestions. Trop peu = pas assez de choix, trop = paralysie de décision.
3. **Format** : icône + label court (5–7 mots max). Le label doit être un verbe d'action.
4. **Clic = prompt exécuté** : cliquer sur une suggestion doit directement lancer la requête, pas remplir le champ de saisie.
5. **Refresh** : bouton "Autres suggestions" pour voir des alternatives si aucune ne convient.

**Pièges à éviter**

- ❌ Suggestions génériques identiques dans tous les contextes
- ❌ Suggestions trop longues qui ne rentrent pas dans le bouton
- ❌ Clic qui remplit le champ mais ne soumet pas — étape supplémentaire inutile
- ❌ Suggestions disparaissant après le premier message — les réafficher quand le champ est vide

---

## 38. Prompt templates

**Ce que c'est** — Bibliothèque de prompts pré-écrits, personnalisables et partageables, que l'utilisateur ou l'équipe peut créer pour standardiser les usages récurrents de l'AI.

**Pourquoi ça marche**  
Le prompt engineering est une compétence rare. Les templates permettent aux utilisateurs avancés de créer des prompts efficaces une fois, et à tout le monde de les utiliser ensuite. Standardise les usages, maintient la qualité, et réduit le temps par tâche.

**Démo**

```
Bibliothèque de templates (partagée par équipe) :

📁 Commercial
   └ Email de relance client        [Utiliser] [Modifier]
   └ Synthèse d'appel de vente      [Utiliser] [Modifier]

📁 Produit  
   └ Rédaction de user story        [Utiliser] [Modifier]
   └ Analyse de feedback utilisateur[Utiliser] [Modifier]

[+ Créer un template]

─────────────────────────────

Template "Rédaction de user story" :
En tant que {{persona}}, je veux {{action}}
afin de {{bénéfice}}.

Contexte : {{contexte_du_ticket}}

Variables à remplir avant envoi :
[persona      ] [action       ] [bénéfice      ]
```

**Meilleurs exemples**
- **HubSpot** — templates AI par équipe (Sales, Marketing, Support)
- **Salesforce Einstein** — prompt templates par rôle métier
- **PromptLayer** — gestion et versioning de templates en équipe
- **Dust** — templates avec variables et workflows

**Guide d'implémentation**

1. **Variables** : supporter des variables `{{variable}}` que l'utilisateur remplit avant l'envoi.
2. **Scope** : templates personnels vs partagés par équipe vs globaux (admin).
3. **Versioning** : historique des modifications d'un template avec possibilité de rollback.
4. **Catégorisation** : dossiers ou tags pour organiser les templates par équipe ou cas d'usage.
5. **Métriques** : tracking d'utilisation — quels templates sont les plus utilisés, quels résultats.

**Pièges à éviter**

- ❌ Templates sans variables — l'utilisateur doit tout réécrire à la main
- ❌ Templates uniquement personnels — la valeur est dans le partage d'équipe
- ❌ Pas de possibilité de prévisualiser le template avant utilisation
- ❌ Templates trop longs et complexes — les plus utilisés sont les plus simples

---

## 39. Multimodal drop zone

**Ce que c'est** — La zone de saisie du chat accepte texte, images, PDF, audio, et autres fichiers — avec indication claire des types acceptés, prévisualisation des fichiers joints, et traitement adapté à chaque type.

**Pourquoi ça marche**  
Les utilisateurs pensent en termes de problème, pas de type de données. "Regarde ce screenshot et dis-moi ce qui ne va pas" est plus naturel que "voici du texte décrivant un screenshot". La multimodalité supprime la traduction mentale et permet des requêtes plus directes.

**Démo**

```
┌─────────────────────────────────────────┐
│                                         │
│         Glissez vos fichiers ici        │
│    ou cliquez pour parcourir            │
│                                         │
│    📷 Images  📄 PDF  🎵 Audio  📊 CSV  │
│                                         │
└─────────────────────────────────────────┘

Après upload :
┌─────────────────────────────────────────┐
│ 🖼️ screenshot-bug.png  ×               │
│ 📄 rapport-q3.pdf      ×               │
│ ─────────────────────────────────────  │
│ [Que vois-tu dans ces fichiers ?    ↑] │
└─────────────────────────────────────────┘
```

**Meilleurs exemples**
- **ChatGPT** — images, PDF, CSV, code files
- **Claude** — images, PDF, documents texte
- **Gemini** — images, vidéo, audio, PDF
- **Copilot** — images et documents Office

**Guide d'implémentation**

1. **Drag & drop** : écouter `dragover` et `drop` sur toute la zone de chat, pas seulement l'input.
2. **Types supportés** : définir clairement les types MIME acceptés et afficher un message d'erreur clair pour les types non supportés.
3. **Preview** : thumbnail pour les images, icône + nom + taille pour les autres fichiers.
4. **Limite de taille** : définir une limite et l'afficher avant upload. Message d'erreur clair si dépassée.
5. **Multiple files** : permettre plusieurs fichiers simultanément avec possibilité de supprimer individuellement.
6. **Traitement côté serveur** : les fichiers sont uploadés vers un storage sécurisé, pas envoyés directement à l'API du modèle en base64 (trop lent, trop lourd).

**Pièges à éviter**

- ❌ Types de fichiers acceptés non indiqués avant l'upload
- ❌ Erreur générique "Fichier non supporté" sans préciser pourquoi
- ❌ Upload bloquant l'interface pendant le transfert
- ❌ Fichiers conservés indéfiniment sans politique de rétention

---

## 40. Mode voix natif

**Ce que c'est** — Interface conversationnelle vocale intégrée nativement : l'utilisateur parle, l'AI répond à voix haute, avec visualisation de la parole, détection de fin de phrase, et streaming audio de la réponse.

**Pourquoi ça marche**  
Certains contextes sont incompatibles avec la frappe : mains occupées, déplacement, pensée à voix haute. Le mode voix natif n'est pas un simple STT (Speech-to-Text) converti en texte — c'est un mode d'interaction complet avec ses propres conventions. Il ouvre l'AI à des cas d'usage impossibles en texte.

**Démo**

```
[Mode voix actif]

     🎤
   ╭─────╮
   │ ~~~ │  ← visualisation de la voix (waveform)
   ╰─────╯

Vous : "Résume les points clés du dernier meeting"

          ●●● [AI réfléchit]

AI : [audio streamé] "Lors du dernier meeting,
      trois points principaux ont été abordés..."

[Retranscription visible en sous-texte]
[⏸ Pause]  [🔁 Rejouer]  [📝 Voir en texte]
```

**Meilleurs exemples**
- **ChatGPT Advanced Voice** — référence : voix naturelle, interruption possible, émotions
- **Claude** — mode voix avec réponse audio naturelle
- **Gemini Live** — voix temps réel avec multimodalité (peut voir l'écran)
- **Pi (Inflection)** — voix comme mode d'interaction principal

**Guide d'implémentation**

1. **VAD (Voice Activity Detection)** : détecter automatiquement la fin de la phrase plutôt que d'utiliser un bouton "Arrêter". Librairies : `@ricky0123/vad-web`, Silero VAD.
2. **Streaming audio** : la réponse audio commence à jouer pendant que l'AI génère encore — même principe que le streaming texte.
3. **Interruption** : l'utilisateur peut interrompre l'AI en parlant. Détecter la voix pendant la lecture audio et couper.
4. **Transcription visible** : toujours afficher la transcription texte en parallèle (accessibilité + vérification).
5. **Bascule voix/texte** : permettre de passer du mode voix au mode texte sans perdre l'historique de conversation.
6. **WebRTC ou WebAudio API** : pour les applications browser. Gérer les permissions micro avec un fallback gracieux si refusé.

**Pièges à éviter**

- ❌ Simple bouton "Enregistrer → Envoyer" sans streaming — perçu comme basique et lent
- ❌ Pas de VAD — l'utilisateur doit appuyer sur un bouton pour terminer sa phrase
- ❌ Réponse audio sans transcription — inaccessible
- ❌ Pas de gestion du bruit ambiant — performances dégradées dans les open spaces
- ❌ Mode voix qui coupe la voix de l'AI quand l'utilisateur commence à parler sans transition douce

---

---

## Conclusion

Ces 40 patterns constituent le socle de l'interface SaaS moderne. Ils ne sont pas des règles rigides mais des **solutions éprouvées à des problèmes récurrents**.

### Principes transversaux

**Persistance** — Les préférences, états, filtres et historiques doivent survivre au refresh et être retrouvés sur n'importe quel appareil. La perte d'état est la source de frustration la plus fréquente.

**Accessibilité clavier** — Chaque pattern doit fonctionner intégralement au clavier. Tab, Échap, Enter, et les raccourcis standards sont des contrats avec l'utilisateur.

**Performance perçue** — Skeleton screens, optimistic UI, streaming : l'objectif n'est pas d'être rapide, c'est d'*être perçu* comme rapide. Les deux ne sont pas identiques.

**Transparence de l'AI** — Pour les patterns AI, la règle d'or est : l'utilisateur doit toujours savoir ce que l'AI fait, avec quelles données, et avec quelle confiance. L'opacité génère de la méfiance.

**Contrôle utilisateur** — Stop buttons, undo, diff view, reject : chaque pattern AI doit donner à l'utilisateur le dernier mot. L'AI propose, l'humain dispose.

---

*Guide maintenu par la communauté — contributions bienvenues.*
