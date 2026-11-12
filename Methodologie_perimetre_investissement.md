# JEVONS Actions Monde — Méthodologie complète du périmètre d'investissement

*Holocène AM · Projet final Finance durable · Université Paris-Dauphine · 2026*

> **Faire moins, pas seulement mieux.**

Ce document explique, étape par étape, **comment on passe des 1 247 entreprises du MSCI World aux 404 entreprises qui ont le droit d'entrer dans le fonds**. C'est notre **périmètre d'investissement**. Pour chaque règle, on donne **le seuil, la donnée utilisée, ce qu'elle mesure et pourquoi on l'a choisie**.

**Sommaire**
1. Le fonds en bref
2. Les données utilisées : lexique
3. L'entonnoir en un coup d'œil
4. Étape A : ce qu'on refuse (A1 à A4)
5. Étape B : le test « investissement durable » (Article 9)
6. La revue qualitative
7. Notre périmètre d'investissement
8. Nos seuils : strict ou souple ?
9. Les limites que nous assumons
10. Sources et code

---

## 1. Le fonds en bref

| | |
|---|---|
| **Société de gestion** | **Holocène AM**. L'Holocène est l'époque de climat stable dans laquelle vit l'humanité depuis environ 11 700 ans. Notre mission : investir pour que l'économie reste dans les limites qui garantissent cette stabilité. |
| **Fonds** | **JEVONS Actions Monde**. Il porte le nom du paradoxe de Jevons (1865) : plus une technologie devient efficace, plus on la consomme. C'est l'effet rebond. |
| **Forme** | FCP de droit français, OPCVM (UCITS), actions monde, long only, sans levier, liquidité quotidienne |
| **Classification** | SFDR **Article 9.3** : objectif de réduction des émissions de carbone, avec un indice Paris-Aligned |
| **Indice de référence** | MSCI World Climate Paris Aligned |
| **Univers de départ** | MSCI World au 31/12/2024 : **1 247 entreprises** (`all_data.csv`) |

### L'objectif d'investissement durable (Article 9)

> *Le fonds a pour objectif d'investissement durable de contribuer à réduire la pression de l'économie sur les **limites planétaires**, en investissant dans des entreprises qui contribuent de manière mesurable à l'atténuation du changement climatique, à la protection des ressources en eau ou à l'économie circulaire, sans porter atteinte de manière significative aux autres limites, notamment la biodiversité.*

Les **limites planétaires** (Rockström et al., 2009, mises à jour en 2023) sont les 9 seuils à ne pas dépasser pour que la Terre reste aussi stable qu'à l'Holocène. **7 sur 9 sont déjà dépassées.** Le fonds en suit 4, celles que nos données permettent de mesurer :

| Limite planétaire | Rôle dans le fonds | Mesure (données MSCI) |
|---|---|---|
| 🌡️ Climat | Contribution | ODD 13, ODD 7, température implicite, intensité carbone |
| 💧 Eau douce | Contribution | ODD 6 |
| ♻️ Ressources et pollution (« nouvelles entités ») | Contribution | ODD 12, part de chiffre d'affaires vert |
| 🌿 Biodiversité (« intégrité de la biosphère ») | Garde-fou : ne pas nuire | ODD 14, ODD 15 |

### Nos deux règles d'or

> 1. **Sur l'environnement, on suit notre thème et on est exigeants. Sur le social et la gouvernance, on applique uniquement le minimum exigé pour un Article 9.**
> 2. **On n'investit pas dans ce qu'on ne mesure pas.**

### Pourquoi l'Article 9.3, aligné avec l'Accord de Paris

L'Article 9 n'impose pas d'être aligné avec Paris. Nous le faisons quand même, pour 5 raisons :
1. **Crédibilité :** un fonds « limites planétaires » qui détiendrait Glencore, l'un des plus gros mineurs de charbon du monde, serait indéfendable, même si c'est légal.
2. **Attentes du marché :** le label ISR et la plupart des investisseurs exigent de toute façon l'exclusion des énergies fossiles.
3. **Anticipation :** la réforme SFDR 2.0, proposée fin 2025, prévoit d'imposer ces exclusions à tous les fonds « durables ».
4. **Coût quasi nul :** il suffit de quelques vérifications en plus.
5. **Un chiffre fort :** au moins 50 % de carbone en moins que le marché.

---

## 2. Les données utilisées : lexique

### Les scores ODD (Objectifs de développement durable) de MSCI

L'ONU a fixé **17 Objectifs de développement durable (ODD, ou SDG en anglais)** pour 2030. MSCI note chaque entreprise sur chacun des 17. Le **score net d'alignement** va de **−10 à +10**. Il combine deux choses :
- **ce que l'entreprise vend** : ses produits aident-ils ou nuisent-ils à l'objectif ?
- **comment elle fonctionne** : ses politiques, ses pratiques, ses objectifs.

| Score | Catégorie MSCI | Notre usage |
|---|---|---|
| ≥ 5 | Fortement aligné | |
| **≥ 2** | **Aligné** | **Seuil de contribution** (étape B) |
| entre −2 et 2 | Neutre | |
| **≤ −2** | **Désaligné** | **Seuil « nuit »** (étape B, DNSH) |
| **≤ −5** | **Fortement désaligné** | **Seuil d'exclusion** (étape A4) |

**Les 6 ODD environnementaux que nous utilisons :**

| ODD | Intitulé officiel | Ce que ça veut dire pour une entreprise | Colonne |
|---|---|---|---|
| **ODD 6** | Eau propre et assainissement | Économiser, traiter ou distribuer l'eau, ne pas la polluer | `SDG_06_NET_ALIGNMENT_SCORE` |
| **ODD 7** | Énergie propre et d'un coût abordable | Produire, distribuer ou permettre une énergie renouvelable et efficace | `SDG_07_NET_ALIGNMENT_SCORE` |
| **ODD 12** | Consommation et production responsables | Économie circulaire, recyclage, moins de déchets et de matières | `SDG_12_NET_ALIGNMENT_SCORE` |
| **ODD 13** | Lutte contre les changements climatiques | Réduire ses émissions, vendre des solutions bas carbone | `SDG_13_NET_ALIGNMENT_SCORE` |
| **ODD 14** | Vie aquatique | Ne pas dégrader les océans (pêche, plastiques, pollution) | `SDG_14_NET_ALIGNMENT_SCORE` |
| **ODD 15** | Vie terrestre | Ne pas détruire les forêts, les sols, la biodiversité | `SDG_15_NET_ALIGNMENT_SCORE` |

*Les 11 autres ODD (pauvreté, santé, éducation, égalité…) sont des ODD sociaux. Ils ne font pas partie de notre thème.*

### Les autres données

| Donnée | Ce qu'elle mesure | Unité / échelle | Colonne |
|---|---|---|---|
| **Température implicite (ITR)** | Le réchauffement en 2100 **si toute l'économie se comportait comme cette entreprise**, au vu de ses émissions (scopes 1, 2 et 3) et de ses objectifs. 1,5 °C = aligné avec Paris | °C (de 1,3 à 10 dans nos données) | `ITR` |
| **Intensité carbone, scope 1** | Émissions **directes** : usines, véhicules, chaudières | tCO2e par M$ de chiffre d'affaires | `INTENSITY_SCOPE_1` |
| **Intensité carbone, scope 2** | Émissions de l'**électricité et de la chaleur achetées** | tCO2e par M$ | `INTENSITY_SCOPE_2` |
| **Intensité carbone, scope 3** | Émissions de **toute la chaîne de valeur** : fournisseurs, transport, **usage des produits vendus** | tCO2e par M$ | `INTENSITY_SCOPE_3` |
| **Chiffre d'affaires « technologies propres »** | Part du chiffre d'affaires dans les énergies alternatives, l'efficacité énergétique, les bâtiments verts, la prévention de la pollution, l'eau et l'agriculture durables | % | `CT_TOTAL_MAX_REV` |
| **Chiffre d'affaires Taxonomie UE** | Part estimée du chiffre d'affaires alignée avec la **Taxonomie européenne** (la liste officielle des activités « vertes ») | % | `EST_EU_TAXONOMY_MAX_REV` |
| **Chiffre d'affaires vert** *(notre calcul)* | Le plus élevé des deux précédents | % | max des deux |
| **Score de controverse** | La gravité des scandales récents de l'entreprise (pollution, accidents, procès…) | de 0 à 10 : **0 = 🔴 rouge** (très grave), **1 = 🟠 orange** (grave), 2 à 4 = 🟡 jaune, 5 à 10 = 🟢 vert | `ENVIRONMENT_`, `SOCIAL_`, `GOVERNANCE_CONTROVERSY_SCORE` |
| **Note de pilier gouvernance** | La qualité de la gouvernance : conseil d'administration, rémunérations, éthique, fiscalité | de 0 à 10 | `GOVERNANCE_PILLAR_SCORE` |
| **Note ESG globale** | La note ESG de MSCI | de CCC à AAA | `IVA_COMPANY_RATING` |
| **Tabac** | L'entreprise produit-elle du tabac ? | oui / non | `TOB_PRODUCER` |
| **Armes controversées** | Liens avec les mines antipersonnel, les armes à sous-munitions, chimiques ou biologiques | oui / non | `CWEAP_TIE` |
| **Secteur et industrie** | La classification GICS (11 secteurs) et le groupe d'industrie | texte | `gics_sector_name`, `industry_group` |

### Les bases externes (ce que MSCI ne voit pas)

| Base | Ce qu'elle apporte | Utilisée en |
|---|---|---|
| **Global Coal Exit List 2026** (urgewald) | Part du chiffre d'affaires issue du **charbon thermique** pour ~3 000 entreprises | A1 |
| **Global Coal Mine Tracker**, août 2026 (Global Energy Monitor) | Chaque mine de charbon du monde, avec ses **propriétaires** et leur part | A1 |
| **Banking on Climate Chaos 2026** et trackers Reclaim Finance | Financements fossiles et politiques des 65 plus grandes banques | A2 (justification) |

---

## 3. L'entonnoir en un coup d'œil

```
1 247  entreprises du MSCI World (31/12/2024)
  │
  │  ÉTAPE A · CE QU'ON REFUSE
  │  ├─ A1  Énergies fossiles ........................... − 115
  │  ├─ A2  Financement des énergies fossiles ........... − 183
  │  ├─ A3  Effet rebond (Jevons) 🎯 ..................... −  49
  │  └─ A4  Garde-fous ................................... −  59
  ▼
  841  entreprises investissables
  │
  │  ÉTAPE B · TEST « INVESTISSEMENT DURABLE » (Article 9)
  │  ├─ Case 1  Contribue à une limite planétaire ?
  │  ├─ Case 2  Ne nuit pas aux autres ?
  │  └─ Case 3  Gouvernance minimale ? ................... − 437
  ▼
  404  entreprises éligibles  =  NOTRE PÉRIMÈTRE
```

*Les exclusions sont comptées dans l'ordre A1 → A4 : une entreprise exclue pour plusieurs motifs n'est comptée qu'une fois, dans la première famille qui l'exclut.*

---

## 4. Étape A — Ce qu'on refuse

On retire d'emblée ce qui est incompatible avec le fonds, **avant même de regarder ce que l'entreprise apporte**.

### A1. Les énergies fossiles — 115 exclues *(obligatoire en Article 9.3)*

Le règlement Paris-Aligned (règlement délégué UE 2020/1818, art. 12) impose d'exclure les entreprises qui tirent **≥ 1 % de leur chiffre d'affaires du charbon**, **≥ 10 % du pétrole**, **≥ 50 % du gaz**, ou **≥ 50 % d'une électricité émettant plus de 100 gCO2e/kWh**.

| Règle | Seuil | Donnée | Pourquoi ce seuil | Exclues |
|---|---|---|---|---|
| ⛽ **Pétrole et gaz** | Tout le secteur, sans seuil | `gics_sector_name` = Energy | **Plus strict** que la règle officielle (10 % / 50 %) : nos données n'ont pas la part de chiffre d'affaires pétrole et gaz, et un fonds « limites planétaires » ne garde aucun pétrolier | 52 |
| 🏭 **Électricité carbonée** | Un électricien est **gardé** seulement si : chiffre d'affaires vert **≥ 50 %**, **ou** scope 1 **< 100 tCO2e par M$** | `CT_TOTAL_MAX_REV`, `EST_EU_TAXONOMY_MAX_REV`, `INTENSITY_SCOPE_1` | **Approximation** de la règle officielle en gCO2/kWh, une donnée absente de notre base. Le seuil de 100 laisse passer les réseaux et l'eau, qui émettent peu | 51 |
| ⚫ **Charbon thermique** | **≥ 1 %** du chiffre d'affaires | Global Coal Exit List 2026 | **Seuil officiel** Paris-Aligned. Nos données MSCI n'ont **aucune colonne charbon** | 4 |
| ⛏️ **Mines de charbon**, thermique **et métallurgique** | Détenir **≥ 10 %** d'une mine **en exploitation**, produisant **> 0,5 Mt/an** | Global Coal Mine Tracker | Notre choix. La GCEL ne couvre pas le charbon métallurgique (pour l'acier). Le seuil de 10 % écarte les participations symboliques | 8 |

**Qui tombe grâce aux bases charbon (12 entreprises) :**
- **GCEL :** Glencore (3,2 % du CA, 98 Mt/an), BHP (3,2 %), CSX (13 %, transport de charbon), Berkshire Hathaway (1,7 %, centrales et transport).
- **Global Coal Mine Tracker :** Anglo American (88 % des mines Grosvenor et Moranbah North), Mitsubishi Corp (50 % des mines BMA), Mitsui & Co, ITOCHU, Sumitomo Corp, Marubeni, Nippon Steel, JFE.

**Pourquoi c'était nécessaire :** les miniers de charbon ne sont **pas** dans le secteur Énergie. Ils sont classés en Matériaux (Glencore, BHP, Anglo American) ou en Industrie (les maisons de commerce japonaises). Sans ces bases, **ITOCHU et Sumitomo**, deux propriétaires de mines de charbon, seraient entrées dans le fonds.

**Bon à savoir :** South32 n'est **pas** exclue. Elle a **vendu** ses mines de charbon d'Illawarra. Croiser plusieurs sources évite d'exclure une entreprise qui a déjà changé.

### A2. Le financement des énergies fossiles — 183 exclues

| Règle | Seuil | Donnée | Exclues |
|---|---|---|---|
| 🏦 Banques | Tout le groupe d'industrie | `industry_group` = Banks | 74 |
| 🛡️ Assureurs et courtiers | Tout le groupe | `industry_group` = Insurance | 64 |
| 📈 Gestionnaires d'actifs, crédit, capital-investissement, holdings | Tout le secteur Financials, sauf l'exception ci-dessous | `gics_sector_name` = Financials | 45 |

**Pourquoi :** une banque ou un assureur pollue peu lui-même, mais **finance, assure ou détient** des entreprises fossiles. En 2025, les 65 plus grandes banques du monde ont financé **906 milliards de dollars** d'énergies fossiles (*Banking on Climate Chaos 2026*). Pourtant, nos données donnent à Goldman Sachs une intensité carbone scope 3 de **0,7 tCO2e par M$**, contre 494 en médiane pour l'industrie. **MSCI mesure leurs bureaux, pas leurs prêts.**

Plutôt que de faire confiance à un chiffre faux, nous les excluons : **on n'investit pas dans ce qu'on ne mesure pas.**

**L'exception :** on garde les **services de paiement, les bourses et les agences de notation** (Visa, Mastercard, American Express, PayPal, S&P Global, Moody's, Deutsche Börse, Nasdaq…). Elles se rémunèrent par commission et ne financent pas d'entreprises.

### A3. L'effet rebond (Jevons) — 49 exclues 🎯

| Activité | Qui | Donnée | Exclues |
|---|---|---|---|
| ✈️ Aérien | Toutes les compagnies aériennes, et **Amadeus** (réservation de billets d'avion, dont le chiffre d'affaires grandit avec le nombre de vols) | `industry_group` = Airlines, et liste | 8 |
| 🚢 Croisières | Carnival, Royal Caribbean | Liste | 3 |
| 🚗 Automobile, **électrique comprise** | Constructeurs et équipementiers | `industry_group` = Auto Manufacturers, Auto Parts&Equipment | 34 |
| 👕 Fast fashion | Inditex (Zara), H&M, Fast Retailing (Uniqlo), Associated British Foods (Primark) | Liste | 4 |

**Pourquoi :** les avions consomment moins par passager, mais on vole toujours plus. Les voitures sont plus propres, mais le parc automobile grossit. Les vêtements sont moins chers à produire, donc on en achète toujours plus. **L'efficacité ne compense pas la hausse des volumes.**

**Pourquoi une liste et pas une donnée :** les notes ESG mesurent l'**efficacité** (émissions par produit), pas le **volume**. Sans cette exclusion, Zara passerait tous nos autres filtres. Nous assumons une limite : presque toute activité crée un peu d'effet rebond. Nous excluons uniquement les activités où il est **le moteur du modèle économique**.

**Une liste fixe, sans suivi :** comme pour le tabac, l'exclusion se vérifie avec le groupe d'industrie et quelques noms. Il n'y a ni score ni surveillance, juste une règle appliquée à chaque révision du portefeuille. Les autres activités, comme l'IA, passent par nos critères environnementaux habituels : leur rebond porte sur l'électricité, qui peut être décarbonée, contrairement au kérosène.

### A4. Les garde-fous — 59 exclues

| Famille | Règle et seuil | Donnée | Pourquoi ce seuil | Exclues (brut) |
|---|---|---|---|---|
| 🔴🟠 **Controverses environnementales** | Score **≤ 1** (rouge ou orange) | `ENVIRONMENT_CONTROVERSY_SCORE` | **Strict, notre thème :** beaucoup de fonds n'excluent que le rouge. Exemples : Coca-Cola, Nestlé, Bayer | 28 |
| 🔴 **Controverses sociales et de gouvernance** | Score **= 0** (rouge seulement) | `SOCIAL_` et `GOVERNANCE_CONTROVERSY_SCORE` | **Minimum Article 9 :** c'est notre approximation des violations du Pacte mondial de l'ONU et des principes de l'OCDE, que le règlement Paris-Aligned impose d'exclure | 2 |
| 🚬 **Tabac** | Toute production | `TOB_PRODUCER` | Obligatoire en Paris-Aligned | 5 |
| 💣 **Armes controversées** | Tout lien | `CWEAP_TIE` | Obligatoire en Paris-Aligned | 5 |
| 🌿 **Atteinte grave à la biodiversité** | ODD 14 **ou** ODD 15 **≤ −5** | `SDG_14`, `SDG_15` | Seuil MSCI « fortement désaligné » | 13 |
| 💧♻️ **Atteinte grave à l'eau ou aux ressources** | ODD 6 **ou** ODD 12 **≤ −5** | `SDG_06`, `SDG_12` | Seuil MSCI « fortement désaligné » | 72 |
| 🔍 **Atteintes invisibles dans les données** | **Or** (mines, sociétés de redevances, bijouterie) et **saumon d'élevage en mer** | Liste issue de la revue qualitative (voir section 6) | Newmont, Barrick, Agnico Eagle, Northern Star, Franco-Nevada, Wheaton Precious Metals, Chow Tai Fook, Mowi, SalMar | 9 |
| ❓ **Données manquantes** | Pas de note ESG, de température implicite ou d'intensité scope 1 | `IVA_COMPANY_RATING`, `ITR`, `INTENSITY_SCOPE_1` | **On n'investit pas dans ce qu'on ne mesure pas** | 14 |

*Les chiffres « brut » se recoupent avec les familles précédentes : au total, 59 entreprises sont exclues **uniquement** par ces garde-fous.*

**→ Résultat de l'étape A : 406 entreprises exclues, 841 investissables.**

---

## 5. Étape B — Le test « investissement durable » (Article 9)

Pour un Article 9, **chaque** entreprise du fonds doit être un **investissement durable** au sens de l'**article 2.17 de SFDR**. La définition a trois conditions : **contribuer** à un objectif environnemental ou social, **ne pas nuire significativement** aux autres objectifs (le principe **DNSH**, « Do No Significant Harm »), et appliquer des **pratiques de bonne gouvernance**. C'est un examen en oui ou non : il faut cocher **les 3 cases**.

### Case 1 — Elle contribue à au moins une limite planétaire

Il suffit d'**une** de ces 5 « portes d'entrée » :

| Porte d'entrée | Seuil | Ce que ça veut dire | Entreprises |
|---|---|---|---|
| 🌡️ Climat | ODD 13 **≥ 2** | MSCI juge l'entreprise « alignée » avec la lutte contre le changement climatique | 292 |
| ⚡ Énergie propre | ODD 7 **≥ 2** | Elle aide la transition énergétique | 258 |
| 💧 Eau | ODD 6 **≥ 2** | Elle aide à préserver ou à fournir l'eau | 133 |
| ♻️ Ressources | ODD 12 **≥ 2** | Elle aide la sobriété et l'économie circulaire | 222 |
| ♻️ Solutions vertes | Chiffre d'affaires vert **≥ 20 %** | Au moins un cinquième de ce qu'elle vend est une solution environnementale (technologies propres ou Taxonomie UE) | 59 |

→ **486 entreprises** contribuent.

**Pourquoi 2 et 20 % :** 2 est le seuil MSCI de l'« alignement ». 20 % est un seuil courant du marché, qui va de 20 à 50 %. Ces seuils sont **plutôt souples** : ils disent qui a le droit d'entrer, et le classement de l'étape suivante favorisera celles qui contribuent **le plus**.

**Pourquoi la température implicite n'est pas une porte d'entrée :** émettre peu, ce n'est pas contribuer. Avec une porte « température ≤ 1,5 °C », 76 entreprises seraient entrées seulement parce qu'elles polluent peu (surtout des banques et des laboratoires pharmaceutiques), sans rien apporter aux limites planétaires.

### Case 2 — Elle ne nuit pas aux autres limites (DNSH)

Il faut remplir **les deux** conditions :

| Condition | Seuil | Ce que ça veut dire |
|---|---|---|
| Aucun ODD environnemental désaligné | ODD 6, 12, 13, 14 **et** 15 tous **> −2** | Elle ne dégrade ni l'eau, ni les ressources, ni le climat, ni les océans, ni les sols. **On ne règle pas un problème en en créant un autre.** |
| Trajectoire climatique acceptable | Température implicite **≤ 3 °C** | Elle n'est pas sur une trajectoire catastrophique |

→ **666 entreprises** passent.

**Pourquoi 3 °C et pas 2 °C :** un seuil à 2 °C exclurait justement des fabricants de solutions, comme EDP Renováveis (éolien et solaire, 2,1 °C), Nibe (pompes à chaleur, 2,5 °C), Novonesis (enzymes, 2,1 °C), Infineon (puces pour le solaire et les réseaux, 3,0 °C), Saint-Gobain (isolation, 2,1 °C) ou Norsk Hydro (aluminium bas carbone, 2,1 °C). Leur température est élevée parce qu'elles **fabriquent et grandissent**, pas parce qu'elles nuisent. La température sert ici de **garde-fou**. L'objectif de Paris est tenu au niveau du **fonds entier** : au moins −50 % d'intensité carbone par rapport à l'univers, puis −7 % par an (vérifié à la pondération).

### Case 3 — Gouvernance minimale

| Condition | Seuil | Pourquoi |
|---|---|---|
| Pas de controverse de gouvernance très grave | Score ≠ 0 *(déjà vérifié en A4)* | Minimum réglementaire |
| Gouvernance correcte | Pilier gouvernance MSCI **≥ 3/10** | On écarte seulement les gouvernances défaillantes |

→ **834 entreprises** passent. C'est volontairement peu sélectif : la gouvernance n'est pas notre thème (règle d'or n°1).

**→ Résultat de l'étape B : 404 entreprises éligibles à l'Article 9.** La plupart des 437 qui échouent **ne contribuent à aucune limite** (257). 80 contribuent mais **nuisent** à une autre, et 94 échouent sur les deux.

---

## 6. La revue qualitative : « les données proposent, l'analyse vérifie »

Les données ESG ne voient pas tout. Après le calcul, l'équipe **relit les entreprises sélectionnées**. Si l'activité réelle contredit les données :
1. **On ne retire jamais une entreprise au cas par cas.**
2. **On écrit une règle** sur l'**activité**, puis on l'applique à **tout l'univers**.
3. **On trace la décision** : l'entreprise repérée, ce qu'on a vu, la règle créée.

| Repérée | Ce que disaient les données | La réalité | Règle créée | Appliquée à |
|---|---|---|---|---|
| **Newmont** (classée 9e) | ODD 6, 7, 12 et 13 alignés, température 1,3 °C | L'or sert surtout aux bijoux et aux lingots, pas à la transition. Son extraction utilise du cyanure, déplace des tonnes de roche et laisse des déchets miniers qui menacent l'eau et les sols | **Pas d'or** : mines, financeurs par redevances, bijouterie | Newmont, Barrick, Agnico Eagle, Northern Star, Franco-Nevada, Wheaton, Chow Tai Fook |
| **Mowi** (classée 7e) | ODD 6 et 12 alignés, 34 % de chiffre d'affaires vert, **ODD 14 (océans) noté 0** | Pollution des fjords, poux de mer transmis aux saumons sauvages, poissons échappés, alimentation au soja (déforestation) et aux farines de poissons sauvages | **Pas de saumon d'élevage en mer** | Mowi, SalMar |
| **Amadeus** | Logiciel, peu émetteur | Son chiffre d'affaires grandit avec le **nombre de vols** | Extension de la règle Jevons **aérien** | Amadeus |

**Pourquoi c'est important :** c'est la leçon de l'*Aggregate Confusion* (Berg, Kölbel et Rigobon) en pratique. Une donnée ESG peut être bonne alors que l'activité, elle, dégrade une limite planétaire. Les bons scores ODD de Newmont reflètent ses **politiques**, pas son **activité**.

**Gardés en connaissance de cause :**
- L'alcool (Diageo, Campari, Kirin) : sujet social, hors de notre thème.
- Les assureurs santé (Elevance, Cigna) : ils n'assurent pas de projets fossiles.
- Holcim (ciment) : secteur indispensable, et Holcim est la meilleure de son secteur.
- Komatsu et Sandvik : leurs machines servent aussi aux mines des métaux de la transition.

---

## 7. Notre périmètre d'investissement

| | Entreprises |
|---|---|
| MSCI World (31/12/2024) | 1 247 |
| − A1 Énergies fossiles | − 115 |
| − A2 Financement des énergies fossiles | − 183 |
| − A3 Effet rebond (Jevons) | − 49 |
| − A4 Garde-fous | − 59 |
| **= Entreprises investissables** | **841** |
| − Test Article 9 | − 437 |
| **= Périmètre d'investissement** | **404** |

**Répartition par secteur :** Industrie 102 · Technologie 89 · Santé 54 · Consommation de base 38 · Immobilier 31 · Consommation discrétionnaire 25 · Communication 21 · Matériaux 16 · Services financiers (paiement, bourses) 14 · Services aux collectivités 14.

**Sélectivité :** on écarte **68 % de l'univers**. Le label ISR exige d'en écarter au moins 30 %.

Ces **404 entreprises** ont toutes le droit, réglementairement et selon notre thème, d'entrer dans le fonds. L'étape suivante choisit **les meilleures** grâce au score JEVONS.

---

## 8. Nos seuils : strict ou souple ?

**En résumé :** **très stricts sur ce qu'on refuse**, **moyens sur la contribution**, **volontairement souples sur le social et la gouvernance**. C'est cohérent avec la règle d'or n°1.

| Seuil | Origine | Niveau |
|---|---|---|
| Tout le secteur Énergie | Notre choix (la règle officielle : 10 % pétrole, 50 % gaz) | 🔴 Très strict |
| Charbon ≥ 1 % du chiffre d'affaires | Règlement Paris-Aligned | 🟠 Standard |
| ≥ 10 % d'une mine de charbon | Notre choix | 🔴 Strict |
| Électricité carbonée | Approximation de la règle officielle | 🟠 Standard |
| Toutes les financières | Notre choix | 🔴 Très strict |
| Effet rebond (Jevons) | Notre choix (même la voiture électrique) | 🔴 Très strict |
| Controverses environnementales : rouge et orange | Notre choix | 🔴 Strict |
| Controverses sociales et de gouvernance : rouge seulement | Minimum Article 9 | 🟢 Souple, voulu |
| Tabac, armes controversées | Règlement Paris-Aligned | 🟠 Standard |
| ODD ≤ −5 | Norme MSCI | 🟠 Moyen |
| Or, saumon d'élevage | Revue qualitative | 🔴 Strict |
| Données manquantes | Notre choix | 🔴 Strict |
| Contribution : ODD ≥ 2 ou chiffre d'affaires vert ≥ 20 % | Norme MSCI et pratique du marché | 🟢 Plutôt souple |
| Ne pas nuire : aucun ODD ≤ −2 | Norme MSCI | 🔴 Strict |
| Ne pas nuire : température ≤ 3 °C | Notre choix | 🟢 Souple, voulu |
| Gouvernance ≥ 3/10 | Notre choix | 🟢 Souple, voulu |

---

## 9. Les limites que nous assumons

1. **Les scores ODD notent aussi les politiques**, pas seulement l'activité. Une entreprise peut être « alignée » grâce à ses engagements. C'est ce qui justifie la revue qualitative.
2. **Les émissions financées ne sont pas mesurées.** C'est pourquoi les financières sont exclues. Une base complète des émissions financées permettrait de réintégrer les meilleures banques.
3. **Le volume n'est pas mesuré.** L'effet rebond est donc traité par une liste d'activités, pas par une donnée.
4. **Électricité carbonée :** nous approchons la règle officielle (gCO2/kWh) par l'intensité scope 1.
5. **Des données de dates différentes :** MSCI à fin 2024, les bases charbon à 2026.

---

## 10. Sources et code

| Donnée | Source |
|---|---|
| Univers, données financières et extra-financières | `all_data.csv` (MSCI, 31/12/2024), fourni par l'enseignant |
| Charbon thermique | urgewald, *Global Coal Exit List 2026* (`Urgewald GCEL 2026 V1.0.xlsx`) |
| Mines de charbon (thermique et métallurgique) | Global Energy Monitor, *Global Coal Mine Tracker*, août 2026 (`Global Coal Mine Tracker, August 2026.xlsx`), licence CC BY 4.0 |
| Financements fossiles des banques | *Banking on Climate Chaos 2026* (RAN, BankTrack et al.) ; Reclaim Finance, *Coal Policy Tool* et *Oil and Gas Policy Tracker* (`CoalPolicyTracker.xlsx`, `OilGasPolicyTracker.xlsx`) |
| Limites planétaires | Rockström et al. (2009), Richardson et al. (2023), *Science Advances* |
| Divergence des notations ESG | Berg, Kölbel et Rigobon (2022), *Aggregate Confusion: The Divergence of ESG Ratings*, Review of Finance |
| Règles Paris-Aligned | Règlement délégué (UE) 2020/1818, article 12 |
| Investissement durable | Règlement (UE) 2019/2088 (SFDR), article 2.17 |

### Le code (Python, pandas)

```python
import pandas as pd
df = pd.read_csv("all_data.csv")
odd   = lambda i: df[f"SDG_{i:02d}_NET_ALIGNMENT_SCORE"]
vert  = df[["CT_TOTAL_MAX_REV", "EST_EU_TAXONOMY_MAX_REV"]].max(axis=1)
nom   = lambda motif: df["name"].str.contains(motif)
E, S, G = (df[f"{p}_CONTROVERSY_SCORE"] for p in ["ENVIRONMENT", "SOCIAL", "GOVERNANCE"])

# ── ÉTAPE A : CE QU'ON REFUSE ─────────────────────────────────────────────
charbon = nom("Glencore|BHP Group|CSX Corp|Berkshire Hathaway"            # GCEL ≥ 1 %
              "|Anglo American|Mitsubishi Corp|Mitsui & Co|ITOCHU"        # GCMT ≥ 10 %
              "|Sumitomo Corp|Marubeni|Nippon Steel|JFE Holdings")
A1 = ((df.gics_sector_name == "Energy")
      | ((df.gics_sector_name == "Utilities") & ~((vert >= 50) | (df.INTENSITY_SCOPE_1 < 100)))
      | charbon)

paiement_bourses = (df.industry_group.isin(["Commercial Services", "Software"])
      | nom("Visa Inc|Mastercard|American Express|Intercontinental Exchange|CME Group"
            "|London Stock Exchange|Hong Kong Exchanges|Deutsche Boerse|Nasdaq Inc"
            "|Cboe|Tradeweb|Japan Exchange|Singapore Exchange|ASX Ltd"))
A2 = (df.gics_sector_name == "Financials") & ~paiement_bourses

A3 = (df.industry_group.isin(["Airlines", "Auto Manufacturers", "Auto Parts&Equipment"])
      | nom("Carnival|Royal Caribbean|Amadeus IT|Industria de Diseno|Hennes & Mauritz"
            "|Fast Retailing|Associated British Foods"))

A4 = ((E <= 1) | (S == 0) | (G == 0)
      | (df.TOB_PRODUCER > 0) | (df.CWEAP_TIE > 0)
      | (odd(14) <= -5) | (odd(15) <= -5) | (odd(6) <= -5) | (odd(12) <= -5)
      | nom("Newmont|Agnico Eagle|Barrick Gold|Northern Star Resources|Franco-Nevada"
            "|Wheaton Precious|Chow Tai Fook|Mowi ASA|Salmar ASA")      # revue qualitative
      | df[["IVA_COMPANY_RATING", "ITR", "INTENSITY_SCOPE_1"]].isna().any(axis=1))

investissable = ~(A1 | A2 | A3 | A4)                                   # 841

# ── ÉTAPE B : TEST ARTICLE 9 ──────────────────────────────────────────────
contribue = (odd(13) >= 2) | (odd(7) >= 2) | (odd(6) >= 2) | (odd(12) >= 2) | (vert >= 20)
ne_nuit_pas = (pd.concat([odd(i) for i in [6, 12, 13, 14, 15]], axis=1).min(axis=1) > -2) \
              & (df.ITR <= 3)
gouvernance = df.GOVERNANCE_PILLAR_SCORE >= 3

perimetre = df[investissable & contribue & ne_nuit_pas & gouvernance]  # 404
```
