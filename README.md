# Green-Finance

# Étape 1 — Concept et objectif du fonds ✅ validé

## Identité

- **Société de gestion : Holocène AM.** L'Holocène est l'époque géologique de climat stable dans laquelle vit l'humanité depuis environ 11 700 ans, et qui lui a permis de prospérer. Notre mission est d'investir pour que l'économie reste dans les limites planétaires qui garantissent cette stabilité.
- **Fonds : JEVONS Actions Monde.** Il porte le nom du paradoxe de Jevons (1865) : plus une technologie devient efficace, plus on la consomme (effet rebond). Le fonds est conçu pour résoudre ce problème. Il ne récompense pas seulement l'efficacité : il finance les entreprises qui réduisent vraiment la pression totale sur la planète.
- **Signature :** *Faire moins, pas seulement mieux.*

## Thème

Un fonds actions monde qui investit dans les entreprises qui aident l'économie à **rester dans les limites planétaires** (Rockström, 2009 : 9 limites, dont 7 franchies selon le Planetary Health Check 2025). Il vise la **sobriété**, pas seulement l'efficacité.

| Limite planétaire | Rôle dans le fonds | Mesures (all_data.csv) |
|---|---|---|
| Changement climatique | Contribution | Température implicite (ITR), intensité carbone, ODD 13 |
| Eau douce | Contribution | ODD 6 |
| Ressources et pollution (entités nouvelles, cycles) | Contribution | ODD 12, Taxonomie, technologies propres |
| Biodiversité (terre et mer) | Garde-fou (DNSH) | ODD 14 et 15 |

## Objectif d'investissement durable (Article 9 SFDR)

> Le fonds a pour objectif d'investissement durable de contribuer à réduire la pression de l'économie sur les limites planétaires, en finançant des entreprises qui contribuent de manière mesurable à au moins un des objectifs suivants (atténuation du changement climatique, protection des ressources en eau, transition vers une économie circulaire) sans porter atteinte de manière significative aux autres limites, notamment la biodiversité. Le fonds vise en outre une réduction de l'empreinte carbone conforme à l'Accord de Paris.

- **100 % d'investissements durables** au sens de l'article 2.17 de SFDR (hors liquidités et couverture).
- **Article 9.3**, parce que l'objectif inclut une réduction des émissions : indice de référence désigné **MSCI World Climate Paris Aligned**. Intensité carbone au moins 50 % sous l'univers, puis −7 % par an.
- **Ancrage Taxonomie :** 3 des 6 objectifs européens (climat, eau, économie circulaire), avec la biodiversité comme garde-fou.

## Pitch oral (version courte)

*« La planète a 9 limites, 7 sont déjà franchies. Les fonds verts récompensent l'efficacité. Nous, nous finançons la sobriété : les entreprises qui réduisent vraiment la pression sur le climat, l'eau et les ressources, sans abîmer le vivant. »*

# Étape 2 — Univers et exclusions (proposition à valider)

## L'univers de départ

**MSCI World au 31/12/2024 : 1 247 entreprises** de 23 pays développés (fichier `all_data.csv`).

Les exclusions sont la première porte du processus. Elles retirent d'emblée tout ce qui est incompatible avec un fonds « limites planétaires », avant même de regarder ce que les entreprises apportent. On les organise en **4 familles**, chacune avec sa justification.

## Famille 1 — Énergies fossiles (socle Paris-Aligned)

Le règlement délégué (UE) 2020/1818 impose aux indices Paris-Aligned (PAB) d'exclure les entreprises qui tirent au moins 1 % de leur chiffre d'affaires du charbon, 10 % du pétrole, 50 % du gaz, ou 50 % d'une électricité émettant plus de 100 gCO2e/kWh.

| Règle | Comment on l'applique | Exclues |
|---|---|---|
| **E1. Secteur Énergie** | Tout le secteur GICS Énergie. Le fichier ne donne pas le chiffre d'affaires fossile ligne à ligne, donc on retient le proxy le plus prudent. | 52 |
| **E2. Électricité carbonée** | Une utility n'est conservée que si au moins 50 % de son chiffre d'affaires est vert, **ou** si son intensité scope 1 est inférieure à 100 tCO2e par M$ de chiffre d'affaires (réseaux, eau). | 51 |
| **E3. Mines de charbon** | Liste manuelle des mineurs exposés au charbon, aucune colonne du fichier ne le permet. Candidats **à vérifier dans les rapports annuels** : Glencore, BHP, Anglo American, South32. Ce sera une donnée complémentaire (2e fichier Excel). | ≈ 4 |

## Famille 2 — Exclusions normatives (éthique et conformité)

| Règle | Donnée utilisée | Exclues |
|---|---|---|
| **N1. Tabac** | `TOB_PRODUCER` | 5 |
| **N2. Armes controversées** | `CWEAP_TIE` | 5 |
| **N3. Controverses graves** | Score de controverse MSCI ≤ 1 (drapeau rouge ou orange) sur l'un des 3 piliers E, S ou G. C'est notre proxy des violations du Pacte mondial de l'ONU et des principes de l'OCDE (PAI 10). | 181 |
| **N4. Pires notes ESG** | Note MSCI CCC ou B | 17 |

## Famille 3 — Exclusions « limites planétaires »

C'est notre spécificité. On écarte les entreprises qui dégradent **fortement** une limite que l'on protège, même si elles sont bonnes ailleurs.

| Règle | Donnée utilisée | Exclues | Qui ? |
|---|---|---|---|
| **L1. Biodiversité** | ODD 14 (vie aquatique) **ou** ODD 15 (vie terrestre) ≤ −5, c'est-à-dire « fortement désaligné » | 13 | Surtout la chimie et les plastiques : BASF, Dow, Amcor, Celanese… La limite « entités nouvelles » (plastiques, polluants) en est une. |
| **L2. Eau et ressources** | ODD 6 (eau) **ou** ODD 12 (consommation responsable) ≤ −5 | 72 | Presque toutes déjà exclues par la famille 1. Sert de filet de sécurité. |

## Famille 4 — Exclusion « Jevons » 🎯

Le cours n°1 prend l'**aviation** comme exemple du paradoxe de Jevons : l'efficacité par passager s'améliore spectaculairement, mais les émissions totales augmentent parce que le volume explose. Pour un fonds qui porte le nom de Jevons, c'est la règle symbolique.

| Règle | Donnée utilisée | Exclues |
|---|---|---|
| **J1. Activités du rebond** | Compagnies aériennes (`industry_group` = Airlines) et croisiéristes (Carnival, Royal Caribbean) : des modèles économiques fondés sur la hausse des volumes d'un usage très carboné. | 10 |

*Argument oral : « Aucune amélioration d'efficacité ne compense un modèle économique qui repose sur toujours plus de volume. »*

## Famille 5 — Qualité des données

| Règle | Exclues |
|---|---|
| **D1.** Note ESG, température implicite ou intensité carbone manquante : on n'investit pas dans ce qu'on ne mesure pas. La couverture ESG doit atteindre au moins 90 % pour le label ISR. | 14 |

## Bilan

| | Nombre | Poids dans le MSCI World |
|---|---|---|
| Univers de départ | 1 247 | 100 % |
| **Exclues** (une entreprise peut cumuler plusieurs motifs) | **≈ 317** | **≈ 39 %** |
| **Univers investissable** | **≈ 930** | ≈ 61 % |

Le poids exclu (39 %) est bien plus élevé que le nombre d'entreprises exclues (25 %). La raison : plusieurs géants tombent sur les controverses graves (Apple, Amazon, Meta, Tesla, JPMorgan…). C'est un point à assumer à l'oral : **pas de passe-droit pour la taille**.

## Ce que ces exclusions couvrent côté réglementation

- **PAB** (indice de l'article 9.3) : exclusions fossiles et de base. ✔
- **Orientations ESMA sur le nom des fonds** (2025) : exclusions PAB. ✔
- **Label ISR** (référentiel 2024) : exclusions fossiles et controverses. La sélectivité de 30 % viendra des étapes suivantes. ✔
- **PAI** (indicateurs d'incidences négatives) : PAI 4 (fossile), PAI 7 (biodiversité, via les ODD 14 et 15), PAI 10 (Pacte mondial), PAI 14 (armes controversées). ✔

## Points à trancher

1. **Seuil des controverses (N3).** On garde ≤ 1, c'est-à-dire rouge et orange (181 exclues) ? Ou seulement le rouge, 0 (2 exclues), ce qui garderait Apple et Amazon dans l'univers ?
2. **Exclusion Jevons (J1).** Seulement l'aérien et les croisières ? Ou l'élargir, par exemple aux constructeurs automobiles thermiques ou à la fast fashion ? Pour ces derniers, les données sont moins nettes.
3. **Mines de charbon (E3).** OK pour que tu vérifies ces 4 noms dans les rapports annuels ? Ce serait notre « donnée complémentaire ».


# Définition de l’investissement durable (article 2.17 de SFDR) : contribution, DNSH, gouvernance.

# Sélection extra-financière : nos critères et nos seuils.

# Filtres financiers.

# Pondération.

# Résultats et robustesse.

# Livrables : les 2 Excel, le PowerPoint, le PDF explicatif et le code.
