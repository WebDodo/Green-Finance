# Fonds Holocène Actions Monde - Partie 4 : tableaux de comparaison
# À lancer après 1_selection_extra_financiere.py et 2_portefeuille.py
# Produit resultats/Analyse_comparaison.xlsx avec :
#   1. secteurs et régions : fonds contre MSCI World
#   2. caractéristiques financières et extra-financières : fonds contre MSCI World
#   3. risque : bêta, écart de suivi (tracking error), ratio d'information
#   4. comparaison avec notre indice de référence (ETF MSCI World Climate Paris Aligned)
#   5. d'où vient l'écart de performance : les plus grosses valeurs du MSCI World
#   6. contribution de chaque ligne du fonds à la performance 2025-2026

import os
import numpy as np
import pandas as pd
import yfinance as yf

data = pd.read_csv("donnees/all_data.csv")
pf = pd.read_excel("resultats/Holocene_Portefeuille.xlsx", sheet_name="Portefeuille")
pf = pf[["ISIN", "Poids"]].merge(data, left_on="ISIN", right_on="isin")
pf["ticker_yahoo"] = pf["ticker_yahoo"].replace({"CICT.SI": "C38U.SI", "CLAR.SI": "A17U.SI"})
pf = pf.drop_duplicates("ticker_yahoo")
pf["Poids"] = pf["Poids"] / pf["Poids"].sum()
msci = data["Weight in MSCI World"] / data["Weight in MSCI World"].sum()
print("Lignes du fonds :", len(pf))

# ---------------------------------------------------------------- 1. secteurs et régions
secteurs = pd.DataFrame({
    "Fonds": pf.groupby("gics_sector_name")["Poids"].sum(),
    "MSCI World": msci.groupby(data["gics_sector_name"]).sum(),
}).fillna(0)
secteurs["Écart"] = secteurs["Fonds"] - secteurs["MSCI World"]
secteurs = secteurs.sort_values("Fonds", ascending=False)

regions = pd.DataFrame({
    "Fonds": pf.groupby("region_en")["Poids"].sum(),
    "MSCI World": msci.groupby(data["region_en"]).sum(),
}).fillna(0)
regions["Écart"] = regions["Fonds"] - regions["MSCI World"]
print("\nSecteurs (%) :\n", (secteurs * 100).round(1))
print("\nRégions (%) :\n", (regions * 100).round(1))

# ---------------------------------------------------------------- 2. caractéristiques
data["empreinte"] = data["FOOTPRINT_SCOPE_1"] + data["FOOTPRINT_SCOPE_2"] + data["FOOTPRINT_SCOPE_3"]
pf["empreinte"] = pf["FOOTPRINT_SCOPE_1"] + pf["FOOTPRINT_SCOPE_2"] + pf["FOOTPRINT_SCOPE_3"]
data["WACI"] = data["INTENSITY_SCOPE_1"] + data["INTENSITY_SCOPE_2"]
pf["WACI"] = pf["INTENSITY_SCOPE_1"] + pf["INTENSITY_SCOPE_2"]


def moyenne(table, colonne, poids):
    ok = table[colonne].notna()
    return (table.loc[ok, colonne] * poids[ok]).sum() / poids[ok].sum()


def mediane(table, colonne, poids):
    # médiane pondérée : moins sensible aux valeurs extrêmes (ex. cash-flow négatif des réseaux qui investissent)
    t = pd.DataFrame({"v": table[colonne], "p": poids}).dropna().sort_values("v")
    return t.loc[t["p"].cumsum() >= t["p"].sum() / 2, "v"].iloc[0]


extra_financier = {
    "Empreinte carbone scopes 1+2+3 (tCO2e / M$ investi)": "empreinte",
    "Intensité carbone scopes 1+2 (tCO2e / M$ de CA)": "WACI",
    "Température implicite (°C)": "ITR",
    "CA aligné Taxonomie UE (%)": "EST_EU_TAXONOMY_MAX_REV",
    "Pilier environnement MSCI (/10)": "ENVIRONMENTAL_PILLAR_SCORE",
}
financier = {   # médianes pondérées
    "PER (médiane)": "PE ratio",
    "Rendement du cash-flow libre, % (médiane)": "FCF yield",
    "ROIC, % (médiane)": "ROIC",
    "Marge nette, % (médiane)": "Net margin",
    "Dette / actifs, % (médiane)": "Debt assets",
    "Rendement annualisé 5 ans 2020-2024 (médiane)": "Annualized return 5Y",
    "Volatilité 5 ans (médiane)": "Volatility 5Y",
}
caracteristiques = pd.concat([
    pd.DataFrame({"Fonds": [moyenne(pf, c, pf["Poids"]) for c in extra_financier.values()],
                  "MSCI World": [moyenne(data, c, msci) for c in extra_financier.values()]}, index=extra_financier.keys()),
    pd.DataFrame({"Fonds": [mediane(pf, c, pf["Poids"]) for c in financier.values()],
                  "MSCI World": [mediane(data, c, msci) for c in financier.values()]}, index=financier.keys()),
])
print("\nCaractéristiques :\n", caracteristiques.round(2))

# ---------------------------------------------------------------- cours de Bourse
# les 15 plus grosses valeurs du MSCI World, pour expliquer l'écart de performance
geants = data.nlargest(15, "Weight in MSCI World")
# ETF sur notre indice de référence (MSCI World Climate Paris Aligned) : on prend le premier code qui répond
etf_pab = ["PABV.DE", "WPAB.L", "PABW.DE"]

fichier = "donnees_complementaires/prix_analyse.csv"
tickers = sorted(set(pf["ticker_yahoo"]) | set(geants["ticker_yahoo"]) | {"URTH"} | set(etf_pab))
deja = pd.read_csv(fichier, nrows=0).columns if os.path.exists(fichier) else []
if any(t not in deja for t in tickers):
    prix = yf.download(tickers, start="2019-12-01", end="2026-11-14", auto_adjust=True)["Close"]
    prix.to_csv(fichier)

prix = pd.read_csv(fichier, index_col=0, parse_dates=True).resample("ME").last()
change = pd.read_csv("donnees_complementaires/change.csv", index_col=0, parse_dates=True).resample("ME").last()

# conversion en euros (les cours de Londres sont en pence)
devise = dict(zip(data["ticker_yahoo"], data["currency"]))
devise.update(dict(zip(pf["ticker_yahoo"], pf["currency"])))
devise.update({"URTH": "USD", "PABV.DE": "EUR", "PABW.DE": "EUR", "WPAB.L": "USD"})
for t in prix.columns:
    d = devise.get(t, "USD")
    if d == "GBp":
        prix[t] = prix[t] / 100 / change["GBP"]
    elif d != "EUR":
        prix[t] = prix[t] / change[d]
rendements = prix.pct_change().iloc[1:]

poids = pf.set_index("ticker_yahoo")["Poids"]
fonds = (rendements[poids.index] * poids).sum(axis=1) - 0.0075 / 12   # 0,75 % de frais par an
marche = rendements["URTH"]

# ---------------------------------------------------------------- 3. risque face au MSCI World


def risque(debut, fin):
    f, m = fonds[debut:fin], marche[debut:fin]
    beta = np.cov(f, m)[0, 1] / m.var()
    ecart = (f - m).std() * np.sqrt(12)
    surperf = ((1 + f).prod() ** (12 / len(f)) - 1) - ((1 + m).prod() ** (12 / len(m)) - 1)
    return {"Bêta": beta,
            "Corrélation": f.corr(m),
            "Écart de suivi (tracking error)": ecart,
            "Surperformance annualisée": surperf,
            "Ratio d'information": surperf / ecart,
            "Mois où le fonds bat le marché": (f > m).mean()}


risques = pd.DataFrame({"2020-2024": risque("2020", "2024"), "2025-2026": risque("2025", "2026")})
print("\nRisque face au MSCI World :\n", risques.round(3))

# ---------------------------------------------------------------- 4. notre indice de référence
pab = next((t for t in etf_pab if t in rendements.columns and rendements[t]["2025":].notna().sum() >= 20), None)
if pab is None:
    print("\nAucun ETF Paris-Aligned trouvé sur Yahoo Finance : comparaison avec l'indice de référence impossible")
    reference = pd.DataFrame()
else:
    debut = rendements[pab].first_valid_index()
    debut = max(debut, pd.Timestamp("2022-01-01"))
    lignes = {}
    for nom, r in [("Fonds Holocène", fonds), ("MSCI World Climate Paris Aligned (ETF " + pab + ")", rendements[pab]),
                   ("MSCI World (ETF URTH)", marche)]:
        lignes[nom] = {}
        for periode, (a, b) in {"Depuis " + debut.strftime("%m/%Y"): (debut, "2026"), "2025-2026": ("2025", "2026")}.items():
            x = r[a:b].dropna()
            lignes[nom][f"Performance cumulée {periode}"] = (1 + x).prod() - 1
            lignes[nom][f"Volatilité {periode}"] = x.std() * np.sqrt(12)
    reference = pd.DataFrame(lignes)
    print("\nFace à notre indice de référence :\n", reference.round(3))

# ---------------------------------------------------------------- 5. d'où vient l'écart : les géants du MSCI World
geants = geants.copy()
geants["Poids dans le MSCI World"] = msci[geants.index]
geants["Performance 2025-2026"] = [(1 + rendements[t]["2025":"2026"]).prod() - 1 if t in rendements.columns else np.nan
                                   for t in geants["ticker_yahoo"]]
geants["Contribution au MSCI World (points)"] = geants["Poids dans le MSCI World"] * geants["Performance 2025-2026"]
geants["Dans le fonds ?"] = np.where(geants["ticker_yahoo"].isin(pf["ticker_yahoo"]), "Oui", "Non")
etapes = pd.read_csv("resultats/etape_1_extra_financier.csv").drop_duplicates("name").set_index("name")["etape"]
geants["Pourquoi pas dans le fonds"] = [etapes.get(n, "") if dedans == "Non" else "" for n, dedans in zip(geants["name"], geants["Dans le fonds ?"])]
geants = geants[["name", "gics_sector_name", "Poids dans le MSCI World", "Performance 2025-2026",
                 "Contribution au MSCI World (points)", "Dans le fonds ?", "Pourquoi pas dans le fonds"]]
print("\nLes 15 plus grosses valeurs du MSCI World en 2025-2026 :\n", geants.round(3).to_string(index=False))
print("Contribution totale de ces 15 valeurs au MSCI World :",
      round(geants["Contribution au MSCI World (points)"].sum() * 100, 1), "points")

# ---------------------------------------------------------------- 6. contribution de chaque ligne du fonds
contributions = pd.DataFrame({
    "Entreprise": pf["name"].values,
    "Secteur": pf["gics_sector_name"].values,
    "Poids": pf["Poids"].values,
    "Performance 2025-2026": [(1 + rendements[t]["2025":"2026"]).prod() - 1 for t in pf["ticker_yahoo"]],
})
contributions["Contribution (points)"] = contributions["Poids"] * contributions["Performance 2025-2026"]
contributions = contributions.sort_values("Contribution (points)", ascending=False)
print("\nLes 5 lignes qui ont le plus rapporté en 2025-2026 :\n", contributions.head(5).round(3).to_string(index=False))
print("\nLes 5 lignes qui ont le plus coûté en 2025-2026 :\n", contributions.tail(5).round(3).to_string(index=False))

contrib_secteur = contributions.groupby("Secteur")[["Poids", "Contribution (points)"]].sum().sort_values(
    "Contribution (points)", ascending=False)

# ---------------------------------------------------------------- fichier Excel
with pd.ExcelWriter("resultats/Analyse_comparaison.xlsx") as fichier_excel:
    secteurs.to_excel(fichier_excel, sheet_name="Secteurs")
    regions.to_excel(fichier_excel, sheet_name="Régions")
    caracteristiques.to_excel(fichier_excel, sheet_name="Caractéristiques")
    risques.to_excel(fichier_excel, sheet_name="Risque vs MSCI World")
    reference.to_excel(fichier_excel, sheet_name="Indice de référence")
    geants.to_excel(fichier_excel, sheet_name="Géants du MSCI World", index=False)
    contributions.to_excel(fichier_excel, sheet_name="Contribution par ligne", index=False)
    contrib_secteur.to_excel(fichier_excel, sheet_name="Contribution par secteur")
print("\nFichier écrit : resultats/Analyse_comparaison.xlsx")
