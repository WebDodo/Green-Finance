# JEVONS Actions Monde — Holocène AM

*Projet final Finance durable · Université Paris-Dauphine · 2026*

> **Faire moins, pas seulement mieux.**

## Le fonds en 30 secondes

- **Société de gestion : Holocène AM.** L'Holocène est l'époque de climat stable dans laquelle vit l'humanité depuis environ 11 700 ans. Notre mission : investir pour que l'économie reste dans les **limites planétaires** qui garantissent cette stabilité.
- **Fonds : JEVONS Actions Monde.** Il porte le nom du paradoxe de Jevons (1865) : plus une technologie devient efficace, plus on la consomme. C'est l'**effet rebond**. Notre fonds refuse de financer ce piège.
- **Forme :** FCP de droit français, OPCVM (UCITS), actions monde, long only, sans levier, liquidité quotidienne.
- **Classification :** SFDR **Article 9** (9.3), avec pour indice de référence le MSCI World Climate Paris Aligned.
- **Données :** `all_data.csv`, qui contient les 1 247 entreprises du MSCI World au 31/12/2024 (données financières et extra-financières MSCI).

**La règle d'or :** sur l'**environnement**, on suit notre thème et on est exigeants. Sur le **social et la gouvernance**, on applique uniquement le minimum exigé pour un Article 9.

## Qui fait quoi

```
PARTIE 1 · EXTRA-FINANCIER     PARTIE 2 · FINANCIER        PARTIE 3 · ALLOCATION
(Doryan)                                       
1 247 entreprises       ───►   filtres financiers   ───►   score final combiné
→ catégorie                    → score financier           → choix des ~50 lignes
→ score JEVONS (0-100)           (0-100)                   → pondération
                                                                   │
                                                                   ▼
                                            PARTIE 4 · ANALYSE DU FONDS
```

---

# PARTIE 1 — Le filtre extra-financier (Doryan)

**Objectif :** donner à chacune des 1 247 entreprises une **catégorie** et un **score de compatibilité JEVONS**, pour que la suite du projet travaille uniquement sur les entreprises compatibles avec le fonds.

## Étape 1 — Le concept *(fichier 01)*

**Objectif durable (Article 9) :** contribuer à réduire la pression de l'économie sur les **limites planétaires**, en finançant des entreprises qui aident sur au moins une limite, **sans nuire aux autres**.

| Limite | Rôle | Mesure |
|---|---|---|
| 🌡️ Climat | Contribution | Température implicite, ODD 13 (climat), ODD 7 (énergie propre) |
| 💧 Eau | Contribution | ODD 6 |
| ♻️ Ressources | Contribution | ODD 12, part de chiffre d'affaires vert |
| 🌿 Biodiversité | Garde-fou (ne pas nuire) | ODD 14 et 15 |

## Étape 2 — Ce qu'on refuse *(fichier 02)*

| Famille | Ce qu'on exclut |
|---|---|
| Énergies fossiles | Pétrole et gaz, électricité carbonée, mines de charbon |
| Controverses | Environnementales : drapeau rouge et orange. Sociales et de gouvernance : drapeau rouge seulement |
| Minimum éthique | Tabac, armes controversées |
| Autres limites | Entreprises fortement nuisibles à la biodiversité, à l'eau ou aux ressources |
| **Activités du rebond (Jevons)** 🎯 | Aérien, croisières, automobile (électrique compris), fast fashion, repérées par notre **détecteur d'effet rebond** |
| Données manquantes | On n'investit pas dans ce qu'on ne mesure pas |

### Le détecteur d'effet rebond 🤖

**Pourquoi :** les données ESG mesurent l'**efficacité** (les émissions par produit), pas le **volume** (combien de produits). Sans cette exclusion, **10 entreprises du rebond passeraient toutes nos étapes**, dont **Zara avec la note maximale** (4 voix sur 4), ainsi que Toyota, BMW, Ferrari… Et même une liste faite à la main en oublie : **Amadeus** (réservation de billets d'avion) et **Next** (vêtements).

**La grille : 4 questions, 1 point par « oui » :**
1. Le chiffre d'affaires grandit-il avec le **volume** d'un produit gourmand en ressources ?
2. Les gains d'efficacité font-ils **baisser les prix**, donc **augmenter la consommation** ?
3. L'essentiel de l'impact vient-il de **l'usage** des produits ? *(calculé avec nos données : part du scope 3)*
4. Le modèle pousse-t-il à **renouveler souvent** ?

| Score | Décision |
|---|---|
| 0 – 1 | ✅ OK |
| 2 | 👀 Sous surveillance : poids ≤ 2 %, dialogue prioritaire, réévaluation annuelle |
| 3 – 4 | ❌ Exclue |

**Qui décide :** Claude (Anthropic) **propose** les réponses avec une justification, et **l'équipe valide**. Le résultat est un fichier, `detecteur_rebond.csv`, que le code lit comme n'importe quelle source de données. La grille, le prompt et toutes les réponses sont publiés dans le fichier de données complémentaires.

## Étape 3 — L'examen d'entrée Article 9 *(fichier 03)*

Chaque entreprise doit cocher **3 cases** (article 2.17 de SFDR) :
1. **Contribuer** à une limite : trajectoire ≤ 1,5 °C, **ou** ODD 13, 7, 6 ou 12 aligné, **ou** au moins 20 % de chiffre d'affaires vert.
2. **Ne pas nuire** : aucun ODD environnemental désaligné et trajectoire ≤ 3 °C.
3. **Gouvernance minimale** : note de gouvernance MSCI ≥ 3/10.

## Étape 4 — Les jurés « limites planétaires » *(fichier 04)*

**4 jurés** comparent chaque entreprise à ses **concurrents du même secteur**. Chacun vote « pour » si elle est dans la moitié haute :

| Juré | Question |
|---|---|
| 🌡️ Trajectoire | Ses objectifs climat sont-ils meilleurs ? |
| 🏭 Pression réelle | Émet-elle moins, **usage de ses produits compris** (scope 3) ? |
| 💧 Eau | Contribue-t-elle plus à l'eau ? |
| ♻️ Ressources | Contribue-t-elle plus à la sobriété des ressources ? |

👉 **3 voix sur 4** pour être retenue. On vote au lieu de faire une moyenne, pour qu'un bon score ne cache pas un mauvais. C'est la leçon du cours sur l'**Aggregate Confusion** : les mesures ne sont pas d'accord entre elles, donc on ne se fie à aucune seule.

## Ce que la partie 1 livre : catégorie + score JEVONS

Un fichier Excel avec **les 1 247 entreprises**, chacune avec :

**1. Une catégorie :**

| Catégorie | Signification | Nombre (environ) |
|---|---|---|
| ❌ **Exclue** | Interdite à l'étape 2 (motif précisé : fossile, controverse, rebond…) | 209 |
| ⛔ **Non éligible** | Ne passe pas le test Article 9 (étape 3) | 456 |
| 🟠 **Éligible** | Article 9 OK, mais 2 voix ou moins sur 4 | 304 |
| 🟢 **Retenue** | 3 voix sur 4 | 181 |
| 🌟 **Excellente** | 4 voix sur 4 | 97 |

**2. Un score de compatibilité JEVONS (0 à 100) :** la moyenne des 4 jurés. Plus il est haut, plus l'entreprise est bonne pour les limites planétaires par rapport à ses concurrents.

**3. Le détail pour justifier :** le motif d'exclusion, les portes de contribution, les votes de chaque juré, la température implicite, l'intensité carbone, le score de rebond.

👉 **Les entreprises 🟢 Retenues et 🌟 Excellentes (≈ 278) sont transmises à la partie 2.**

---

# PARTIE 2 — Le filtre financier *(membre 2 · voir A_FAIRE.md)*

Elle part des ≈ 278 entreprises compatibles. Elle applique des **filtres financiers** (liquidité, rentabilité, dette, risque, valorisation ; brouillon dans le fichier 05) et donne un **score financier de 0 à 100**, pour repérer les meilleures entreprises financièrement.

# PARTIE 3 — L'allocation *(membre 3 · voir A_FAIRE.md)*

Elle combine le **score JEVONS** et le **score financier** en un **score final**, tient compte des **catégories** (par exemple, priorité aux 🌟 Excellentes), choisit environ 50 lignes et décide des **poids** (brouillon dans le fichier 06).

# PARTIE 4 — L'analyse du fonds *(tous · voir A_FAIRE.md)*

Elle présente la composition du fonds, son score ESG et climat comparé au MSCI World, et ses performances.
