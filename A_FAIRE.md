# Ce qui reste à faire

## Construction du fonds
- [ ] **Détecteur d'effet rebond (étape 2) :** produire `detecteur_rebond.csv` (Claude), puis la validation par l'équipe, la calibration du seuil (les cas évidents doivent être ≥ 3) et le remplacement de la liste manuelle.
- [ ] **Tableau « sans / avec l'exclusion rebond »** pour la présentation (Zara 4/4, Toyota, BMW… passent sans elle ; Amadeus et Next ratés par la liste manuelle).
- [ ] **Mines de charbon :** vérifier Glencore, BHP, Anglo American et South32 dans leurs rapports annuels.
- [ ] **Filtres financiers :** relire et confirmer les seuils (déjà définis, fichier 05).
- [ ] **Choix final (étape 6) :** passer de 188 éligibles à environ 50 lignes (méthode secteur × région, score final). *→ confié à un membre du groupe*
- [ ] **Choix des poids :** méthode de pondération et contraintes (carbone, température, secteurs, régions, 5/10/40). *→ idem*
- [ ] **Rebalancement :** fréquence (trimestrielle ?), règle de sortie (on sort quand le score baisse), contrôle de la trajectoire de −7 %/an.

## Résultats et analyse
- [ ] **Séries de prix Yahoo** (Doryan) : backtest 2015-2024 et performance réelle hors échantillon 2025-2026.
- [ ] **Résultats financiers :** rendement, volatilité, Sharpe, perte maximale, comparaison au MSCI World.
- [ ] **Composition du fonds :** secteurs, régions, top 10, concentration.
- [ ] **Score ESG du fonds :** note MSCI moyenne, température implicite, intensité carbone (scopes 1-2 et 1-2-3), alignement aux ODD, part verte, PAI, comparaison au MSCI World.
- [ ] **Robustesse :** que se passe-t-il si on change un seuil ou si on retire un juré ?

## Livrables (avant le mardi 24/11/2026, 23h59)
- [ ] Excel 1 : les actifs sélectionnés et leurs poids
- [ ] Excel 2 : les données complémentaires (détecteur de rebond, mines de charbon, prix Yahoo, seuils)
- [ ] Code Python
- [ ] PowerPoint d'environ 10 slides
- [ ] PDF explicatif

## Soutenance (26/11 ou 03/12, 15 min + 5 min de questions)
- [ ] Storytelling et branding (pitch Jevons, logo Holocène)
- [ ] Répartition de la parole entre les 3 membres
- [ ] Préparation des questions du jury
