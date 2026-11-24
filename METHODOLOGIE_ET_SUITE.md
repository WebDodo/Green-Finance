# Lichen Symbiose Climat — méthodologie complète (étapes 0 à 10)

**Lichen Asset Management · fonds actions monde · SFDR Article 9 · « La performance et le climat, en symbiose. »**

Projet final de Finance durable (Université Paris-Dauphine, T. Béchu et J. Jardel, Kanopy AM).
Ce document décrit **toute la méthode du fonds, de l'univers MSCI World au portefeuille final de 70 lignes**, et les choix à défendre devant le jury. Il remplace la version « consignes pour la suite » : l'étape 10 est faite.

> **Échéance** : envoi avant le **mardi 24/11/2026 à 23 h 59** à thierry.bechu@kanopy-am.com et jean.jardel@kanopy-am.com.
> **Livrables** : la présentation (`presentation/Lichen_AM_Presentation_Finale.pptx`), `resultats/Lichen_Portefeuille.xlsx`, `resultats/Lichen_Donnees_complementaires.xlsx`.
> **Soutenance** : 26/11 ou 03/12/2026, 15 min + 5 min de questions. Préparation des questions : `QUESTIONS_JURY.md`.

---

## 1. Démarrer

### Arborescence

| Dossier / fichier | Contenu |
|---|---|
| `code_py/Lichen_AM_V17.ipynb` | **Notebook de référence**, exécuté de bout en bout (étapes 0 à 10, environ 4 minutes). V16 = la même chose sans l'étape 10 (archive). |
| `code_py/extraire_prix_yahoo.py` | Script qui a téléchargé les cours Yahoo Finance (déjà fait, inutile de le relancer). |
| `data/all_data.csv` | Données du cours : MSCI World au 31/12/2024, 1 247 valeurs, 100 colonnes. **Données MSCI du professeur : ne pas diffuser.** |
| `data/externes/` | Données externes : Global Coal Exit List 2026 (urgewald), Global Coal Mine Tracker août 2026 (GEM), cours Yahoo quotidiens du 02/12/2019 au 20/11/2026 (`prix_yahoo_quotidiens.csv`, 1 247 titres + ETF de référence), taux de change EUR (`change_eur.csv`), €STR de la BCE (`estr_bce.csv`, taux sans risque du Sharpe). |
| `resultats/` | Tableaux produits par le notebook (CSV), les deux Excel livrables, et les figures (`figures/G1` à `G14`). |
| `presentation/Lichen_AM_Presentation_Finale.pptx` | **Présentation à envoyer** : 12 slides + 7 en annexe, avec les notes de l'orateur. Version PDF à côté. |
| `presentation/Lichen_AM_Presentation.pptx` | Présentation d'origine (11 slides, étapes 0 à 9). |
| `presentation/ajouter_slides_etape10.py` | Ajoute les slides de l'étape 10 à la présentation d'origine → `Lichen_AM_Presentation_V2.pptx` (19 slides). |
| `presentation/finaliser_presentation.py` | Passe de la V2 à la version finale : slide « objectif », zooms des filtres en annexe, corrections de mise en page. |
| `presentation/mettre_en_forme_excel.py` | Mise en forme des deux Excel (en-têtes, formats %, largeurs). Ne modifie aucune valeur. |

Chaîne complète pour tout reconstruire : notebook V17 → `ajouter_slides_etape10.py` → `finaliser_presentation.py` → `mettre_en_forme_excel.py resultats`.

### Lancer le notebook

Python 3 avec `pandas`, `numpy`, `scipy`, `matplotlib`, `openpyxl`. Ouvrir `Lichen_AM_V17.ipynb` à la racine du projet et tout exécuter. Variables principales :

- `df` : les 1 247 valeurs, avec toutes les colonnes construites (secteur et région en français, `poids_indice`, `ca_vert`, `ITR`, `intensite_s12`, `empreinte_s123`, colonnes `exclu_*`, `eligible_article9`, `univers_financier`, `selectionnable`) ;
- `S` : les **344 entreprises de l'intersection**, avec `score_vert`, `score_financier`, `score_moyen` et leurs rangs ;
- `PF` : le **portefeuille final** (70 lignes, colonnes `poche` et `poids`) ; `CONFORMITE`, `POCHES`, `RESULTATS_EXTRA`, `PERFORMANCE`.

---

## 2. Le principe

Le chemin suit le cours *Approche Quantitative* (J. Jardel) : **univers extra-financier** (filtres d'exclusion) ∩ **univers financier** → **univers sélectionnable** → classement → deux poches → pondération par optimisation sous contraintes.

**Objectif durable (Article 9.3 SFDR)** : réduire les émissions de carbone, avec l'indice **MSCI World Climate Paris Aligned** comme référence. Le mot « Climat » dans le nom impose, selon les orientations de l'ESMA sur les noms de fonds, les exclusions Paris-Aligned : elles sont appliquées.

Règles de mesure, appliquées partout :
- chaque filtre est d'abord **mesuré seul sur tout le MSCI World**, puis on indique ce qu'il retire **en plus** des filtres précédents ;
- « % de l'indice » = **en poids** (capitalisation) ; « entreprises » = **en nombre** ;
- **donnée manquante = exclusion** (prudence) ;
- les seuils **relatifs** (« les X % pires ») sont **comparés au secteur** quand les niveaux diffèrent beaucoup d'un secteur à l'autre (carbone, volatilité).

---

## 3. Étapes 0 à 9 : de l'indice à l'univers sélectionnable

### Étape 1 — Le constat (annexe, slide 13)

Matrice de corrélation (Spearman) entre 15 métriques extra-financières MSCI : **corrélation moyenne 0,14**. **34 %** des entreprises notées AAA (68 sur 201) ont une trajectoire au-dessus de 2 °C. Le CA vert est corrélé à **−0,32** au faible carbone (« paradoxe vert » : les producteurs de solutions émettent). Conclusion : une seule note ne suffit pas, il faut combiner des filtres et raisonner par secteur.

### Étapes 2 à 6 — Les 6 filtres extra-financiers (slide 3 ; zooms en annexe, slides 14 à 19)

| # | Filtre | Règle | Pourquoi | Exclues seul (nb · % indice) | En plus | Il reste |
|---|---|---|---|---|---|---|
| 1 | **Bonne gouvernance** | Note ESG MSCI ≥ BB (on exclut B, CCC, sans note) | SFDR art. 2.17 : bonne gouvernance obligatoire | 27 · 2,6 % | 27 | **1 220 · 97,4 %** |
| 2 | **Ne pas nuire (DNSH)** | Aucune controverse grave : score E, S ou G < 2/10 | SFDR art. 2.17 : pas de préjudice important | 189 · 33,6 % | 174 | **1 046 · 66,0 %** |
| 3 | **Accord de Paris** | Température implicite < 3,1 °C (on exclut les 20 % les plus chaudes, seuil global) | Trajectoire compatible avec Paris | 270 · 15,7 % | 213 | **833 · 55,8 %** |
| 4 | **Exclusions Paris-Aligned** | Armes controversées, tabac, charbon ≥ 1 % du CA (urgewald), mines de charbon (GEM), tout le secteur Énergie, distribution de gaz, électricité carbonée (intensité S1 ≥ 1 000 t/M$ sauf ≥ 50 % de CA vert) | Le mot « Climat » impose les exclusions PAB (ESMA 2025, règlement 2020/1818 art. 12) | 109 · 8,0 % | 33 | **800 · 54,4 %** |
| 5 | **Carbone par secteur** | Exclusion des 10 % les plus émetteurs de **chaque secteur**, en empreinte S1+2+3 **ou** en intensité S1+2+3 (union des deux listes ; seuil calculé sur tout le MSCI) | Figure 11 du cours ; comparer à ses pairs évite le paradoxe vert | 202 · 12,2 % | 94 | **706 · 50,4 %** |
| 6 | **Contribution** | Au moins une « porte » : CA vert ≥ 20 %, ou température ≤ 1,5 °C, ou un ODD environnemental aligné (score MSCI ≥ 2) | SFDR art. 2.17 : un investissement durable doit **contribuer** | 483 · 31,6 % | 211 | **495 · 40,5 %** |

**Résultat : 495 entreprises éligibles Article 9 (40,5 % de l'indice) ; 752 exclues (59,5 %).** Sélectivité ≥ 30 % (label ISR) respectée.

Détails à connaître pour les questions :
- filtre 3 : un seuil par secteur garderait des entreprises jusqu'à 6,1 °C, d'où le seuil global ;
- filtre 4 : nos données n'ont pas la part du CA pétrole et gaz, donc on exclut **tout le secteur Énergie** (plus strict que la règle) ; le charbon vient de sources externes (urgewald GCEL 2026, GEM Coal Mine Tracker) ;
- filtre 5 : 65 entreprises exclues sur l'empreinte, 27 sur l'intensité seulement, 2 pour donnée manquante (parmi les 94 nouvelles) ;
- filtre 6 : seules 82 entreprises du MSCI World ont ≥ 20 % de CA vert, d'où les deux autres portes.

### Étape 8 — Les filtres financiers et l'intersection (slide 4)

Univers financier construit **sur tout le MSCI World**, indépendamment des filtres extra-financiers :

| Filtre | Règle | Exclues seul | En plus | Il reste |
|---|---|---|---|---|
| Rentabilité | ROIC > 0 (ROE pour la finance) et marge nette > 0 | 112 | 112 | 1 135 · 95,9 % |
| Bilan | Dette / actif ≤ 60 % (70 % immobilier et services aux collectivités ; pas de règle pour la finance) | 52 | 51 | 1 084 · 92,1 % |
| Risque | Volatilité 5 ans hors des 10 % pires **du secteur**, et perte maximale 5 ans > −70 % | 171 | 119 | 965 · 83,6 % |
| Liquidité | Poids dans le MSCI World ≥ 0,01 % | 147 | 105 | 860 · 82,9 % |
| Historique de cours | Cours Yahoo sur ≥ 95 % des **semaines** 2020-2024 | 87 | 35 | **825 · 81,8 %** |

> **Point de méthode** : mesuré en *jours*, l'historique excluait 276 entreprises dont 154 japonaises **sans aucune donnée manquante** (la bourse de Tokyo a plus de jours fériés, comptés comme des trous dans le calendrier commun). Mesuré en semaines, le biais disparaît.

**Intersection (tableau croisé)** :

| | Solide financièrement | Exclue par le financier |
|---|---|---|
| **Éligible Article 9** | **344 · 35,9 % → univers sélectionnable** | 151 · 4,6 % |
| **Exclue extra-financier** | 481 · 46,0 % | 271 · 13,5 % |

Le financier ne coûte que 4,6 points d'indice : la sélectivité vient de l'extra-financier.

### Étape 9 — Le classement des 344 (slide 5)

Aucune exclusion à cette étape : chaque entreprise de l'intersection reçoit **trois notes**, comparées à son secteur (rang centile au sein de l'intersection, de 0 à 100) :

| Score | Composantes (moyenne des rangs) |
|---|---|
| **Score vert** | CA vert ; température implicite (inversée) ; intensité carbone S1+2 (inversée) ; alignement ODD environnementaux (6, 7, 11 à 15) |
| **Score financier** | Rentabilité (ROIC, ROE pour la finance) ; ratio de Sharpe 5 ans ; rendement du cash-flow libre ; volatilité 5 ans (inversée) |
| **Score moyen** | 50 % score vert + 50 % score financier (paramètre `POIDS_VERT` dans le notebook) |

Les deux notes sont presque indépendantes (corrélation **0,07**) : d'où l'intérêt de deux poches.

Podiums : **vert** AECOM, Dassault Systèmes, Jacobs ; **financier** Iberdrola, Public Storage, Holcim ; **moyenne** Iberdrola, Novartis, Zurich.

Fichier : **`resultats/classement_lichen.csv`** (344 lignes). La colonne `ligne_all_data` est l'index de la ligne dans `all_data.csv` / `df`.

---

## 4. Étape 10 : les deux poches, la pondération, les résultats (slides 6 à 12)

### 10.0 Revue qualitative : 344 → 339 candidates

Les données MSCI ne voient pas tout. Avant de construire les poches, on relit l'univers et on écarte des **activités** (pas des entreprises au cas par cas) qui contredisent l'objectif climat et biodiversité, même avec de bonnes notes :

| Entreprise | Activité écartée |
|---|---|
| Agnico Eagle Mines, Wheaton Precious Metals | Or (mines, redevances, bijouterie) |
| Mowi | Saumon d'élevage en mer |
| Inditex | Fast fashion |
| Amadeus IT Group | Croisières et réservation de vols |

Fichier : `resultats/` → feuille `revue_qualitative` de l'Excel des données complémentaires.

### 10.1 Les deux poches : 70 lignes

L'architecture du lichen : deux partenaires qui survivent ensemble là où aucun ne survivrait seul.

| Poche | Règle de sélection | Lignes | Poids |
|---|---|---|---|
| **Photosynthèse** (l'algue) | Les 25 meilleures en **score vert**, parmi celles qui font **au moins 10 % de CA vert**, **5 au plus par secteur** | 25 | **55 %** |
| **Noyau** (le champignon) | Les 45 meilleures en **score financier** parmi les autres, avec un nombre de lignes par secteur **proportionnel au poids du secteur dans le MSCI World** (hors Énergie, exclu) ; banques et assureurs gardés | 45 | **45 %** |

- Le seuil de 10 % de CA vert évite que des entreprises sans aucun CA vert (Novartis, Novo Nordisk, Swisscom, Zurich) entrent dans la poche verte grâce à leur seule trajectoire. À 20 %, il ne resterait que 29 candidates concentrées dans 3 secteurs.
- Photosynthèse : CA vert moyen **27,4 %**, 1,77 °C, score vert moyen 76. Noyau : score financier moyen **71**, 1,59 °C, CA vert 3,6 %.

### 10.2 La pondération : minimiser la tracking error (méthode du cours, *Approche Quantitative* p. 63)

Poids de départ égaux (1/N), somme des poids = 1, **chaque ligne entre 0,5 % et 5 %**, et on minimise la **tracking error ex ante face au MSCI World** :

$$\min_w \; (w - b)^\top \Sigma \,(w - b) \; + \; \lambda \sum_i \frac{(w_i - c_i)^2}{c_i}$$

avec `b` les poids du MSCI World (les 1 247 valeurs), `w` les poids du fonds, et un petit terme de rappel (λ = 0,3) vers une cible de conviction `c` (Photosynthèse au prorata du score vert, Noyau au prorata de √poids indice × score financier). Sans ce terme, l'optimiseur met la moitié des lignes au plancher. Résolution : `scipy.optimize.minimize`, méthode SLSQP.

**Matrice de covariance Σ** : rendements **hebdomadaires en euros 2020-2024** (connus au 31/12/2024, pas de biais d'anticipation), rétrécissement de 30 % vers une corrélation constante. Pour les rares titres sans cours : volatilité 5 ans d'`all_data`, corrélation 0,5 dans un secteur, 0,3 entre secteurs.

**Contraintes** (toutes vérifiées sur les poids finaux, voir 10.4) :

| Contrainte | Valeur | Origine |
|---|---|---|
| Poids par ligne | 0,5 % à 5 % | OPCVM 5/10/40 : aucune ligne > 5 %, donc la règle des 40 % est respectée d'office |
| Température implicite du fonds | **< 2 °C** | Accord de Paris : « bien en dessous de 2 °C » |
| Intensité carbone S1+2 et empreinte S1+2+3 | ≤ 50 % du MSCI World | Paris-Aligned (−50 %) |
| Secteurs à fort impact climatique | ≥ exposition du MSCI World | Paris-Aligned (énergie, matériaux, industrie, services aux collectivités, immobilier, consommation) |
| Part de CA vert | ≥ 1,5 × MSCI World (≥ 13,9 % vs 9,2 %) | Objectif de contribution |
| Écart par secteur | ± 5 points vs MSCI World | Équilibre du fonds |
| Écart par région | ± 10 points vs MSCI World | Équilibre du fonds |

### 10.3 La taille de la poche verte : 55 %

On choisit la taille de la poche **comme on choisit les poids : en minimisant la tracking error.** On teste une poche Photosynthèse de 20 % à 70 % ; parmi les tailles qui respectent **toutes** les règles, on garde la tracking error la plus faible.

| Poche verte | 20 % | 25 % | 30 % | 35 % | 40 % | 45 % | 50 % | **55 %** | 60 % | 65 % | 70 % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tracking error ex ante | 5,3 % | 4,7 % | 4,7 % | 4,7 % | 4,7 % | 4,8 % | 4,7 % | **4,6 %** | 4,7 % | 5,0 % | 5,1 % |
| CA vert du fonds | 13,3 % | 13,9 % | 13,9 % | 13,9 % | 13,9 % | 13,9 % | 15,2 % | **16,7 %** | 18,1 % | 19,0 % | 19,0 % |
| Règles respectées | 8/12 | 12 | 12 | 12 | 12 | 12 | 12 | **12** | 12 | 12 | 10/12 |

- À 20 %, le CA vert est insuffisant ; à 70 %, l'équilibre sectoriel casse.
- Entre les deux, la tracking error bouge à peine (4,6 % à 5,0 %) : **le vert ne coûte presque rien en risque**.

**Et 1,5 °C ?** Testé (`resultats/comparaison_temperature.csv`) : faisable, mais moins bon sur presque tout.

| | Plafond 2 °C (retenu, poche verte 55 %) | Plafond 1,5 °C (poche verte 50 %) |
|---|---|---|
| Tracking error ex ante | **4,6 %** | 5,5 % |
| Température | 1,69 °C | 1,50 °C |
| Empreinte carbone vs MSCI World | −62 % | −66 % |
| CA vert | **16,7 %** | 13,9 % |
| Part notée AA ou AAA | **74 %** | 66 % |
| Lignes bloquées au plafond de 5 % | 2 | 5 |

### 10.4 Le portefeuille final et la conformité (slides 6 à 8, 10)

**12 règles sur 12 respectées** :

| Cadre | Règle | Fonds | Limite |
|---|---|---|---|
| SFDR Article 9 | 100 % d'investissements durables | 100 % | 100 % |
| OPCVM 5/10/40 | Aucune ligne au-dessus de 10 % | 5,0 % | ≤ 10 % |
| OPCVM 5/10/40 | Lignes au-dessus de 5 % : total ≤ 40 % | 0 % | ≤ 40 % |
| Paris-Aligned | Exclusions (charbon, pétrole, gaz, électricité carbonée, tabac, armes controversées) | 0 ligne | 0 |
| Paris-Aligned | Empreinte carbone S1+2+3 | −62 % | ≤ −50 % |
| Paris-Aligned | Intensité carbone S1+2 | −52 % | ≤ −50 % |
| Paris-Aligned | Secteurs à fort impact climatique | 48 % vs 39 % | ≥ indice |
| Accord de Paris | Température implicite | 1,69 °C | < 2 °C |
| Contribution | CA vert | 16,7 % vs 9,2 % | ≥ 13,9 % |
| Équilibre | Écart par secteur | max 5,0 pts | ≤ 5 pts |
| Équilibre | Écart par région | max 10,0 pts | ≤ 10 pts |
| Diversification | Poids par ligne | 0,5 % à 5,0 % | 0,5 % à 5 % |

> Plusieurs contraintes sont **saturées** (intensité à −52 %, secteurs et régions pile à la limite) : c'est normal en optimisation, l'optimiseur va au bout de ce qui est permis pour réduire la tracking error.

- **Plus grosses lignes** : Microsoft et Alphabet (5 %, Noyau), puis Autodesk, NVIDIA, ServiceNow, AMD, AECOM, Jacobs, WSP, Xylem (≈ 3 %, Photosynthèse).
- **Secteurs** : industrie, services aux collectivités, matériaux et immobilier à +5 points ; finance et santé à −5 points ; énergie à 0 %.
- **Régions** : Amérique du Nord 66 % (−10 points), Europe 26 % (+10 points), Japon 6 %, Asie-Pacifique et Moyen-Orient 2 %.

### 10.5 Résultats extra-financiers (slide 9)

| Indicateur | Fonds | MSCI World | Écart |
|---|---|---|---|
| Température implicite | 1,69 °C | 2,40 °C | −29 % |
| Intensité carbone S1+2 (tCO2e / M$ de CA) | 46 | 96 | −52 % |
| Empreinte carbone S1+2+3 (tCO2e / M$ investi) | 582 | 1 522 | −62 % |
| CA vert | 16,7 % | 9,2 % | +81 % |
| Part notée AA ou AAA | 74 % | 45 % | |
| Note ESG MSCI moyenne (1 = CCC … 7 = AAA) | 6,1 | 5,2 | |
| Part en controverse grave | 0 % | 33 % | |
| Exposition aux exclusions Paris-Aligned (dont fossiles) | 0 % | 8,0 % | |

### 10.6 Performance passée (slide 11)

Cours Yahoo **mensuels** convertis en euros, poids **remis à la cible chaque mois**, **frais de gestion de 0,75 % par an déduits**. Références : MSCI World (ETF `IWDA.AS`) et deux ETF MSCI World Paris-Aligned (`PABV.DE`, `PABW.DE`). Taux sans risque : €STR (BCE).

| | Fonds | MSCI World | PABV | PABW |
|---|---|---|---|---|
| **2020-2024** (période qui a servi à choisir : flatteuse) — annualisé | +19,4 % | +13,2 % | – | – |
| **01/2025 → 20/11/2026** (vrai test, hors échantillon) — cumulé | **+10,4 %** | +17,8 % | +16,1 % | +12,0 % |
| 2025-2026 — annualisé | +5,3 % | +8,9 % | +8,1 % | +6,1 % |
| 2025-2026 — volatilité | **11,3 %** | 13,6 % | 17,6 % | 14,4 % |
| 2025-2026 — perte maximale (fin de mois) | **−10,2 %** | −13,7 % | −16,1 % | −14,3 % |
| 2025-2026 — Sharpe | 0,28 | 0,50 | 0,34 | 0,27 |
| 2025-2026 — tracking error ex post | 8,0 % | – | 5,8 % | 2,7 % |

Lecture honnête : sur la vraie période de test, le fonds fait **moins bien que le MSCI World**, dont la hausse a été portée par l'IA et les très grandes capitalisations américaines (le fonds est sous-pondéré de 10 points en Amérique du Nord et exclut Apple, Amazon, Meta, Tesla). Il est en revanche **moins volatil et baisse moins**, et reste proche de l'ETF Paris-Aligned PABW. Biais assumés : univers fixé au 31/12/2024 (biais du survivant), coûts de transaction non comptés.

**Indicateur de risque (SRI) : 4 sur 7.** Volatilité du fonds sur 5 ans ≈ 15,5 % ; selon la méthode PRIIPs, une volatilité équivalente entre 12 % et 20 % correspond à la classe de risque de marché 4 (risque de crédit négligeable pour un fonds actions).

### 10.7 Présentation finale

12 slides pour 15 minutes, puis l'annexe pour les questions :

| # | Slide | # | Slide |
|---|---|---|---|
| 1 | Titre : Lichen Symbiose Climat | 7 | La pondération et la taille de la poche verte |
| 2 | **Notre objectif durable : le climat** | 8 | Le portefeuille : secteurs, régions, top 10 |
| 3 | Les 6 filtres extra-financiers | 9 | Résultats extra-financiers |
| 4 | Les filtres financiers et l'intersection | 10 | Conformité : 12 règles sur 12 |
| 5 | La carte de la symbiose (344 entreprises) | 11 | Performance passée |
| 6 | Deux poches, une symbiose | 12 | Le fonds en bref + mentions AMF |
| 13 | Annexe · Une seule note ESG ne suffit pas | 14-19 | Annexe · Zoom sur chacun des 6 filtres |

Mentions AMF présentes : document à caractère promotionnel ; société de gestion et fonds fictifs ; risque de perte en capital ; performances simulées ; les performances passées ne préjugent pas des performances futures ; consulter le DIC et le prospectus ; SRI 4/7.

---

## 5. Limites à connaître

- **Données arrêtées au 31/12/2024** : notes ESG, températures et CA vert ne sont pas mis à jour sur 2025-2026.
- **Biais du survivant** et **2020-2024 dans l'échantillon** : la performance 2020-2024 sert à illustrer, pas à prouver.
- **Proxy « secteurs à fort impact »** : nous utilisons les secteurs GICS, pas les codes NACE du règlement 2020/1818.
- **Trajectoire de décarbonation de −7 % par an** des indices Paris-Aligned : non testée (une seule date de données). En gestion réelle, on la suivrait à chaque revue annuelle.
- **CA vert** = maximum entre la part du CA en technologies propres (`CT_TOTAL_MAX_REV`) et la part estimée alignée sur la Taxonomie européenne (`EST_EU_TAXONOMY_MAX_REV`), toutes deux MSCI, en estimation **haute** (« MAX »). C'est cette donnée qui fait entrer NVIDIA (78 %) et AMD (29 %) dans la poche verte ; voir `QUESTIONS_JURY.md`.

Les réponses préparées aux questions probables du jury sont dans **`QUESTIONS_JURY.md`**.
