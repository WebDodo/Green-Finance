# Holocène Actions Monde — Méthodologie du fonds

*Lichen AM · Projet final Finance durable · Université Paris-Dauphine · 2026*

> **Investir dans les limites de la planète.**

Ce document explique comment on passe des **1 247 entreprises du MSCI World** à un **portefeuille de 50 entreprises pondérées**, avec, pour chaque règle, le seuil, la donnée et la raison du choix.

**Sommaire**
1. Le fonds en bref
2. L'entonnoir
3. Étape A : ce qu'on refuse
4. Étape B : le test Article 9
5. Étape C : le score Holocène
6. Étape D : la revue qualitative
7. Étape E : les filtres financiers
8. Étape F : le score final et les 50 lignes
9. Étape G : la pondération
10. Le portefeuille
11. Résultats extra-financiers
12. Résultats financiers passés
13. Conformité réglementaire
14. Nos limites
15. Fichiers et code

---

## 1. Le fonds en bref

| | |
|---|---|
| **Société de gestion** | **Lichen AM**. Le lichen est un bio-indicateur : il ne pousse que là où l'air est sain. Notre méthode : **mesurer avant d'investir**. |
| **Fonds** | **Holocène Actions Monde**. L'Holocène est la période de climat stable dans laquelle vit l'humanité depuis 11 700 ans. |
| **Forme** | FCP de droit français, OPCVM, actions monde, sans levier, liquidité quotidienne |
| **Classification** | **SFDR Article 9.3** (objectif de réduction carbone, indice Paris-Aligned) |
| **Indice de référence** | MSCI World Climate Paris Aligned |
| **Univers de départ** | MSCI World au 31/12/2024 : 1 247 entreprises (`all_data.csv`) |
| **Frais de gestion** | 0,75 % par an |

### L'objectif d'investissement durable

> *Le fonds a pour objectif la **réduction des émissions de carbone** (article 9.3 de SFDR) : son empreinte carbone est au moins **50 % inférieure** à celle du marché, puis baisse de **7 % par an**. Plus largement, il investit dans des entreprises qui aident à rester dans les **limites planétaires** (climat, eau, ressources) sans nuire aux autres, notamment à la biodiversité.*

**Pourquoi le carbone en premier :** l'article 9.3 vise les fonds dont l'objectif est la réduction carbone. Il faut donc un objectif carbone chiffré, et on le tient : **−53 %** (section 11).

**Les limites planétaires** (Rockström 2009, Richardson 2023) sont 9 seuils à ne pas dépasser pour que la Terre reste stable ; 7 sont déjà dépassés. Le fonds en suit 4 directement avec les données (climat, eau douce, nouvelles entités, biodiversité) et 4 par ses exclusions (usage des sols, azote et phosphore, acidification des océans, aérosols). La couche d'ozone n'est pas suivie : elle se reconstitue.

### Nos deux règles d'or

1. **L'environnement est notre expertise : là, on va au-delà de la réglementation.** Sur le social et la gouvernance, on applique le socle exigé (Pacte mondial de l'ONU, OCDE, gouvernance saine).
2. **On n'investit pas dans ce qu'on ne mesure pas.**

---

## 2. L'entonnoir

```
1 247  MSCI World (31/12/2024)
  │  A  Ce qu'on refuse (fossiles, financières, secteurs incompatibles, garde-fous)   − 406
  ▼
  841  investissables
  │  B  Test Article 9 : contribue + ne nuit pas + bonne gouvernance                 − 437
  ▼
  404  périmètre d'investissement
  │  C  Score Holocène ≥ 60                                                          − 272
  │  D  Revue qualitative (or, saumon, fast fashion, croisières)                      −   7
  ▼
  125  sélection extra-financière
  │  E  Filtres financiers (rentable, pas surendettée, risque supportable)           −  23
  │  F  Score final : les 50 meilleures, 10 maximum par secteur                       −  52
  ▼
   50  entreprises en portefeuille
  │  G  Pondération : score ÷ volatilité, chaque ligne entre 1 % et 5 %
  ▼
  LE FONDS
```

*Une entreprise exclue pour plusieurs raisons est comptée une seule fois, dans la première règle qui l'exclut. Toutes les règles sont automatiques, sauf l'étape D : nos données n'ont pas de colonne « or » ou « saumon ».*

---

## 3. Étape A — Ce qu'on refuse (−406)

| Règle | Seuil | Donnée | Pourquoi | Exclues |
|---|---|---|---|---|
| ⛽ Pétrole et gaz | Tout le secteur Énergie | `gics_sector_name` | Plus strict que la règle Paris-Aligned (10 % pétrole, 50 % gaz) : nos données n'ont pas ces parts | 52 |
| 🏭 Électricité carbonée | Électricien gardé seulement si CA Taxonomie ≥ 50 % ou scope 1 < 100 tCO2e/M$ | `EST_EU_TAXONOMY_MAX_REV`, `INTENSITY_SCOPE_1` | Approximation de la règle officielle (100 gCO2/kWh), absente de nos données | 51 |
| ⚫ Charbon | ≥ 1 % du chiffre d'affaires | Global Coal Exit List 2026 (urgewald) | Seuil officiel Paris-Aligned. Glencore : 98 Mt de charbon par an, mais seulement 3,2 % de son CA | 7 |
| ⛏️ Mines de charbon | ≥ 10 % d'une mine active de plus de 0,5 Mt/an | Global Coal Mine Tracker 2026 (GEM) | Les miniers et maisons de commerce japonaises ne sont pas classés en Énergie | 7 |
| 🏦 Financières | Banques, assureurs, gestionnaires (sauf paiement et notation) | `gics_sector_name`, `industry_group` | Elles financent les fossiles, et MSCI mesure leurs bureaux, pas leurs prêts | 197 |
| ✈️🚗🌾 Secteurs incompatibles | Aérien, automobile (électrique comprise), négoce agricole | `industry_group` | Modèles qui dépassent les limites planétaires sans alternative à grande échelle | 49 |
| 🛡️ Garde-fous | Données manquantes, controverse environnementale rouge ou orange, controverse sociale ou de gouvernance rouge, tabac, armes controversées, un ODD environnemental ≤ −5 | colonnes MSCI | Exigences Paris-Aligned + règle d'or n°2 | 43 |

**Exclus pour charbon :** Glencore, BHP, CSX, Berkshire Hathaway, Jardine Matheson, Jardine Cycle & Carriage, Sumitomo (GCEL) ; Anglo American, Mitsubishi, Mitsui, ITOCHU, Marubeni, Nippon Steel, JFE (mines).

⚠️ *Piège : dans la Global Coal Exit List, la colonne « Coal Share of Revenue » est une fraction (0,03 = 3 %) alors que l'en-tête dit « in % ».*

---

## 4. Étape B — Le test Article 9 (−437)

Pour un Article 9, **chaque** entreprise doit être un « investissement durable » (SFDR, art. 2.17). Il faut cocher **les 3 cases** :

| Case | Règle | Pourquoi |
|---|---|---|
| **1. Contribue** | Au moins un ODD parmi 6 (eau), 7 (énergie), 12 (ressources), 13 (climat) ≥ 2, **ou** CA Taxonomie ≥ 20 % | 2 = seuil MSCI « aligné » ; 20 % = seuil courant du marché |
| **2. Ne nuit pas** | ODD 6, 12, 13, 14, 15 tous > −2, **et** température implicite ≤ 3 °C | On ne règle pas un problème en en créant un autre. 3 °C et pas 2 °C pour garder des fabricants de solutions (Nibe, Infineon, Saint-Gobain) |
| **3. Gouvernance** | Pilier gouvernance MSCI ≥ 3/10 | Écarte les gouvernances défaillantes |

Les scores ODD de MSCI vont de −10 à +10 : ≥ 2 « aligné », ≤ −2 « désaligné », ≤ −5 « fortement désaligné ».

**→ 404 entreprises éligibles.** La plupart de celles qui échouent ne contribuent à rien.

---

## 5. Étape C — Le score Holocène (−272)

On classe les 404 pour garder celles qui **apportent le plus** à la planète **en lui coûtant le moins**.

> **Score Holocène = 50 % contribution + 25 % trajectoire + 25 % pollution**

| Critère | Mesure | Comparée à |
|---|---|---|
| **Contribution** (50 %) | Somme des scores positifs des ODD 6, 7, 12, 13 + CA Taxonomie ÷ 10 | Tout le périmètre |
| **Trajectoire** (25 %) | Température implicite (plus bas = mieux) | Son secteur |
| **Pollution** (25 %) | Intensité carbone scopes 1+2+3 (plus bas = mieux) | Son secteur |

Chaque mesure devient un **percentile** (« meilleure que X % des entreprises comparées »). L'empreinte est comparée **dans le secteur** : une usine émettra toujours plus qu'un éditeur de logiciels.

*Exemple, Vestas : 0,5 × 100 + 0,25 × 92 + 0,25 × 60 = **88**.*

**Pourquoi 50 % sur la contribution :** à poids égaux, le haut du classement était Visa, Pearson et Diageo, qui polluent peu mais n'apportent rien.

**On garde les scores ≥ 60** : environ un tiers du périmètre, soit 132 entreprises.

---

## 6. Étape D — La revue qualitative (−7)

Les données ESG ne voient pas tout. On relit les 132 et, si l'activité réelle contredit les données, **on écrit une règle sur l'activité** (jamais un retrait au cas par cas) :

| Règle | Pourquoi | Retirées (score) |
|---|---|---|
| Pas d'or | Cyanure, déchets miniers ; l'or sert surtout aux bijoux et aux lingots | Newmont (88), Agnico Eagle (75), Chow Tai Fook (74) |
| Pas de saumon d'élevage en mer | Pollution des fjords, poux de mer, soja | Mowi (88), SalMar (84) |
| Pas de fast fashion | Eau, polyester, déchets textiles | Inditex (69) |
| Pas de croisières ni de réservation de vols | Même logique que l'aérien | Amadeus (62) |

C'est la leçon d'*Aggregate Confusion* (Berg, Kölbel, Rigobon, 2022) : une bonne note ESG peut cacher une activité nuisible.

**→ 125 entreprises.**

---

## 7. Étape E — Les filtres financiers (−23)

Une entreprise très verte mais **fragile** n'a pas sa place dans un fonds « équilibré ».

| Filtre | Règle | Pourquoi | Exclues |
|---|---|---|---|
| **E1 Rentable** | ROIC > 0 et marge nette > 0 | Une entreprise qui perd de l'argent ne peut pas financer sa transition | 8 |
| **E2 Pas surendettée** | Dette / actifs ≤ 60 % (70 % pour les réseaux et l'immobilier) | On ne retire que les cas extrêmes. Les réseaux d'eau et d'électricité et les foncières ont des revenus stables et portent plus de dette | 5 |
| **E3 Risque supportable** | Volatilité 5 ans ≤ 45 % et pire baisse 5 ans moins forte que −60 % | Un épargnant qui perd plus de 60 % vend au pire moment | 10 |

**Exclues :** Brookfield Renewable, Segro, Bristol-Myers Squibb, Link REIT, Nexi… (E1) ; Simon Property, Crown Castle, KPN, Getlink, Masco (E2) ; Vestas, Ørsted, NVIDIA, Croda, PayPal… (E3).

**Choix assumé : Vestas et Ørsted sortent.** Ce sont des symboles de la transition, mais leurs actions ont perdu 70 % et 81 % en 5 ans. On finance la transition à travers des entreprises solides : réseaux électriques (Red Eléctrica, Terna, Hydro One), eau (Xylem, United Utilities), efficacité énergétique (Schneider, Trane).

**Pas de filtre sur le PER :** il est trompeur quand les bénéfices sont temporairement bas (Vestas : PER de 406). Le prix entre dans le score (étape F).

**→ 102 entreprises.**

---

## 8. Étape F — Le score final et les 50 lignes (−52)

**Score financier** = moyenne de 3 percentiles, calculés **dans le secteur** :
- **Qualité :** ROIC (combien l'entreprise gagne sur chaque euro investi)
- **Performance / risque :** ratio de Sharpe sur 5 ans
- **Prix :** rendement du cash-flow libre (plus il est élevé, moins l'action est chère)

> **Score final = 60 % score Holocène + 40 % score financier**

60 / 40 : c'est un Article 9, donc le vert prime, mais le fonds doit aussi être performant.

*Exemple, AECOM (ingénierie environnementale) : 0,6 × 88 + 0,4 × 73 = **82** (1re).*

On garde **les 50 meilleures**, avec **au plus 10 par secteur** pour ne pas avoir un fonds 100 % industrie et technologie. La 50e a un score final de 63.

---

## 9. Étape G — La pondération

> **Poids ∝ score final ÷ volatilité sur 5 ans**, puis chaque ligne est bornée **entre 1 % et 5 %**

- **× score final :** plus une entreprise est bonne, plus elle pèse (conviction).
- **÷ volatilité :** à score égal, une action deux fois plus instable pèse deux fois moins (équilibre).
- **5 % maximum :** aucune entreprise ne pèse trop, et la règle 5/10/40 des OPCVM est respectée d'office.

**Résultat :** des poids de 1,3 % à 3,2 % ; les 10 premières lignes pèsent 27 %. Les poids sont **remis à la cible chaque mois** et la sélection est **revue chaque année**, à la publication des nouvelles données ESG.

**Pourquoi pas autre chose :** pondérer par la capitalisation ferait de Microsoft une ligne énorme ; des poids égaux ignoreraient le score et le risque ; une optimisation de Markowitz concentrerait le fonds sur les titres qui ont le mieux marché par le passé.

---

## 10. Le portefeuille

**Les 10 premières lignes** (la liste complète des 50 est dans `resultats/Holocene_Portefeuille.xlsx`) :

| # | Entreprise | Activité | Pays | Poids |
|---|---|---|---|---|
| 1 | Novartis | Pharmacie | Suisse | 3,2 % |
| 2 | Hydro One | Réseau électrique | Canada | 3,1 % |
| 3 | Swisscom | Télécoms | Suisse | 3,0 % |
| 4 | Red Eléctrica | Réseau électrique | Espagne | 2,9 % |
| 5 | RELX | Information scientifique | Royaume-Uni | 2,7 % |
| 6 | United Utilities | Eau potable | Royaume-Uni | 2,5 % |
| 7 | CapitaLand Integrated Commercial Trust | Immobilier | Singapour | 2,5 % |
| 8 | Terna | Réseau électrique | Italie | 2,4 % |
| 9 | GSK | Pharmacie | Royaume-Uni | 2,4 % |
| 10 | Merck & Co | Pharmacie | États-Unis | 2,4 % |

| Secteur | Lignes | Fonds | MSCI World |
|---|---|---|---|
| Santé | 10 | 21,0 % | 10,5 % |
| Industrie | 10 | 19,3 % | 10,6 % |
| Technologie | 10 | 16,4 % | 26,3 % |
| Services aux collectivités | 6 | 14,5 % | 2,4 % |
| Consommation de base | 6 | 12,5 % | 6,0 % |
| Immobilier | 3 | 6,7 % | 2,0 % |
| Consommation discrétionnaire | 2 | 3,4 % | 11,1 % |
| Matériaux | 2 | 3,2 % | 3,1 % |
| Communication | 1 | 3,0 % | 8,1 % |
| Énergie et financières | 0 | 0 % | 19,9 % |

| Région | Fonds | MSCI World |
|---|---|---|
| Europe | 47,8 % | 16,0 % |
| Amérique du Nord | 38,6 % | 75,9 % |
| Japon | 9,2 % | 5,3 % |
| Asie-Pacifique | 4,3 % | 2,4 % |

**À retenir :** le fonds surpondère les solutions (réseaux, eau, ingénierie, santé) et l'Europe, dont les entreprises publient plus de données et ont de meilleurs scores ODD. Il sous-pondère la technologie américaine (NVIDIA est sortie par le risque, Microsoft pèse 1,8 %).

---

## 11. Résultats extra-financiers

Moyennes pondérées : pour le fonds, ses poids ; pour le MSCI World, la capitalisation boursière.

| Indicateur | **Fonds** | MSCI World | Écart |
|---|---|---|---|
| **Empreinte carbone** scopes 1+2+3 (tCO2e par M$ investi) | **712** | 1 522 | **−53 %** |
| Intensité carbone scopes 1+2 (tCO2e par M$ de CA) | **47** | 96 | **−50 %** |
| **Température implicite** | **1,47 °C** | 2,40 °C | aligné 1,5 °C |
| Chiffre d'affaires aligné Taxonomie UE | **13,0 %** | 8,9 % | +4 pts |
| Part notée AA ou AAA par MSCI | **79 %** | 45 % | +34 pts |
| Pilier environnement / social / gouvernance (/10) | **7,2 / 5,6 / 6,4** | 6,7 / 5,1 / 5,7 | |
| Énergies fossiles | **0 %** | 7,6 % | |

**Les 3 chiffres de l'oral :** **−53 %** de carbone, **1,47 °C**, **79 %** noté AA ou AAA.

---

## 12. Résultats financiers passés

**Méthode :** cours mensuels ajustés des dividendes (Yahoo Finance), convertis en euros, poids remis à la cible chaque mois, **0,75 % de frais déduits**. Comparaison avec l'ETF iShares MSCI World (URTH) converti en euros. Taux sans risque : €STR de la BCE.

⚠️ **À dire honnêtement :** les entreprises ont été choisies avec des données de fin 2024 (Sharpe et volatilité 2020-2024). La période 2020-2024 est donc **flatteuse par construction**. **Le vrai test est 2025-2026**, que nos données ne connaissaient pas.

| | Fonds 2020-2024 | MSCI World 2020-2024 | **Fonds 2025-2026** | **MSCI World 2025-2026** |
|---|---|---|---|---|
| Performance cumulée | +98,2 % | +83,9 % | **+16,7 %** | **+26,7 %** |
| Performance annualisée | 14,7 % | 13,0 % | 8,4 % | 13,1 % |
| Volatilité | 13,0 % | 16,0 % | 10,2 % | 11,2 % |
| Sharpe | 1,04 | 0,74 | 0,61 | 0,98 |
| Pire baisse (fin de mois) | −13,8 % | −20,3 % | −5,9 % | −12,3 % |

| Année | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 (au 13/11) |
|---|---|---|---|---|---|---|---|
| Fonds | +11,3 % | +30,5 % | **−4,0 %** | +21,8 % | +16,8 % | +2,5 % | +13,8 % |
| MSCI World | +5,5 % | +32,8 % | **−12,9 %** | +19,4 % | +26,2 % | +7,5 % | +17,8 % |

**Ce que ça dit :**
- **C'est un fonds défensif :** il baisse moins quand le marché chute (−4 % contre −13 % en 2022) et il est moins volatil.
- **Il a été distancé en 2024-2026**, quand la hausse venait de ce que nous excluons : semi-conducteurs de l'IA, banques, géants technologiques américains. Il a aussi souffert de Novo Nordisk (−54 % depuis janvier 2025) et des éditeurs de logiciels (ServiceNow −56 %, Salesforce −38 %), mais profité de la pharmacie (Eli Lilly +73 %, Novartis +64 %) et des réseaux électriques.
- **Profil de risque :** volatilité de 13 % sur 5 ans, soit la **classe 4 sur 7** de l'indicateur de risque réglementaire (SRI).

> *Mention obligatoire : « Les performances passées ne préjugent pas des performances futures. Performances simulées, nettes de frais de gestion. Le fonds présente un risque de perte en capital. »*

---

## 13. Conformité réglementaire

Recalculée automatiquement (onglet « Contrôles » du fichier Excel).

| Règle | Mesure | ✓ |
|---|---|---|
| **OPCVM 5/10/40** : aucune ligne > 10 % ; les lignes > 5 % totalisent ≤ 40 % | ligne maximale 3,2 % | ✅ |
| **Article 9** : 100 % d'investissements durables | 50 / 50 passent le test B | ✅ |
| **Paris-Aligned, exclusions** (charbon, pétrole, gaz, électricité carbonée, tabac, armes, Pacte mondial) | 0 ligne concernée | ✅ |
| **Paris-Aligned** : empreinte carbone ≤ 50 % du marché | −53 % | ✅ |
| **Paris-Aligned** : exposition aux secteurs à fort impact climatique ≥ marché | 82 % contre 59 % | ✅ |
| **Paris-Aligned** : −7 % d'empreinte par an | engagement : ≤ 662 tCO2e/M$ en 2027 | ⏳ |
| **Label ISR** : au moins 30 % de l'univers écarté | 68 % au périmètre, 96 % au fonds | ✅ |

**Les indicateurs d'incidences négatives (PAI)**, obligatoires pour un Article 9 :

| Traitement | PAI |
|---|---|
| **Mesurés ou exclus** | 1-3 émissions, empreinte et intensité carbone · 4 énergies fossiles · 10 violations du Pacte mondial · 14 armes controversées |
| **Approchés par les scores ODD** | 7 biodiversité (ODD 14, 15) · 8 rejets dans l'eau (ODD 6) · 9 déchets dangereux (ODD 12) · 11 contrôle du Pacte mondial (pilier gouvernance) |
| **Absents de nos données** | 5 énergie non renouvelable · 6 intensité énergétique · 12 écart de salaire femmes-hommes · 13 mixité des conseils |

**Communication (règles AMF, pour l'oral) :**
- les risques doivent être aussi visibles que les avantages ;
- les performances passées s'accompagnent de la mention obligatoire et sont signalées comme simulées ;
- toute affirmation verte doit être prouvée par un chiffre (« −53 % de carbone », pas « un fonds qui sauve la planète ») ;
- le nom « Holocène Actions Monde » ne contient pas de terme ESG : les règles ESMA sur les noms ne s'appliquent pas, et on les respecterait de toute façon.

---

## 14. Nos limites

1. **Les scores ODD notent aussi les politiques**, pas seulement l'activité : d'où la revue qualitative.
2. **Les émissions financées ne sont pas mesurées** : d'où l'exclusion de toutes les financières, y compris Visa et Mastercard, que nos données ne distinguent pas.
3. **Approximations :** électricité carbonée par le scope 1, secteurs à fort impact par les groupes d'industrie, 4 PAI absents.
4. **Données de dates différentes :** MSCI à fin 2024, bases charbon à 2026.
5. **La simulation 2020-2024 est biaisée en notre faveur.** Sur le vrai test (2025-2026), le fonds fait moins bien que le marché, mais avec moins de risque.
6. **Backtest simplifié :** coûts de transaction non comptés, cours Yahoo Finance (source gratuite), données mensuelles, MSCI World approché par un ETF.

---

## 15. Fichiers et code

| Fichier | Contenu |
|---|---|
| `1_selection_extra_financiere.py` | Étapes A à D : 1 247 → 125 |
| `2_portefeuille.py` | Étapes E à G, résultats verts, contrôles, performance, fichiers Excel |
| `resultats/Holocene_Portefeuille.xlsx` | **Livrable 1** : les 50 lignes et leurs poids, caractéristiques, contrôles, performance, entonnoir des 1 247 |
| `resultats/Holocene_Donnees_complementaires.xlsx` | **Livrable 2** : sources, exclus pour charbon, cours mensuels, taux de change, €STR |
| `Urgewald GCEL 2026 V1.0.xlsx`, `Global Coal Mine Tracker, August 2026.xlsx` | Bases charbon |
| `all_data_eligibles.xlsx` | Les 404 et les 125, avec le score Holocène |

**Pour tout relancer :** mettre `all_data.csv` dans un dossier `data` à côté du dossier du dépôt, puis, depuis le dossier du dépôt :

```bash
pip install pandas openpyxl yfinance
python 1_selection_extra_financiere.py
python 2_portefeuille.py
```

Les cours sont téléchargés une seule fois puis gardés dans `donnees_complementaires/`. Pour les retélécharger, supprimer ce dossier.

**Sources :** MSCI (`all_data.csv`) · urgewald, *Global Coal Exit List 2026* · Global Energy Monitor, *Global Coal Mine Tracker* (CC BY 4.0) · *Banking on Climate Chaos 2026* · Rockström et al. (2009), Richardson et al. (2023) · Berg, Kölbel, Rigobon (2022) · SFDR (UE 2019/2088) et RTS (UE 2022/1288) · Paris-Aligned (UE 2020/1818) · Taxonomie (UE 2020/852) · Yahoo Finance · BCE (€STR).
