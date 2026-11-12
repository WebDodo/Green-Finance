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
  │  ÉTAPE A · Exclusions (ce qu'on refuse) ............ − 211
  ▼
1 036  entreprises investissables
  │
  │  ÉTAPE B · Test « investissement durable » ........ − 454
  ▼
  582  entreprises éligibles à l'Article 9  =  NOTRE PÉRIMÈTRE
```

---

## 3. Étape A — Les exclusions : ce qu'on refuse

On retire d'emblée ce qui est incompatible avec le fonds, avant même de regarder ce que l'entreprise apporte. Une entreprise peut être exclue pour plusieurs motifs.

### A1. Les énergies fossiles *(obligatoire en Article 9.3)*

| Règle | Comment on l'applique | Exclues |
|---|---|---|
| Pétrole et gaz | Tout le secteur GICS Énergie | 52 |
| Électricité carbonée | Un électricien n'est gardé que s'il fait au moins 50 % de chiffre d'affaires vert, ou si ses émissions directes sont inférieures à 100 tCO2e par M$ de chiffre d'affaires (réseaux, eau) | 51 |
| **Charbon** (≥ 1 % du chiffre d'affaires, seuil Paris-Aligned) | Croisement avec la **Global Coal Exit List 2026** (urgewald). 32 de nos entreprises y figurent, dont 26 déjà exclues. **Nouvelles exclusions :** Glencore (3,2 % du CA, 98 Mt/an), BHP (3,2 %), CSX (13 %, transport de charbon), Berkshire Hathaway (1,7 %), auxquelles s'ajoutent les producteurs de **charbon métallurgique** absents de la GCEL : Anglo American et South32 | 6 |

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

**→ Résultat de l'étape A : 211 entreprises exclues, 1 036 investissables.**

---

## 4. Étape B — Le test « investissement durable » (Article 9)

Pour un Article 9, **chaque** entreprise du fonds doit être un investissement durable au sens de l'**article 2.17 de SFDR**. C'est un examen en oui ou non : il faut cocher **les 3 cases**.

### Case 1 — Elle contribue à au moins une limite planétaire

Il suffit d'**une** de ces conditions :

| Porte d'entrée | Condition | Entreprises |
|---|---|---|
| 🌡️ Trajectoire climat | Température implicite ≤ 1,5 °C | 271 |
| 🌡️ Climat | ODD 13 aligné (score ≥ 2) | 386 |
| ⚡ Énergie propre | ODD 7 aligné (score ≥ 2) | 335 |
| 💧 Eau | ODD 6 aligné (score ≥ 2) | 141 |
| ♻️ Ressources | ODD 12 aligné (score ≥ 2) | 230 |
| ♻️ Solutions vertes | ≥ 20 % du chiffre d'affaires vert (technologies propres ou Taxonomie) | 62 |

→ **678 entreprises** contribuent.

*Les scores ODD de MSCI vont de −10 à +10 : à partir de 2, l'entreprise est « alignée » ; à −2 ou moins, elle est « désalignée ».*

### Case 2 — Elle ne nuit pas aux autres limites (DNSH)

| Condition | Pourquoi |
|---|---|
| Aucun ODD environnemental désaligné (ODD 6, 12, 13, 14 ou 15 ≤ −2) | On ne règle pas un problème en en créant un autre |
| Température implicite ≤ 3 °C | Pas de trajectoire climatique catastrophique |

→ **839 entreprises** passent.

### Case 3 — Gouvernance minimale

| Condition | Pourquoi |
|---|---|
| Pas de drapeau rouge de gouvernance *(déjà vérifié à l'étape A)* | Minimum réglementaire |
| Note du pilier gouvernance MSCI ≥ 3/10 | On écarte seulement les gouvernances défaillantes |

→ **1 026 entreprises** passent. C'est volontairement peu sélectif : la gouvernance n'est pas notre thème.

**→ Résultat de l'étape B : 582 entreprises éligibles à l'Article 9.** Les autres échouent surtout parce qu'elles **ne contribuent à aucune limite** (250 entreprises), plus rarement parce qu'elles **nuisent** à l'une d'elles (91).

---

## 5. Notre périmètre d'investissement

| | Entreprises |
|---|---|
| MSCI World (31/12/2024) | 1 247 |
| Après les exclusions | 1 036 |
| **Périmètre d'investissement (Article 9)** | **582** |

Ces **582 entreprises** ont toutes le droit, réglementairement et selon notre thème, d'entrer dans le fonds. Les étapes suivantes choisissent **les meilleures** : sélection extra-financière, filtres financiers, puis pondération.

---

## 6. Sources

| Donnée | Source |
|---|---|
| Univers, données financières et extra-financières | `all_data.csv` (MSCI, 31/12/2024), fourni par l'enseignant |
| Charbon thermique | urgewald, *Global Coal Exit List 2026* (`Urgewald GCEL 2026 V1.0.xlsx`) |
| Charbon métallurgique | urgewald, *Metallurgical Coal Exit List 2026* ; Global Energy Monitor, *Global Coal Mine Tracker* (à intégrer) |
| Règles Paris-Aligned | Règlement délégué (UE) 2020/1818 |
| Investissement durable | Règlement (UE) 2019/2088 (SFDR), article 2.17 |
