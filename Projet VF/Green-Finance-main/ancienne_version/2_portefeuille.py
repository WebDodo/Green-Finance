# Fonds Holocène Actions Monde - Partie 2 : portefeuille
# 125 entreprises -> filtres financiers (E) -> score final et 50 lignes (F) -> poids (G)
# puis : caractéristiques vertes, contrôles réglementaires, performance passée, fichiers Excel
# À lancer après 1_selection_extra_financiere.py

import os
import numpy as np
import pandas as pd
import yfinance as yf

# on se place dans le dossier du script : le code marche d'où qu'on le lance
os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("resultats/etape_1_extra_financier.csv")

# ---------------------------------------------------------------- étape E : filtres financiers
s = df[df["etape"] == "Sélection 125"].copy()

rentable = (s["ROIC"] > 0) & (s["Net margin"] > 0)
# 70 % de dette autorisée pour les réseaux et l'immobilier (actifs régulés ou loués), 60 % sinon
dette_max = np.where(s["gics_sector_name"].isin(["Utilities", "Real Estate"]), 70, 60)
pas_trop_endettee = s["Debt assets"].fillna(0) <= dette_max   # pas de donnée = pas de dette déclarée
risque_ok = (s["Volatility 5Y"] <= 0.45) & (s["Max drawdown 5Y"] > -0.60)

print("E1 pas rentables :", list(s.loc[~rentable, "name"]))
print("E2 trop endettées :", list(s.loc[rentable & ~pas_trop_endettee, "name"]))
print("E3 trop risquées :", list(s.loc[rentable & pas_trop_endettee & ~risque_ok, "name"]))
s = s[rentable & pas_trop_endettee & risque_ok]
print("Après les filtres financiers :", len(s))

# ---------------------------------------------------------------- étape F : score final
# score financier : rentabilité (ROIC), performance/risque (Sharpe 5 ans), prix (FCF yield)
# en percentile dans le secteur, calculé sur les 404 du périmètre (assez d'entreprises par secteur)
p = df[df["perimetre_404"]].copy()
for colonne, nom in [("ROIC", "pct_qualite"), ("Sharpe 5Y", "pct_sharpe"), ("FCF yield", "pct_prix")]:
    p[nom] = p.groupby("gics_sector_name")[colonne].rank(pct=True) * 100
p["score_financier"] = ((p["pct_qualite"] + p["pct_sharpe"] + p["pct_prix"]) / 3).round()

s = s.join(p["score_financier"])
s["score_final"] = 0.6 * s["score_Holocene"] + 0.4 * s["score_financier"]

# les 50 meilleures, au plus 10 par secteur
s = s.sort_values("score_final", ascending=False)
pf = s.groupby("gics_sector_name").head(10).head(50).copy()
print("Score final de la 50e :", round(pf["score_final"].min(), 1))

# ---------------------------------------------------------------- étape G : pondération
# poids proportionnel au score final divisé par la volatilité, puis chaque ligne entre 1 % et 5 %
pf["poids"] = pf["score_final"] / pf["Volatility 5Y"]
pf["poids"] = pf["poids"] / pf["poids"].sum()
pf["poids"] = pf["poids"].clip(0.01, 0.05)
pf["poids"] = pf["poids"] / pf["poids"].sum()
pf = pf.sort_values("poids", ascending=False)

secteurs = pf.groupby("gics_sector_name")["poids"].sum().sort_values(ascending=False)
print("\nPoids par secteur :\n", (secteurs * 100).round(1))
print("\nPoids par région :\n", (pf.groupby("region_en")["poids"].sum() * 100).round(1))

# ---------------------------------------------------------------- caractéristiques vertes
df["poids"] = pf["poids"]
df["poids"] = df["poids"].fillna(0)
df["empreinte_carbone"] = df["FOOTPRINT_SCOPE_1"] + df["FOOTPRINT_SCOPE_2"] + df["FOOTPRINT_SCOPE_3"]
df["WACI"] = df["INTENSITY_SCOPE_1"] + df["INTENSITY_SCOPE_2"]
df["note_AA_AAA"] = df["IVA_COMPANY_RATING"].isin(["AA", "AAA"]) * 100
# secteurs à fort impact climatique (règle Paris-Aligned) : tout sauf services, logiciels, finance...
faible_impact = ["Software", "Internet", "Commercial Services", "Media", "Advertising", "Telecommunications",
                 "Healthcare-Services", "Lodging", "Food Service", "Entertainment", "Banks", "Insurance",
                 "Diversified Finan Serv", "Investment Companies", "Private Equity", "Holding Companies-Divers"]
df["fort_impact"] = (~df["industry_group"].isin(faible_impact)) * 100


def moyenne(colonne, poids):
    ok = df[colonne].notna() & (poids > 0)
    return (df.loc[ok, colonne] * poids[ok]).sum() / poids[ok].sum()


indicateurs = {
    "Empreinte carbone scopes 1+2+3 (tCO2e / M$ investi)": "empreinte_carbone",
    "Intensité carbone scopes 1+2 (tCO2e / M$ de CA)": "WACI",
    "Température implicite (°C)": "ITR",
    "Chiffre d'affaires Taxonomie UE (%)": "EST_EU_TAXONOMY_MAX_REV",
    "Part notée AA ou AAA par MSCI (%)": "note_AA_AAA",
    "Pilier environnement MSCI (/10)": "ENVIRONMENTAL_PILLAR_SCORE",
    "Pilier social MSCI (/10)": "SOCIAL_PILLAR_SCORE",
    "Pilier gouvernance MSCI (/10)": "GOVERNANCE_PILLAR_SCORE",
    "Secteurs à fort impact climatique (%)": "fort_impact",
}
carac = pd.DataFrame({
    "Fonds": [moyenne(c, df["poids"]) for c in indicateurs.values()],
    "MSCI World": [moyenne(c, df["Weight in MSCI World"]) for c in indicateurs.values()],
}, index=indicateurs.keys())
carac["Écart"] = carac["Fonds"] / carac["MSCI World"] - 1
print("\n", carac.round(2))

# ---------------------------------------------------------------- contrôles réglementaires
empreinte_fonds, empreinte_msci = carac.iloc[0, 0], carac.iloc[0, 1]
controles = pd.DataFrame([
    ["OPCVM 5/10/40 : aucune ligne > 10 %", pf["poids"].max() <= 0.10],
    ["OPCVM 5/10/40 : lignes > 5 % au total <= 40 %", pf.loc[pf["poids"] > 0.05, "poids"].sum() <= 0.40],
    ["Notre règle : chaque secteur <= 25 %", secteurs.max() <= 0.25],
    ["Article 9 : 100 % des lignes passent le test B", pf["perimetre_404"].all()],
    ["Paris-Aligned : empreinte carbone <= 50 % du MSCI World", empreinte_fonds <= 0.5 * empreinte_msci],
    ["Paris-Aligned : fort impact climatique >= MSCI World", carac.iloc[-1, 0] >= carac.iloc[-1, 1]],
    ["Label ISR : au moins 30 % de l'univers écarté", 1 - df["perimetre_404"].mean() >= 0.30],
], columns=["Règle", "Respectée"])
print("\n", controles)

# ---------------------------------------------------------------- performance passée
# cours téléchargés une seule fois puis gardés dans donnees_complementaires/
os.makedirs("donnees_complementaires", exist_ok=True)
pf["ticker_yahoo"] = pf["ticker_yahoo"].replace({"CICT.SI": "C38U.SI"})   # ancien code Yahoo de CapitaLand

if not os.path.exists("donnees_complementaires/prix.csv"):
    tickers = list(pf["ticker_yahoo"]) + ["URTH"]   # URTH = ETF iShares MSCI World, en dollars
    prix = yf.download(tickers, start="2019-12-01", end="2026-11-14", auto_adjust=True)["Close"]
    prix.to_csv("donnees_complementaires/prix.csv")
    devises = ["USD", "GBP", "JPY", "CHF", "CAD", "SEK", "DKK", "NOK", "SGD", "NZD"]
    change = yf.download([f"EUR{d}=X" for d in devises], start="2019-12-01", end="2026-11-14")["Close"]
    change.columns = [c[3:6] for c in change.columns]   # "EURUSD=X" -> "USD"
    change.to_csv("donnees_complementaires/change.csv")
    estr = pd.read_csv("https://data-api.ecb.europa.eu/service/data/EST/B.EU000A2X2A25.WT"
                       "?format=csvdata&startPeriod=2019-12-01", usecols=["TIME_PERIOD", "OBS_VALUE"])
    estr.columns = ["date", "estr"]
    estr.to_csv("donnees_complementaires/estr.csv", index=False)

# on travaille en données MENSUELLES : en quotidien, Tokyo, Paris et New York ne ferment pas
# à la même heure et les rendements seraient décalés
prix = pd.read_csv("donnees_complementaires/prix.csv", index_col=0, parse_dates=True).resample("ME").last()
change = pd.read_csv("donnees_complementaires/change.csv", index_col=0, parse_dates=True).resample("ME").last()
estr = pd.read_csv("donnees_complementaires/estr.csv", index_col=0, parse_dates=True)["estr"]

# conversion en euros (les cours de Londres sont en pence)
devise = dict(zip(pf["ticker_yahoo"], pf["currency"]))
devise["URTH"] = "USD"
for t in prix.columns:
    if devise[t] == "GBp":
        prix[t] = prix[t] / 100 / change["GBP"]
    elif devise[t] != "EUR":
        prix[t] = prix[t] / change[devise[t]]

rendements = prix.pct_change().iloc[1:]
poids = pf.set_index("ticker_yahoo")["poids"]
frais = 0.0075 / 12   # 0,75 % de frais de gestion par an
fonds = (rendements[poids.index] * poids).sum(axis=1) - frais   # poids remis à la cible chaque mois
indice = rendements["URTH"]


def stats(r, debut, fin):
    r = r[debut:fin]
    annees = len(r) / 12
    valeur = (1 + r).cumprod()
    perf_annuelle = valeur.iloc[-1] ** (1 / annees) - 1
    vol = r.std() * np.sqrt(12)
    taux_sans_risque = estr[debut:fin].mean() / 100
    return {"Performance cumulée": valeur.iloc[-1] - 1,
            "Performance annualisée": perf_annuelle,
            "Volatilité": vol,
            "Sharpe": (perf_annuelle - taux_sans_risque) / vol,
            "Pire baisse": (valeur / valeur.cummax() - 1).min()}


perf = pd.DataFrame({
    "Fonds 2020-2024": stats(fonds, "2020", "2024"),
    "MSCI World 2020-2024": stats(indice, "2020", "2024"),
    "Fonds 2025-2026": stats(fonds, "2025", "2026"),
    "MSCI World 2025-2026": stats(indice, "2025", "2026"),
})
par_annee = pd.DataFrame({"Fonds": fonds, "MSCI World": indice}).groupby(fonds.index.year).apply(
    lambda r: (1 + r).prod() - 1)
print("\n", perf.round(3))
print("\n", par_annee.round(3))

# ---------------------------------------------------------------- fichiers Excel
colonnes = {"name": "Entreprise", "isin": "ISIN", "country": "Pays", "gics_sector_name": "Secteur",
            "poids": "Poids", "score_Holocene": "Score Holocène", "score_financier": "Score financier",
            "score_final": "Score final", "IVA_COMPANY_RATING": "Note ESG MSCI", "ITR": "Température (°C)",
            "EST_EU_TAXONOMY_MAX_REV": "CA Taxonomie (%)", "Volatility 5Y": "Volatilité 5 ans"}
df.loc[pf.index, "etape"] = "Portefeuille"
df.loc[s.index.difference(pf.index), "etape"] = "F Score final trop bas"
df.loc[df["etape"] == "Sélection 125", "etape"] = "E Filtres financiers"

with pd.ExcelWriter("resultats/Holocene_Portefeuille.xlsx") as fichier:
    pf[list(colonnes)].rename(columns=colonnes).to_excel(fichier, sheet_name="Portefeuille", index=False)
    carac.to_excel(fichier, sheet_name="Caractéristiques")
    controles.to_excel(fichier, sheet_name="Contrôles", index=False)
    perf.to_excel(fichier, sheet_name="Performance")
    par_annee.to_excel(fichier, sheet_name="Performance par année")
    df[["name", "gics_sector_name", "etape", "score_Holocene"]].to_excel(fichier, sheet_name="Entonnoir 1247",
                                                                       index=False)

with pd.ExcelWriter("resultats/Holocene_Donnees_complementaires.xlsx") as fichier:
    pd.DataFrame({
        "Donnée": ["Charbon (part du CA)", "Mines de charbon", "Cours de Bourse ajustés", "Taux de change",
                   "Taux sans risque €STR", "MSCI World"],
        "Source": ["urgewald, Global Coal Exit List 2026", "Global Energy Monitor, Global Coal Mine Tracker 08/2026",
                   "Yahoo Finance (yfinance)", "Yahoo Finance (yfinance)", "Banque centrale européenne",
                   "ETF iShares MSCI World (URTH)"],
        "Où la trouver": ["Urgewald GCEL 2026 V1.0.xlsx", "Global Coal Mine Tracker, August 2026.xlsx",
                          "onglet Cours mensuels en EUR", "onglet Change", "onglet ESTR",
                          "onglet Cours mensuels en EUR, colonne URTH"],
    }).to_excel(fichier, sheet_name="Sources", index=False)
    charbon = df[df["etape"].str.startswith(("A1 Charbon", "A1 Mines"))]
    charbon[["name", "etape"]].to_excel(fichier, sheet_name="Exclus pour charbon", index=False)
    prix.resample("ME").last().to_excel(fichier, sheet_name="Cours mensuels en EUR")
    change.resample("ME").last().to_excel(fichier, sheet_name="Change (pour 1 EUR)")
    estr.to_excel(fichier, sheet_name="ESTR")

print("\nFichiers écrits dans resultats/")
