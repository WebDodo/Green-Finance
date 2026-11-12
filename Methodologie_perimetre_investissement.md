# JEVONS Actions Monde — Méthodologie : le périmètre d'investissement

*Holocène AM · Projet final Finance durable · Université Paris-Dauphine · 2026*

> **Faire moins, pas seulement mieux.**

Ce document explique **comment on passe des 1 247 entreprises du MSCI World à la liste des entreprises qui ont le droit d'entrer dans le fonds**. C'est notre **périmètre d'investissement**. Le choix final des lignes et leurs poids viennent après.

---

## 1. Le fonds en bref

| | |
|---|---|
| **Société de gestion** | **Holocène AM**. L'Holocène est l'époque de climat stable dans laquelle vit l'humanité depuis environ 11 700 ans. Notre mission : investir pour que l'économie reste dans les limites qui garantissent cette stabilité. |
| **Fonds** | **JEVONS Actions Monde**. Il porte le nom du paradoxe de Jevons (1865) : plus une technologie devient efficace, plus on la consomme. C'est l'effet rebond. |
| **Forme** | FCP de droit français, OPCVM (UCITS), actions monde, long only, sans levier, liquidité quotidienne |
| **Classification** | SFDR **Article 9.3** |
| **Indice de référence** | MSCI World Climate Paris Aligned |
| **Univers de départ** | MSCI World au 31/12/2024 : **1 247 entreprises** (`all_data.csv`) |

### L'objectif d'investissement durable (Article 9)

> *Le fonds a pour objectif d'investissement durable de contribuer à réduire la pression de l'économie sur les **limites planétaires**, en investissant dans des entreprises qui contribuent de manière mesurable à l'atténuation du changement climatique, à la protection des ressources en eau ou à l'économie circulaire, sans porter atteinte de manière significative aux autres limites, notamment la biodiversité.*

| Limite planétaire | Rôle dans le fonds | Mesure (données MSCI) |
|---|---|---|
| 🌡️ Climat | Contribution | Température implicite, intensité carbone, ODD 13 (climat), ODD 7 (énergie propre) |
| 💧 Eau douce | Contribution | ODD 6 |
| ♻️ Ressources et pollution | Contribution | ODD 12 (consommation responsable), part de chiffre d'affaires vert |
| 🌿 Biodiversité | Garde-fou (ne pas nuire) | ODD 14 (océans), ODD 15 (vie terrestre) |

### Notre règle d'or

> **Sur l'environnement, on suit notre thème et on est exigeants. Sur le social et la gouvernance, on applique uniquement le minimum exigé pour un Article 9.**

### Pourquoi l'Article 9.3, aligné avec l'Accord de Paris

L'Article 9 n'impose pas d'être aligné avec Paris. Nous le faisons quand même, pour 5 raisons :
1. **Crédibilité :** un fonds « limites planétaires » qui détiendrait Glencore, l'un des plus gros mineurs de charbon du monde, serait indéfendable, même si c'est légal.
2. **Attentes du marché :** le label ISR et la plupart des investisseurs exigent de toute façon l'exclusion des énergies fossiles.
3. **Anticipation :** la réforme SFDR 2.0, proposée fin 2025, prévoit d'imposer ces exclusions à tous les fonds « durables ».
4. **Coût quasi nul :** il suffit de quelques vérifications en plus.
5. **Un chiffre fort :** au moins 50 % de carbone en moins que le marché.

---

## 2. L'entonnoir

```
1 247  entreprises du MSCI World
  │
  │  ÉTAPE A · Exclusions (ce qu'on refuse) ............ − 397
  ▼
  850  entreprises investissables
  │
  │  ÉTAPE B · Test « investissement durable » ........ − 440
  ▼
  410  entreprises éligibles à l'Article 9  =  NOTRE PÉRIMÈTRE
```

---

## 3. Étape A — Les exclusions : ce qu'on refuse

On retire d'emblée ce qui est incompatible avec le fonds, avant même de regarder ce que l'entreprise apporte. Une entreprise peut être exclue pour plusieurs motifs.

### A1. Les énergies fossiles *(obligatoire en Article 9.3)*

| Règle | Comment on l'applique | Exclues |
|---|---|---|
| Pétrole et gaz | Tout le secteur GICS Énergie | 52 |
| Électricité carbonée | Un électricien n'est gardé que s'il fait au moins 50 % de chiffre d'affaires vert, ou si ses émissions directes sont inférieures à 100 tCO2e par M$ de chiffre d'affaires (réseaux, eau) | 51 |
| **Charbon thermique** (≥ 1 % du chiffre d'affaires, seuil Paris-Aligned) | Croisement avec la **Global Coal Exit List 2026** (urgewald). 32 de nos entreprises y figurent, dont 26 déjà exclues. **Nouvelles exclusions :** Glencore (3,2 % du CA, 98 Mt/an), BHP (3,2 %), CSX (13 %, transport de charbon), Berkshire Hathaway (1,7 %) | 4 |
| **Mines de charbon** (thermique **et métallurgique**) | Croisement avec le **Global Coal Mine Tracker** (Global Energy Monitor, août 2026), mine par mine. On exclut toute entreprise qui détient **au moins 10 % d'une mine de charbon en exploitation** (production > 0,5 Mt/an). **Nouvelles exclusions :** Anglo American (88 % des mines Grosvenor et Moranbah North, charbon métallurgique), Mitsubishi Corp (50 % des mines BMA avec BHP), Mitsui & Co, ITOCHU, Sumitomo Corp, Marubeni, Nippon Steel, JFE | 8 |

**Bon à savoir :** South32 n'est **pas** exclue. Le Global Coal Mine Tracker montre qu'elle a **vendu** ses mines de charbon métallurgique d'Illawarra (Appin, Dendrobium), aujourd'hui détenues par d'autres groupes. Nos données MSCI datent de fin 2024, la base de Global Energy Monitor d'août 2026 : croiser plusieurs sources permet d'éviter d'exclure une entreprise qui a déjà changé.

### A2. Les controverses *(sévères sur l'environnement, minimum sur le social)*

| Règle | Exclues |
|---|---|
| 🔴🟠 Controverse **environnementale** grave : drapeau rouge ou orange (score MSCI ≤ 1). Par exemple Coca-Cola, Nestlé, Volkswagen, Bayer | 28 |
| 🔴 Controverse **sociale ou de gouvernance** très grave : drapeau rouge seulement (score = 0), notre proxy des violations du Pacte mondial de l'ONU | 2 |

### A3. Le minimum éthique *(obligatoire en Article 9.3)*

| Règle | Exclues |
|---|---|
| Tabac | 5 |
| Armes controversées | 5 |

### A4. Les atteintes graves aux autres limites

| Règle | Exclues |
|---|---|
| Fortement nuisible à la **biodiversité** : ODD 14 ou 15 ≤ −5 (chimie, plastiques…) | 13 |
| Fortement nuisible à l'**eau** ou aux **ressources** : ODD 6 ou 12 ≤ −5 | 72 |

### A5. L'exclusion Jevons : les activités du rebond 🎯

| Activité | Qui | Exclues |
|---|---|---|
| ✈️ Aérien | Toutes les compagnies aériennes | 7 |
| 🚢 Croisières | Carnival, Royal Caribbean | 3 |
| 🚗 Automobile, **électrique comprise** | Constructeurs et équipementiers | 34 |
| 👕 Fast fashion | Inditex (Zara), H&M, Fast Retailing (Uniqlo), Associated British Foods (Primark) | 4 |

**Pourquoi :** les avions consomment moins par passager, mais on vole toujours plus. Les voitures sont plus propres, mais le parc automobile grossit. Les vêtements sont moins chers à produire, donc on en achète toujours plus. **L'efficacité ne compense pas la hausse des volumes.**

**Pourquoi une liste et pas une donnée :** les notes ESG mesurent l'**efficacité** (émissions par produit), pas le **volume**. Sans cette exclusion, Zara passerait tous nos autres filtres. Nous assumons une limite : presque toute activité crée un peu d'effet rebond. Nous excluons uniquement les activités où il est **le moteur du modèle économique**.

### A6. Les données manquantes

| Règle | Exclues |
|---|---|
| Pas de note ESG, de température implicite ou de données carbone : on n'investit pas dans ce qu'on ne mesure pas | 14 |
| **Les entreprises dont le métier est de financer, d'investir ou d'assurer** : banques, assureurs, gestionnaires d'actifs, capital-investissement, holdings. Leur vrai impact, ce qu'elles **financent ou assurent**, n'est pas mesuré dans nos données | 180 |

**Pourquoi exclure les financières :** en 2025, les 65 plus grandes banques du monde ont financé **906 milliards de dollars** d'énergies fossiles (*Banking on Climate Chaos 2026*). Pourtant, nos données donnent à Goldman Sachs une intensité carbone scope 3 de **0,7 tCO2e par M$** de chiffre d'affaires, contre 494 pour l'industrie. MSCI mesure leurs bureaux, pas leurs prêts. Les assureurs ont le même angle mort : ce qu'ils assurent et ce qu'ils placent. Plutôt que de faire confiance à un chiffre faux, nous les excluons. C'est la même règle que pour les données manquantes : **on n'investit pas dans ce qu'on ne mesure pas.**

**Ce qu'on garde :** les **services de paiement, les bourses et les agences de notation** (Visa, Mastercard, PayPal, S&P Global, Deutsche Börse, Nasdaq…). Elles se rémunèrent par commission et ne financent pas d'entreprises.

**→ Résultat de l'étape A : 397 entreprises exclues, 850 investissables.**

---

## 4. Étape B — Le test « investissement durable » (Article 9)

Pour un Article 9, **chaque** entreprise du fonds doit être un investissement durable au sens de l'**article 2.17 de SFDR**. C'est un examen en oui ou non : il faut cocher **les 3 cases**.

### Case 1 — Elle contribue à au moins une limite planétaire

Il suffit d'**une** de ces conditions :

| Porte d'entrée | Condition | Entreprises |
|---|---|---|
| 🌡️ Climat | ODD 13 aligné (score ≥ 2) | 295 |
| ⚡ Énergie propre | ODD 7 aligné (score ≥ 2) | 261 |
| 💧 Eau | ODD 6 aligné (score ≥ 2) | 138 |
| ♻️ Ressources | ODD 12 aligné (score ≥ 2) | 227 |
| ♻️ Solutions vertes | ≥ 20 % du chiffre d'affaires vert (technologies propres ou Taxonomie) | 61 |

→ **492 entreprises** contribuent.

*Les scores ODD de MSCI vont de −10 à +10 : à partir de 2, l'entreprise est « alignée » ; à −2 ou moins, elle est « désalignée ».*

**Pourquoi la température implicite n'est pas une porte d'entrée :** émettre peu, ce n'est pas contribuer. Avec une porte « température ≤ 1,5 °C », 76 entreprises seraient entrées seulement parce qu'elles polluent peu, surtout des banques et des laboratoires pharmaceutiques, sans rien apporter aux limites planétaires. Dans notre fonds, chaque entreprise a une **vraie contribution** : un ODD environnemental aligné ou du chiffre d'affaires vert.

### Case 2 — Elle ne nuit pas aux autres limites (DNSH)

| Condition | Pourquoi |
|---|---|
| Aucun ODD environnemental désaligné (ODD 6, 12, 13, 14 ou 15 ≤ −2) | On ne règle pas un problème en en créant un autre |
| Température implicite ≤ 3 °C | Pas de trajectoire climatique catastrophique |

→ **674 entreprises** passent.

**Pourquoi 3 °C et pas 2 °C :** un seuil à 2 °C exclurait justement des fabricants de solutions, comme EDP Renováveis (éolien et solaire, 2,1 °C), Nibe (pompes à chaleur, 2,5 °C), Novonesis (enzymes, 2,1 °C), Infineon (puces pour le solaire et les réseaux, 3,0 °C), Saint-Gobain (isolation, 2,1 °C) ou Norsk Hydro (aluminium bas carbone, 2,1 °C). Leur température est élevée parce qu'elles **fabriquent et grandissent**, pas parce qu'elles nuisent. La température sert ici de **garde-fou**. L'objectif de Paris est tenu au niveau du **fonds entier** : au moins −50 % d'intensité carbone par rapport à l'univers, puis −7 % par an (vérifié à la pondération). La température sert aussi à départager les entreprises à l'étape suivante.

### Case 3 — Gouvernance minimale

| Condition | Pourquoi |
|---|---|
| Pas de drapeau rouge de gouvernance *(déjà vérifié à l'étape A)* | Minimum réglementaire |
| Note du pilier gouvernance MSCI ≥ 3/10 | On écarte seulement les gouvernances défaillantes |

→ **843 entreprises** passent. C'est volontairement peu sélectif : la gouvernance n'est pas notre thème.

**→ Résultat de l'étape B : 410 entreprises éligibles à l'Article 9.** La plupart des 440 qui échouent **ne contribuent à aucune limite** (259) ; 80 contribuent mais **nuisent** à une autre ; 95 échouent sur les deux.

---

## 5. Notre périmètre d'investissement

| | Entreprises |
|---|---|
| MSCI World (31/12/2024) | 1 247 |
| Après les exclusions | 850 |
| **Périmètre d'investissement (Article 9)** | **410** |

Ces **410 entreprises** ont toutes le droit, réglementairement et selon notre thème, d'entrer dans le fonds. Les étapes suivantes choisissent **les meilleures** : sélection extra-financière, filtres financiers, puis pondération.

---

## 6. Sources

| Donnée | Source |
|---|---|
| Univers, données financières et extra-financières | `all_data.csv` (MSCI, 31/12/2024), fourni par l'enseignant |
| Charbon thermique | urgewald, *Global Coal Exit List 2026* (`Urgewald GCEL 2026 V1.0.xlsx`) |
| Mines de charbon (thermique et métallurgique) | Global Energy Monitor, *Global Coal Mine Tracker*, août 2026 (`Global Coal Mine Tracker, August 2026.xlsx`), licence CC BY 4.0 |
| Financements fossiles des banques (justification de l'exclusion des financières) | *Banking on Climate Chaos 2026* (RAN, BankTrack et al.) ; Reclaim Finance, *Coal Policy Tool* et *Oil and Gas Policy Tracker* (`CoalPolicyTracker.xlsx`, `OilGasPolicyTracker.xlsx`) |
| Règles Paris-Aligned | Règlement délégué (UE) 2020/1818 |
| Investissement durable | Règlement (UE) 2019/2088 (SFDR), article 2.17 |
