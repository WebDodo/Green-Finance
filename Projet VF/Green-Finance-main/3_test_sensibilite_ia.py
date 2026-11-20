# Fonds Holocène Actions Monde - Partie 3 : test de sensibilité « IA »
# Question : que se passerait-il si on assouplissait le filtre de risque (E3)
# pour laisser entrer les fabricants de puces de l'IA (NVIDIA, AMD) ?
# On compare deux versions du fonds, toutes les autres règles restant identiques :
#   - le fonds actuel   : volatilité 5 ans <= 45 % et pire baisse > -60 %
#   - le fonds « IA »   : volatilité 5 ans <= 55 % et pire baisse > -65 %
# À lancer après 1_selection_extra_financiere.py et 2_portefeuille.py
# Ce test n'a PAS servi à construire le fonds : il est présenté en annexe.

import os
import numpy as np
import pandas as pd
import yfinance as yf

df = pd.read_csv("resultats/etape_1_extra_financier.csv")
selection = df[df["etape"].isin(["Sélection", "Portefeuille", "E Filtres financiers", "F Score final trop bas"])]

# score financier calculé sur les 404 du périmètre, comme dans le script 2
p = df[df["perimetre_404"]].copy()
for colonne, nom in [("ROIC", "pct_qualite"), ("Sharpe 5Y", "pct_sharpe"), ("FCF yield", "pct_prix")]:
    p[nom] = p.groupby("gics_sector_name")[colonne].rank(pct=True) * 100
p["score_financier"] = ((p["pct_qualite"] + p["pct_sharpe"] + p["pct_prix"]) / 3).round()


def construire_fonds(vol_max, baisse_max):
    # mêmes étapes E, F, G que le script 2, seul le filtre de risque change
    s = selection.copy()
    rentable = (s["ROIC"] > 0) & (s["Net margin"] > 0)
    dette_max = np.where(s["gics_sector_name"].isin(["Utilities", "Real Estate"]), 70, 60)
    pas_trop_endettee = s["Debt assets"].fillna(0) <= dette_max
    risque_ok = (s["Volatility 5Y"] <= vol_max) & (s["Max drawdown 5Y"] > baisse_max)
    s = s[rentable & pas_trop_endettee & risque_ok]

    s = s.join(p["score_financier"])
    s["score_final"] = 0.6 * s["score_Holocene"] + 0.4 * s["score_financier"]
    s = s.sort_values("score_final", ascending=False)
    s = s.drop_duplicates("ticker_yahoo")
    pf = s.groupby("gics_sector_name").head(11).head(50).copy()

    pf["poids"] = pf["score_Holocene"]
    pf["poids"] = pf["poids"] / pf["poids"].sum()
    pf["poids"] = pf["poids"].clip(0.01, 0.05)
    pf["poids"] = pf["poids"] / pf["poids"].sum()
    pf["ticker_yahoo"] = pf["ticker_yahoo"].replace({"CICT.SI": "C38U.SI", "CLAR.SI": "A17U.SI"})
    return pf.sort_values("poids", ascending=False)


actuel = construire_fonds(0.45, -0.60)
ia = construire_fonds(0.55, -0.65)

print("Lignes : fonds actuel", len(actuel), "/ fonds IA", len(ia))
print("Entrent dans le fonds IA :", sorted(set(ia["name"]) - set(actuel["name"])))
print("Sortent du fonds IA :", sorted(set(actuel["name"]) - set(ia["name"])))

# ---------------------------------------------------------------- cours de Bourse
# fichier séparé pour ne pas toucher aux données du fonds principal
fichier = "donnees_complementaires/prix_test_ia.csv"
tickers = sorted(set(actuel["ticker_yahoo"]) | set(ia["ticker_yahoo"]) | {"URTH"})
deja = pd.read_csv(fichier, nrows=0).columns if os.path.exists(fichier) else []
if any(t not in deja for t in tickers):
    prix = yf.download(tickers, start="2019-12-01", end="2026-11-14", auto_adjust=True)["Close"]
    prix.to_csv(fichier)

prix = pd.read_csv(fichier, index_col=0, parse_dates=True).resample("ME").last()
change = pd.read_csv("donnees_complementaires/change.csv", index_col=0, parse_dates=True).resample("ME").last()
estr = pd.read_csv("donnees_complementaires/estr.csv", index_col=0, parse_dates=True)["estr"]

# conversion en euros (les cours de Londres sont en pence)
devise = dict(zip(actuel["ticker_yahoo"], actuel["currency"]))
devise.update(dict(zip(ia["ticker_yahoo"], ia["currency"])))
devise["URTH"] = "USD"
for t in prix.columns:
    if devise[t] == "GBp":
        prix[t] = prix[t] / 100 / change["GBP"]
    elif devise[t] != "EUR":
        prix[t] = prix[t] / change[devise[t]]
rendements = prix.pct_change().iloc[1:]


def performance(pf, debut, fin, frais=0.0075):
    poids = pf.set_index("ticker_yahoo")["poids"]
    r = (rendements[poids.index] * poids).sum(axis=1) - frais / 12   # 0,75 % de frais par an
    r = r[debut:fin]
    valeur = (1 + r).cumprod()
    perf_annuelle = valeur.iloc[-1] ** (12 / len(r)) - 1
    vol = r.std() * np.sqrt(12)
    return {"Performance cumulée": valeur.iloc[-1] - 1,
            "Performance annualisée": perf_annuelle,
            "Volatilité": vol,
            "Sharpe": (perf_annuelle - estr[debut:fin].mean() / 100) / vol,
            "Pire baisse": (valeur / valeur.cummax() - 1).min()}


msci = pd.DataFrame({"ticker_yahoo": ["URTH"], "poids": [1.0]})   # l'ETF MSCI World, sans nos frais

# ---------------------------------------------------------------- caractéristiques vertes
df["empreinte"] = df["FOOTPRINT_SCOPE_1"] + df["FOOTPRINT_SCOPE_2"] + df["FOOTPRINT_SCOPE_3"]
connue = df["empreinte"].notna()
empreinte_msci = (df.loc[connue, "empreinte"] * df.loc[connue, "Weight in MSCI World"]).sum() / df.loc[connue, "Weight in MSCI World"].sum()


def vert(pf):
    emp = (df.loc[pf.index, "empreinte"] * pf["poids"]).sum() / pf["poids"].sum()
    return {"Lignes": len(pf),
            "Empreinte carbone vs MSCI World": emp / empreinte_msci - 1,
            "Température implicite (°C)": (pf["ITR"] * pf["poids"]).sum(),
            "CA Taxonomie UE (%)": (pf["EST_EU_TAXONOMY_MAX_REV"].fillna(0) * pf["poids"]).sum(),
            "Poids des semi-conducteurs": pf.loc[pf["industry_group"] == "Semiconductors", "poids"].sum()}


comparaison = pd.DataFrame({
    "Fonds actuel": {**vert(actuel), **{f"{k} 2020-2024": v for k, v in performance(actuel, "2020", "2024").items()},
                     **{f"{k} 2025-2026": v for k, v in performance(actuel, "2025", "2026").items()}},
    "Fonds IA (risque assoupli)": {**vert(ia), **{f"{k} 2020-2024": v for k, v in performance(ia, "2020", "2024").items()},
                                   **{f"{k} 2025-2026": v for k, v in performance(ia, "2025", "2026").items()}},
    "MSCI World": {**{f"{k} 2020-2024": v for k, v in performance(msci, "2020", "2024", frais=0).items()},
                   **{f"{k} 2025-2026": v for k, v in performance(msci, "2025", "2026", frais=0).items()}},
})
print("\n", comparaison.round(3))

colonnes = ["name", "gics_sector_name", "industry_group", "poids", "score_Holocene", "Volatility 5Y", "Max drawdown 5Y"]
with pd.ExcelWriter("resultats/Test_sensibilite_IA.xlsx") as fichier_excel:
    comparaison.to_excel(fichier_excel, sheet_name="Comparaison")
    ia[colonnes].to_excel(fichier_excel, sheet_name="Fonds IA", index=False)
    actuel[colonnes].to_excel(fichier_excel, sheet_name="Fonds actuel", index=False)
print("\nFichier écrit : resultats/Test_sensibilite_IA.xlsx")
