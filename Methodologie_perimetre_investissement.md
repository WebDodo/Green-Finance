# Holocène Actions Monde — Méthodologie de sélection extra-financière

*Lichen AM · Projet final Finance durable · Université Paris-Dauphine · 2026*

> **Investir dans les limites de la planète.**

Ce document explique, étape par étape, **comment on passe des 1 247 entreprises du MSCI World aux 404 entreprises qui ont le droit d'entrer dans le fonds** (notre **périmètre d'investissement**), **puis aux 125 meilleures**, transmises à l'analyse financière. Pour chaque règle, on donne **le seuil, la donnée utilisée, ce qu'elle mesure et pourquoi on l'a choisie**.

**Sommaire**
1. Lichen AM et le fonds Holocène
2. L'objectif : les 9 limites planétaires
3. Les données utilisées : lexique
4. L'entonnoir en un coup d'œil
5. Étape A : ce qu'on refuse
6. Étape B : le test « investissement durable » (Article 9)
7. Notre périmètre d'investissement (404)
8. Étape C : le classement, score Holocène
9. Étape D : la revue qualitative
10. La sélection finale (125)
11. Le niveau d'exigence de nos critères
12. Les limites que nous assumons
13. Sources et code

---

## 1. Lichen AM et le fonds Holocène

| | |
|---|---|
| **Société de gestion** | **Lichen AM**. Le lichen est un **bio-indicateur** : il ne pousse que là où l'air est sain, et les scientifiques s'en servent pour mesurer la santé d'un écosystème. C'est notre méthode : **mesurer avant d'investir**. Le lichen pousse lentement (le long terme) et naît d'une symbiose entre un champignon et une algue (la coopération). |
| **Fonds** | **Holocène Actions Monde**. L'Holocène est l'époque de climat stable dans laquelle vit l'humanité depuis environ 11 700 ans, et qui a permis l'agriculture et les civilisations. Le fonds investit pour que l'économie reste dans les limites qui garantissent cette stabilité. |
| **Forme** | FCP de droit français, OPCVM (UCITS), actions monde, long only, sans levier, liquidité quotidienne |
| **Classification** | SFDR **Article 9.3** : objectif de réduction des émissions de carbone, avec un indice Paris-Aligned |
| **Indice de référence** | MSCI World Climate Paris Aligned |
| **Univers de départ** | MSCI World au 31/12/2024 : **1 247 entreprises** (`all_data.csv`) |

### Nos deux règles d'or

> 1. **Notre expertise, c'est l'environnement : c'est là que nous allons au-delà de la réglementation. Sur le social et la gouvernance, nous appliquons le socle de garanties exigé par SFDR et le règlement Paris-Aligned : respect du Pacte mondial de l'ONU et des principes de l'OCDE, gouvernance saine.**
> 2. **On n'investit pas dans ce qu'on ne mesure pas.**

### Pourquoi l'Article 9.3, aligné avec l'Accord de Paris

L'Article 9 n'impose pas d'être aligné avec Paris. Nous le faisons quand même, pour 5 raisons :
1. **Crédibilité :** un fonds « limites planétaires » qui détiendrait Glencore, l'un des plus gros mineurs de charbon du monde, serait indéfendable, même si c'est légal.
2. **Attentes du marché :** le label ISR et la plupart des investisseurs exigent de toute façon l'exclusion des énergies fossiles.
3. **Anticipation :** la réforme SFDR 2.0, proposée fin 2025, prévoit d'imposer ces exclusions à tous les fonds « durables ».
4. **Coût quasi nul :** il suffit de quelques vérifications en plus.
5. **Un chiffre fort :** au moins 50 % de carbone en moins que le marché.

---

## 2. L'objectif : les 9 limites planétaires

### L'objectif d'investissement durable (Article 9)

> *Le fonds a pour objectif d'investissement durable de contribuer à maintenir l'économie dans les **limites planétaires**, en investissant dans des entreprises qui contribuent de manière mesurable à l'atténuation du changement climatique, à la protection des ressources en eau ou à l'économie circulaire, sans porter atteinte de manière significative aux autres limites, notamment la biodiversité.*

Les **limites planétaires** (Rockström et al., 2009, mises à jour par Richardson et al., 2023) sont les **9 seuils** à ne pas dépasser pour que la Terre reste aussi stable qu'à l'Holocène. **7 sur 9 sont déjà dépassées.** Le fonds les couvre **toutes les 9**, de trois façons :

| Limite planétaire | Dépassée ? | Comment le fonds la couvre | Comment |
|---|---|---|---|
| 🌡️ **Changement climatique** | 🔴 Oui | **Directement** : contribution + exclusions | ODD 13, ODD 7, température implicite, intensité carbone ; exclusion des fossiles et de l'aérien |
| 💧 **Eau douce** | 🔴 Oui | **Directement** : contribution | ODD 6 |
| ♻️ **Nouvelles entités** (plastiques, produits chimiques, déchets) | 🔴 Oui | **Directement** : contribution | ODD 12, chiffre d'affaires vert ; exclusion de la fast fashion |
| 🌿 **Intégrité de la biosphère** (biodiversité) | 🔴 Oui | **Directement** : garde-fou (ne pas nuire) | ODD 14, ODD 15 ; exclusion de l'or et du saumon d'élevage |
| 🌳 **Changement d'usage des sols** (déforestation) | 🔴 Oui | Par les exclusions sectorielles | Exclusion du négoce agricole industriel (soja, huile de palme) et de l'automobile ; ODD 15 |
| 🧪 **Flux d'azote et de phosphore** (engrais) | 🔴 Oui | Par les exclusions | Exclusion du négoce agricole industriel ; aucun producteur d'engrais (Nutrien, Yara, CF Industries, Mosaic, Corteva) dans le périmètre |
| 🌊 **Acidification des océans** | 🔴 Oui | Par le climat | Elle est causée par le CO2 : réduire le CO2, c'est la freiner. Plus ODD 14 |
| 🌫️ **Aérosols** (particules dans l'air) | 🟢 Non | Par les exclusions fossiles | Ils viennent surtout de la combustion du charbon et du pétrole |
| 🛡️ **Couche d'ozone** | 🟢 Non, elle se reconstitue | Non suivie | Le problème est réglé par le Protocole de Montréal (1987) |

**En résumé :** **4 limites suivies directement** avec des données, **4 couvertes par nos exclusions**, et **1 non suivie** parce qu'elle n'est pas dépassée.

---

## 3. Les données utilisées : lexique

### Les scores ODD (Objectifs de développement durable) de MSCI

L'ONU a fixé **17 Objectifs de développement durable (ODD, ou SDG en anglais)** pour 2030. MSCI note chaque entreprise sur chacun des 17. Le **score net d'alignement** va de **−10 à +10**. Il combine deux choses :
- **ce que l'entreprise vend** : ses produits aident-ils ou nuisent-ils à l'objectif ?
- **comment elle fonctionne** : ses politiques, ses pratiques, ses objectifs.

| Score | Catégorie MSCI | Notre usage |
|---|---|---|
| ≥ 5 | Fortement aligné | Compte **plus** dans le score Holocène (étape C) : un ODD à 6 rapporte 3 fois plus de points qu'un ODD à 2 |
| **≥ 2** | **Aligné** | **Seuil de contribution** (étape B) |
| entre −2 et 2 | Neutre | Ni contribution, ni nuisance : l'ODD n'ouvre pas de porte d'entrée, mais ne bloque pas non plus. Un score entre 0 et 2 compte quand même un peu dans le score Holocène |
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

*Les 11 autres ODD (pauvreté, santé, éducation, égalité…) sont des ODD sociaux. Ils sont couverts par nos garanties sociales (controverses, Pacte mondial), et non par notre objectif environnemental.*

### Les autres données

| Donnée | Ce qu'elle mesure | Unité / échelle | Colonne |
|---|---|---|---|
| **Température implicite (ITR)** | Le réchauffement en 2100 **si toute l'économie se comportait comme cette entreprise**, au vu de ses émissions (scopes 1, 2 et 3) et de ses objectifs. 1,5 °C = aligné avec Paris | °C (de 1,3 à 10 dans nos données) | `ITR` |
| **Intensité carbone, scope 1** | Émissions **directes** : usines, véhicules, chaudières | tCO2e par M$ de chiffre d'affaires | `INTENSITY_SCOPE_1` |
| **Intensité carbone, scope 2** | Émissions de l'**électricité et de la chaleur achetées** | tCO2e par M$ | `INTENSITY_SCOPE_2` |
| **Intensité carbone, scope 3** | Émissions de **toute la chaîne de valeur** : fournisseurs, transport, **usage des produits vendus** | tCO2e par M$ | `INTENSITY_SCOPE_3` |
| **Chiffre d'affaires vert** | Part du chiffre d'affaires **alignée avec la Taxonomie européenne**, la liste officielle de l'UE des activités « vertes » (estimation MSCI, haut de fourchette) | % | `EST_EU_TAXONOMY_MAX_REV` |
| **Score de controverse** | La gravité des scandales récents de l'entreprise (pollution, accidents, procès…) | de 0 à 10 : **0 = 🔴 rouge** (très grave), **1 = 🟠 orange** (grave), 2 à 4 = 🟡 jaune, 5 à 10 = 🟢 vert | `ENVIRONMENT_`, `SOCIAL_`, `GOVERNANCE_CONTROVERSY_SCORE` |
| **Note de pilier gouvernance** | La qualité de la gouvernance : conseil d'administration, rémunérations, éthique, fiscalité | de 0 à 10 | `GOVERNANCE_PILLAR_SCORE` |
| **Note ESG globale** | La note ESG de MSCI | de CCC à AAA | `IVA_COMPANY_RATING` |
| **Tabac** | L'entreprise produit-elle du tabac ? | oui / non | `TOB_PRODUCER` |
| **Armes controversées** | Liens avec les mines antipersonnel, les armes à sous-munitions, chimiques ou biologiques | oui / non | `CWEAP_TIE` |
| **Secteur et groupe d'industrie** | La classification GICS (11 secteurs) et le groupe d'industrie (64 groupes) | texte | `gics_sector_name`, `industry_group` |

**Pourquoi la Taxonomie européenne pour le chiffre d'affaires vert :** c'est la **référence réglementaire européenne**. MSCI fournit aussi une mesure « technologies propres », mais elle n'est jamais plus stricte et n'est pas une norme officielle.

### Les bases externes (ce que MSCI ne voit pas)

| Base | Ce qu'elle apporte | Utilisée en |
|---|---|---|
| **Global Coal Exit List 2026** (urgewald) | Part du chiffre d'affaires issue du **charbon** pour ~1 500 maisons mères | A1 |
| **Global Coal Mine Tracker**, août 2026 (Global Energy Monitor) | Chaque mine de charbon du monde, avec ses **propriétaires** et leur part | A1 |
| **Banking on Climate Chaos 2026**, **Still Burning** (urgewald) et trackers Reclaim Finance | Financements fossiles et politiques des grandes banques | A2 (justification) |

---

## 4. L'entonnoir en un coup d'œil

```
1 247  entreprises du MSCI World (31/12/2024)
  │
  │  ÉTAPE A · CE QU'ON REFUSE (données MSCI + bases charbon)
  │  ├─ A1  Énergies fossiles ........................... − 116
  │  ├─ A2  Financement des énergies fossiles ........... − 197
  │  ├─ A3  Secteurs incompatibles ...................... −  49
  │  └─ A4  Garde-fous ................................... −  44
  ▼
  841  entreprises investissables
  │
  │  ÉTAPE B · TEST « INVESTISSEMENT DURABLE » (Article 9)
  │  ├─ Case 1  Contribue à une limite planétaire ?
  │  ├─ Case 2  Ne nuit pas aux autres ?
  │  └─ Case 3  Gouvernance ? ............................ − 437
  ▼
  404  entreprises éligibles  =  NOTRE PÉRIMÈTRE
  │
  │  ÉTAPE C · CLASSEMENT : SCORE HOLOCÈNE (0-100), on garde ≥ 60 ... − 272
  ▼
  132
  │
  │  ÉTAPE D · REVUE QUALITATIVE (or, saumon, fast fashion, croisières, vols) ... − 7
  ▼
  125  entreprises sélectionnées  →  filtres financiers, puis pondération
```

*Les exclusions sont appliquées dans l'ordre : une entreprise exclue pour plusieurs motifs n'est comptée qu'une fois, dans la première règle qui l'exclut.*

**Un principe :** toutes les règles des étapes A à C sont **automatiques**, calculées à partir des données (MSCI et bases charbon). **Aucun nom d'entreprise n'est écrit à la main**, sauf à l'étape D, la revue qualitative, faite à la fin et documentée.

---

## 5. Étape A — Ce qu'on refuse

On retire d'emblée ce qui est incompatible avec le fonds, **avant même de regarder ce que l'entreprise apporte**.

### A1. Les énergies fossiles — 116 exclues *(obligatoire en Article 9.3)*

Le règlement Paris-Aligned (règlement délégué UE 2020/1818, art. 12) impose d'exclure les entreprises qui tirent **≥ 1 % de leur chiffre d'affaires du charbon** (houille et lignite, y compris le charbon métallurgique), **≥ 10 % du pétrole**, **≥ 50 % du gaz**, ou **≥ 50 % d'une électricité émettant plus de 100 gCO2e/kWh**.

| Règle | Seuil | Donnée | Pourquoi ce seuil | Exclues |
|---|---|---|---|---|
| ⛽ **Pétrole et gaz** | Tout le secteur, sans seuil | `gics_sector_name` = Energy | **Plus strict** que la règle officielle (10 % / 50 %) : nos données n'ont pas la part de chiffre d'affaires pétrole et gaz, et un fonds « limites planétaires » ne garde aucun pétrolier | 52 |
| 🏭 **Électricité carbonée** | Un électricien est **gardé** seulement si : chiffre d'affaires vert **≥ 50 %**, **ou** scope 1 **< 100 tCO2e par M$** | `EST_EU_TAXONOMY_MAX_REV`, `INTENSITY_SCOPE_1` | **Approximation** de la règle officielle en gCO2/kWh, une donnée absente de notre base. Le seuil de 100 laisse passer les réseaux et l'eau, qui émettent peu | 51 |
| ⚫ **Charbon** | **≥ 1 %** du chiffre d'affaires | Global Coal Exit List 2026 | **Seuil officiel** Paris-Aligned. Nos données MSCI n'ont **aucune colonne charbon** | 5 |
| ⛏️ **Mines de charbon**, thermique **et métallurgique** | Détenir **≥ 10 %** d'une mine **en activité**, produisant **> 0,5 Mt/an** | Global Coal Mine Tracker | Cette base donne la propriété des mines, pas le chiffre d'affaires. 10 % : en dessous, c'est une participation sans contrôle. 0,5 Mt : en dessous, c'est une toute petite mine | 8 |

**Comment on croise :** on met les noms en minuscules et on enlève les mots comme « plc », « inc », « ltd » pour comparer les noms MSCI et ceux des bases charbon (« Glencore PLC » = « Glencore plc »). Dans le Global Coal Mine Tracker, les propriétaires sont écrits « BHP [50%]; Mitsubishi Corp [50%] » : on lit la part de chacun.

**Qui tombe grâce aux bases charbon (13 entreprises) :**
- **Global Coal Exit List :** Glencore (3,2 % du CA, 98 Mt/an), BHP (3,2 %), CSX (13 %, transport de charbon), Berkshire Hathaway (1,7 %, centrales et transport), Jardine Matheson (10 %, mines indonésiennes).
- **Global Coal Mine Tracker :** Anglo American (88 % des mines Grosvenor et Moranbah North), Mitsubishi Corp (50 % des mines BMA), Mitsui & Co, ITOCHU, Sumitomo Corp, Marubeni, Nippon Steel, JFE.

**Pourquoi c'était nécessaire :** les miniers de charbon ne sont **pas** dans le secteur Énergie. Ils sont classés en Matériaux (Glencore, BHP, Anglo American) ou en Industrie (les maisons de commerce japonaises).

**Pourquoi 1 % :** c'est strict, mais c'est le seul seuil qui exclut les géants. Avec 5 %, **Glencore, qui produit 98 millions de tonnes de charbon par an**, passerait : le charbon ne pèse que 3,2 % de son énorme chiffre d'affaires.

**Bon à savoir :** South32 n'est **pas** exclue. Elle a **vendu** ses mines de charbon d'Illawarra. Croiser plusieurs sources évite d'exclure une entreprise qui a déjà changé.

### A2. Le financement des énergies fossiles — 197 exclues

| Règle | Donnée | Exclues |
|---|---|---|
| 🏦 Banques | `industry_group` = Banks | 74 |
| 🛡️ Assureurs et courtiers | `industry_group` = Insurance | 64 |
| 📈 Gestionnaires d'actifs, crédit, cartes, bourses, capital-investissement, holdings | Reste du secteur `Financials` | 59 |

**Pourquoi :** une banque ou un assureur pollue peu lui-même, mais **finance, assure ou détient** des entreprises fossiles. En 2025, les 65 plus grandes banques du monde ont financé **906 milliards de dollars** d'énergies fossiles (*Banking on Climate Chaos 2026*). Même BNP Paribas (186 M$) et Crédit Agricole (153 M$) ont financé le développement du charbon métallurgique entre 2022 et 2024 (*Still Burning*, urgewald). Pourtant, nos données donnent à Goldman Sachs une intensité carbone scope 3 de **0,7 tCO2e par M$**, contre 494 en médiane pour l'industrie. **MSCI mesure leurs bureaux, pas leurs prêts.**

Plutôt que de faire confiance à un chiffre faux, nous les excluons : **on n'investit pas dans ce qu'on ne mesure pas.**

**L'exception :** on garde les financières classées dans les groupes **« Commercial Services » et « Software »** : les **services de paiement et les agences de notation** (PayPal, Fiserv, Block, Edenred, Nexi, S&P Global, Moody's…). Elles se rémunèrent par commission et ne financent pas d'entreprises.

*Visa, Mastercard et les bourses sont classées avec les gestionnaires d'actifs (« Diversified Financial Services ») : nos données ne permettent pas de les distinguer, elles sont donc exclues aussi.*

### A3. Les secteurs incompatibles avec les limites planétaires — 49 exclues

> **On exclut les secteurs dont le modèle économique dépasse les limites planétaires, sans alternative durable à grande échelle.**

| Secteur | Groupe d'industrie | Limites planétaires dépassées | Exclues |
|---|---|---|---|
| ✈️ **Aérien** | Airlines | **Climat** : kérosène, aucune alternative propre avant des décennies | 7 |
| 🚗 **Automobile**, électrique comprise | Auto Manufacturers, Auto Parts&Equipment | **Ressources** (300 à 500 kg de métaux par batterie), **usage des sols** (routes, parkings, étalement urbain), **biodiversité** (mines de lithium et de nickel), particules de pneus et de freins | 34 |
| 🌾 **Négoce agricole industriel** | Agriculture | **Usage des sols** (déforestation : soja, huile de palme), **biodiversité**, **azote et phosphore** (ADM, Bunge, Wilmar ; ce groupe contient aussi les cigarettiers) | 8 |

**Pourquoi la voiture électrique aussi :** elle décarbone l'usage, mais pas le reste : les métaux, les sols, les routes. Notre fonds suit les **9 limites planétaires**, pas seulement le climat. Une voiture électrique de plus reste une voiture de plus.

**Et la fast fashion, les croisières ?** Nos données ne les distinguent pas : Zara est classée « Retail » comme un supermarché, Carnival « Leisure Time » comme un fabricant de vélos. Elles sont traitées par la **revue qualitative** (étape D).

### A4. Les garde-fous — 44 exclues

| Famille | Règle et seuil | Donnée | Pourquoi ce seuil | Exclues |
|---|---|---|---|---|
| ❓ **Données manquantes** | Pas de note ESG, de température implicite ou d'intensité scope 1 | `IVA_COMPANY_RATING`, `ITR`, `INTENSITY_SCOPE_1` | **On n'investit pas dans ce qu'on ne mesure pas** | 9 |
| 🔴🟠 **Controverses environnementales** | Score **≤ 1** (rouge ou orange) | `ENVIRONMENT_CONTROVERSY_SCORE` | **Notre expertise :** beaucoup de fonds n'excluent que le rouge. Exemples : Coca-Cola, Nestlé, Bayer | 15 |
| 🔴 **Controverses sociales et de gouvernance** | Score **= 0** (rouge) | `SOCIAL_` et `GOVERNANCE_CONTROVERSY_SCORE` | **Garanties sociales :** nous excluons les violations du Pacte mondial de l'ONU et des principes de l'OCDE (droits humains, droit du travail, corruption), comme l'impose le règlement Paris-Aligned. Le drapeau rouge MSCI signale ces violations | 2 |
| 🚬 **Tabac** | Toute production | `TOB_PRODUCER` | Obligatoire en Paris-Aligned *(les cigarettiers sont déjà sortis en A3)* | 0 |
| 💣 **Armes controversées** | Tout lien | `CWEAP_TIE` | Obligatoire en Paris-Aligned | 5 |
| 🌿💧♻️ **Atteinte grave à une autre limite** | ODD 6, 12, 14 **ou** 15 **≤ −5** | `SDG_06`, `SDG_12`, `SDG_14`, `SDG_15` | Seuil MSCI « fortement désaligné » | 13 |

*Comptage dans l'ordre du tableau, après les familles A1 à A3.*

**→ Résultat de l'étape A : 406 entreprises exclues, 841 investissables.**

---

## 6. Étape B — Le test « investissement durable » (Article 9)

Pour un Article 9, **chaque** entreprise du fonds doit être un **investissement durable** au sens de l'**article 2.17 de SFDR**. La définition a trois conditions : **contribuer** à un objectif environnemental ou social, **ne pas nuire significativement** aux autres objectifs (le principe **DNSH**, « Do No Significant Harm »), et appliquer des **pratiques de bonne gouvernance**. C'est un examen en oui ou non : il faut cocher **les 3 cases**.

### Case 1 — Elle contribue à au moins une limite planétaire

Il suffit d'**une** de ces 5 « portes d'entrée » :

| Porte d'entrée | Seuil | Ce que ça veut dire | Entreprises |
|---|---|---|---|
| 🌡️ Climat | ODD 13 **≥ 2** | MSCI juge l'entreprise « alignée » avec la lutte contre le changement climatique | 290 |
| ⚡ Énergie propre | ODD 7 **≥ 2** | Elle aide la transition énergétique | 255 |
| 💧 Eau | ODD 6 **≥ 2** | Elle aide à préserver ou à fournir l'eau | 139 |
| ♻️ Ressources | ODD 12 **≥ 2** | Elle aide la sobriété et l'économie circulaire | 226 |
| ♻️ Activités vertes | Chiffre d'affaires aligné Taxonomie UE **≥ 20 %** | Au moins un cinquième de ce qu'elle vend est une activité « verte » au sens européen | 55 |

→ **486 entreprises** contribuent.

**Pourquoi 2 et 20 % :** 2 est le seuil MSCI de l'« alignement ». 20 % est un seuil courant du marché, qui va de 20 à 50 %. Ce sont des **seuils d'entrée** : ils disent qui a le droit d'entrer. Le classement de l'étape C sélectionne ensuite celles qui contribuent **le plus**.

**Pourquoi la température implicite n'est pas une porte d'entrée :** émettre peu, ce n'est pas contribuer. Avec une porte « température ≤ 1,5 °C », des dizaines d'entreprises entreraient seulement parce qu'elles polluent peu (laboratoires pharmaceutiques, éditeurs de logiciels), sans rien apporter aux limites planétaires.

### Case 2 — Elle ne nuit pas aux autres limites (DNSH)

Il faut remplir **les deux** conditions :

| Condition | Seuil | Ce que ça veut dire |
|---|---|---|
| Aucun ODD environnemental désaligné | ODD 6, 12, 13, 14 **et** 15 tous **> −2** | Elle ne dégrade ni l'eau, ni les ressources, ni le climat, ni les océans, ni les sols. **On ne règle pas un problème en en créant un autre.** |
| Trajectoire climatique acceptable | Température implicite **≤ 3 °C** | Elle n'est pas sur une trajectoire catastrophique |

→ **663 entreprises** passent.

**Pourquoi 3 °C et pas 2 °C :** un seuil à 2 °C exclurait justement des fabricants de solutions, comme EDP Renováveis (éolien et solaire, 2,1 °C), Nibe (pompes à chaleur, 2,5 °C), Novonesis (enzymes, 2,1 °C), Infineon (puces pour le solaire et les réseaux, 3,0 °C), Saint-Gobain (isolation, 2,1 °C) ou Norsk Hydro (aluminium bas carbone, 2,1 °C). Leur température est élevée parce qu'elles **fabriquent et grandissent**, pas parce qu'elles nuisent. La température sert ici de **garde-fou**.

**L'alignement avec Paris se vérifie au niveau du fonds entier**, pas entreprise par entreprise : au moins **−50 % d'intensité carbone** par rapport à l'univers, puis **−7 % par an** (vérifié à la pondération). Un fonds Paris-Aligned mélange des entreprises très bas carbone et des fabricants de solutions.

### Case 3 — Gouvernance

| Condition | Seuil | Pourquoi |
|---|---|---|
| Pas de controverse de gouvernance très grave | Score ≠ 0 *(déjà vérifié en A4)* | Exigence réglementaire (Pacte mondial, OCDE) |
| Gouvernance saine | Pilier gouvernance MSCI **≥ 3/10** | On écarte les gouvernances défaillantes |

→ **834 entreprises** passent. La sélectivité du fonds se joue sur l'environnement (règle d'or n°1).

**→ Résultat de l'étape B : 404 entreprises éligibles à l'Article 9.** La plupart des 437 qui échouent **ne contribuent à aucune limite** (254). 80 contribuent mais **nuisent** à une autre, et 97 échouent sur les deux.

---

## 7. Notre périmètre d'investissement

| | Entreprises |
|---|---|
| MSCI World (31/12/2024) | 1 247 |
| − A1 Énergies fossiles | − 116 |
| − A2 Financement des énergies fossiles | − 197 |
| − A3 Secteurs incompatibles | − 49 |
| − A4 Garde-fous | − 44 |
| **= Entreprises investissables** | **841** |
| − Test Article 9 | − 437 |
| **= Périmètre d'investissement** | **404** |

**Répartition par secteur :** Industrie 102 · Technologie 89 · Santé 54 · Consommation de base 40 · Immobilier 31 · Consommation discrétionnaire 28 · Communication 21 · Matériaux 18 · Services aux collectivités 14 · Services financiers (paiement, notation) 7.

**Sélectivité :** on écarte **68 % de l'univers**, plus de deux fois l'exigence du label ISR (30 %).

---

## 8. Étape C — Le classement : le score Holocène (0 à 100)

**En une phrase :** les 404 entreprises du périmètre ont toutes le droit d'entrer ; on les **classe** pour garder celles qui **apportent le plus** à la planète **en lui coûtant le moins**.

### Les deux questions

| Question | Ce qu'on regarde | Donnée | Comparée à… | Poids |
|---|---|---|---|---|
| 🌱 **Qu'apporte-t-elle à la planète ?** | **La contribution** : la somme de ses scores **positifs** sur les 4 ODD de contribution (6 eau, 7 énergie propre, 12 ressources, 13 climat), **+ sa part de chiffre d'affaires vert ÷ 10** | ODD 6, 7, 12, 13, Taxonomie UE | **Tout le périmètre** (404) | **50 %** |
| 🌡️ **Que coûte-t-elle ? (trajectoire)** | **La température implicite** : plus elle est basse, mieux c'est | `ITR` | **Son secteur** | **25 %** |
| 🏭 **Que coûte-t-elle ? (pollution)** | **L'intensité carbone totale**, scopes 1 + 2 + 3 : moins elle émet par M$ de chiffre d'affaires, mieux c'est | `INTENSITY_SCOPE_1 + 2 + 3` | **Son secteur** | **25 %** |

**Le calcul de la contribution, en détail :** un ODD négatif compte pour 0 (on ne veut pas qu'un point faible annule un point fort : c'est déjà le rôle du test « ne pas nuire »). Le chiffre d'affaires vert est divisé par 10 pour être à la même échelle : **100 % de CA vert = 10 points**, comme un ODD parfaitement aligné.

### Comment on transforme ça en note : le percentile

On ne compare pas des tonnes de CO2 à des scores ODD : on transforme chaque mesure en **percentile**, c'est-à-dire **« elle fait mieux que X % des entreprises comparées »**. Un percentile de 90 = meilleure que 90 % des autres. Puis :

> **Score Holocène = 50 % × percentile contribution + 25 % × percentile trajectoire + 25 % × percentile pollution**

### Pourquoi ces choix

- **Contribution comparée à tout le monde :** on veut celles qui aident **le plus**, quel que soit leur secteur.
- **Empreinte comparée au secteur (« best-in-class ») :** une usine émettra toujours plus qu'un éditeur de logiciels. On compare Vestas aux autres industriels, pas à Microsoft. Sinon, le fonds ne contiendrait que des logiciels.
- **50 % sur la contribution :** nous avons d'abord testé 4 critères à poids égal (trajectoire, pollution, contribution, note environnementale MSCI). Le haut du classement était alors Visa, Pearson (édition scolaire) et Diageo (spiritueux) : des entreprises qui polluent peu, mais n'apportent rien. Avec 50 % sur la contribution, le classement ressemble enfin à un fonds « limites planétaires ».
- **La température implicite revient ici :** elle n'était qu'un garde-fou à l'étape B (≤ 3 °C) ; ici, elle **départage**.

### Exemples de calcul

| | Vestas (éoliennes) | Xylem (eau) | Microsoft | Caterpillar (engins) |
|---|---|---|---|---|
| ODD 6 / 7 / 12 / 13 | 1,5 / 6 / 5,5 / 6,5 | 6,5 / 1,5 / 6 / 2 | 1 / 0 / 3,5 / 0,5 | 2 / 0 / 0 / −0,5 → 0 |
| Chiffre d'affaires vert | 100 % → +10 | 44 % → +4,4 | 23 % → +2,3 | 5 % → +0,5 |
| **Contribution** (points → percentile) | 29,5 → **100** | 20,4 → **98** | 7,3 → **64** | 2,5 → **0,5** |
| **Trajectoire** (°C → percentile secteur) | 1,3 → **92** | 1,3 → **92** | 1,4 → **80** | 2,8 → **4** |
| **Pollution** (tCO2e/M$ → percentile secteur) | 388 → **60** | 321 → **69** | 179 → **58** | 3 099 → **5** |
| **Score Holocène** | **88** | **89** | **66** | **3** |

*Vestas : 0,5 × 100 + 0,25 × 92 + 0,25 × 60 = 88.*

### Les catégories

| Catégorie | Score | Nombre | Suite |
|---|---|---|---|
| 🌟 **Excellente** | ≥ 75 | 36 | Passe à la revue qualitative |
| 🟢 **Retenue** | 60 à 74 | 96 | Passe à la revue qualitative |
| 🟠 **Éligible** | < 60 | 272 | Reste dans le périmètre, non prioritaire |

**Pourquoi 60 :** c'est un seuil nettement au-dessus de la moyenne (51) qui garde environ **un tiers du périmètre**, soit **132 entreprises** : assez pour qu'il reste une cinquantaine de lignes après les filtres financiers.

---

## 9. Étape D — La revue qualitative : « les données proposent, l'analyse vérifie »

Les données ESG ne voient pas tout. Après le score Holocène, l'équipe **relit les 132 entreprises sélectionnées** : on ne relit pas tout l'univers, on relit **ce dans quoi on va investir**. Si l'activité réelle contredit les données :
1. **On ne retire jamais une entreprise au cas par cas.**
2. **On écrit une règle** sur l'**activité**, appliquée à **toutes** les entreprises qui l'exercent.
3. **On trace la décision** : l'entreprise repérée, ce qu'on a vu, la règle créée.

C'est la **seule étape où des noms d'entreprises sont écrits à la main**, parce que nos données n'ont aucune colonne « or », « saumon d'élevage » ou « fast fashion ».

| Règle | Limites planétaires | Pourquoi | Entreprises concernées | Retirées de la sélection (score) |
|---|---|---|---|---|
| **Pas d'or** (mines, redevances, bijouterie) | Biosphère, eau, sols | L'or sert surtout aux bijoux et aux lingots, pas à la transition. Son extraction utilise du cyanure, déplace des tonnes de roche et laisse des déchets miniers | Newmont, Barrick, Agnico Eagle, Northern Star, Franco-Nevada, Wheaton, Chow Tai Fook | Newmont (88), Agnico Eagle (75), Chow Tai Fook (74) |
| **Pas de saumon d'élevage en mer** | Biosphère, océans | Pollution des fjords, poux de mer transmis aux saumons sauvages, alimentation au soja (déforestation) et aux farines de poissons sauvages. MSCI note pourtant l'ODD 14 (océans) de Mowi à **0** | Mowi, SalMar | Mowi (88), SalMar (84) |
| **Pas de fast fashion** | Eau, nouvelles entités, ressources | Coton gourmand en eau, polyester issu du pétrole, montagnes de déchets textiles : des vêtements toujours moins chers, donc toujours plus achetés | Inditex (Zara), H&M, Fast Retailing (Uniqlo), Associated British Foods (Primark) | **Zara (69)** |
| **Pas de croisières ni de réservation de vols** | Climat, océans | Leur chiffre d'affaires grandit avec le volume de vols et de croisières, comme l'aérien exclu en A3 | Carnival, Royal Caribbean, Amadeus | Amadeus (62) |

**→ Résultat : 7 entreprises retirées, 125 entreprises sélectionnées.**

**Pourquoi c'est important :** c'est la leçon de l'*Aggregate Confusion* (Berg, Kölbel et Rigobon) en pratique. Une donnée ESG peut être bonne alors que l'activité, elle, dégrade une limite planétaire. Sans la revue, **Zara obtenait 69/100** et **Newmont 88/100** : les données mesurent les **politiques** et l'**efficacité**, pas toujours l'**activité réelle**.

**Gardés en connaissance de cause :**
- L'alcool (Diageo, Campari, Kirin) : il ne figure pas parmi les exclusions réglementaires, et ces entreprises respectent nos garanties sociales. Leur présence se décide sur leur performance environnementale.
- Les assureurs santé (Elevance, Cigna) : ils n'assurent pas de projets fossiles.
- Holcim (ciment) : secteur indispensable à la transition, et Holcim est parmi les meilleures de son secteur.
- Komatsu et Sandvik : leurs machines servent aussi aux mines des métaux de la transition.
- L'IA et les data centers (NVIDIA, Microsoft) : ils consomment beaucoup d'électricité, mais elle peut être décarbonée. Ils passent par nos critères habituels.

---

## 10. La sélection finale : 125 entreprises

**Le top 12 :** United Utilities (eau potable, 90) · Brookfield Renewable (renouvelables, 89) · Xylem (traitement de l'eau, 89) · Jacobs (ingénierie de l'eau et des infrastructures, 89) · AECOM (ingénierie environnementale, 88) · Vestas (éoliennes, 88) · WSP (ingénierie, 86) · Segro (entrepôts basse consommation, 86) · Daiwa House (construction bas carbone, 84) · Prologis (84) · Meridian (hydroélectricité, 84) · Dassault Systèmes (83).

**Répartition des 125 :** Industrie 31 · Technologie 27 · Santé 20 · Immobilier 14 · Services aux collectivités 11 · Consommation de base 11 · Matériaux 5 · Autres 6.

👉 **Les 125 entreprises sont transmises à l'étape suivante (filtres financiers), avec leur score Holocène** (`selection_finale.xlsx`). Elles représentent **10 % de l'univers de départ**.

---

## 11. Le niveau d'exigence de nos critères

**En résumé :** sur **l'environnement**, notre cœur d'expertise, la plupart de nos critères vont **au-delà de la réglementation**. Sur le **social et la gouvernance**, nous appliquons le **socle de garanties** exigé par SFDR et le règlement Paris-Aligned. Résultat : **68 % de l'univers écarté** au périmètre, **90 %** à la sélection finale.

| Critère | Origine | Exigence |
|---|---|---|
| Tout le secteur Énergie | Notre choix (la règle officielle : 10 % pétrole, 50 % gaz) | 🔴 Bien au-delà de la réglementation |
| Charbon ≥ 1 % du chiffre d'affaires | Règlement Paris-Aligned | 🟠 Réglementaire |
| ≥ 10 % d'une mine de charbon | Notre choix | 🔴 Au-delà de la réglementation |
| Électricité carbonée | Approximation de la règle officielle | 🟠 Réglementaire |
| Toutes les financières | Notre choix | 🔴 Bien au-delà de la réglementation |
| Secteurs incompatibles (aérien, automobile, négoce agricole) | Notre choix (même la voiture électrique) | 🔴 Bien au-delà de la réglementation |
| Controverses environnementales : rouge et orange | Notre choix | 🔴 Au-delà de la réglementation |
| Controverses sociales et de gouvernance : violations du Pacte mondial | Règlement Paris-Aligned | 🟠 Réglementaire |
| Tabac, armes controversées | Règlement Paris-Aligned | 🟠 Réglementaire |
| ODD ≤ −5 | Norme MSCI | 🟠 Norme de marché |
| Données manquantes | Notre choix | 🔴 Au-delà de la réglementation |
| Contribution : ODD ≥ 2 ou CA Taxonomie ≥ 20 % | Norme MSCI, Taxonomie UE | 🟠 Seuil d'entrée (l'étape C sélectionne ensuite) |
| Ne pas nuire : aucun ODD ≤ −2 | Norme MSCI | 🔴 Au-delà de la réglementation |
| Ne pas nuire : température ≤ 3 °C | Notre choix | 🟠 Garde-fou (la trajectoire Paris est pilotée au niveau du fonds) |
| Gouvernance ≥ 3/10 | Notre choix | 🟠 Écarte les gouvernances défaillantes |
| Sélection : score Holocène ≥ 60 | Notre choix (≈ un tiers du périmètre) | 🔴 Au-delà de la réglementation |
| Or, saumon d'élevage, fast fashion, croisières | Revue qualitative | 🔴 Au-delà de la réglementation |

---

## 12. Les limites que nous assumons

1. **Les scores ODD notent aussi les politiques**, pas seulement l'activité. Une entreprise peut être « alignée » grâce à ses engagements. C'est ce qui justifie la revue qualitative.
2. **Les émissions financées ne sont pas mesurées.** C'est pourquoi les financières sont exclues. Une base complète des émissions financées permettrait de réintégrer les meilleures banques. Visa, Mastercard et les bourses sont exclues avec elles, car nos données ne permettent pas de les distinguer.
3. **Électricité carbonée :** nous approchons la règle officielle (gCO2/kWh) par l'intensité scope 1. Cette approximation peut exclure à tort des électriciens en transition, comme **Iberdrola**, leader des renouvelables mais qui exploite encore des centrales au gaz.
4. **Les classifications sectorielles sont larges** (64 groupes d'industrie). La fast fashion et les croisières ne peuvent être repérées que par la revue qualitative.
5. **Des données de dates différentes :** MSCI à fin 2024, les bases charbon à 2026.
6. **Le score Holocène dépend de nos poids** (50 / 25 / 25). D'autres poids donneraient un autre classement : c'est pourquoi nous les justifions et les publions.

---

## 13. Sources et code

| Donnée | Source |
|---|---|
| Univers, données financières et extra-financières | `all_data.csv` (MSCI, 31/12/2024), fourni par l'enseignant |
| Charbon | urgewald, *Global Coal Exit List 2026* (`Urgewald GCEL 2026 V1.0.xlsx`) |
| Mines de charbon (thermique et métallurgique) | Global Energy Monitor, *Global Coal Mine Tracker*, août 2026 (`Global Coal Mine Tracker, August 2026.xlsx`), licence CC BY 4.0 |
| Financements fossiles des banques | *Banking on Climate Chaos 2026* (RAN, BankTrack et al.) ; urgewald, *Still Burning: How Banks and Investors Fuel Met Coal Expansion* (annexe 1) ; Reclaim Finance, *Coal Policy Tool* et *Oil and Gas Policy Tracker* |
| Limites planétaires | Rockström et al. (2009), *Nature* ; Richardson et al. (2023), *Science Advances* |
| Divergence des notations ESG | Berg, Kölbel et Rigobon (2022), *Aggregate Confusion: The Divergence of ESG Ratings*, Review of Finance |
| Taxonomie européenne | Règlement (UE) 2020/852 |
| Règles Paris-Aligned | Règlement délégué (UE) 2020/1818, article 12 |
| Investissement durable | Règlement (UE) 2019/2088 (SFDR), article 2.17 |

### Le code

Tout le calcul est dans le notebook **`Holocene_selection_extra_financiere.ipynb`**, écrit en Python simple : une règle par ligne, avec le nombre d'entreprises restantes affiché après chaque étape.

```
Départ : 1247 → A1 : 1131 → A2 : 934 → A3 : 885 → A4 : 841 → B : 404 → C : 132 → D : 125
```

Il lit `all_data.csv` et les deux bases charbon, et crée `selection_finale.xlsx`.
