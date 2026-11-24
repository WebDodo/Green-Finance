# Fonds Holocène Actions Monde - Partie 1 : sélection extra-financière
# 1247 entreprises du MSCI World -> 125 entreprises
# Étapes A (exclusions), B (test Article 9), C (score Holocène), D (revue qualitative)

import pandas as pd

df = pd.read_csv("../data/all_data.csv")
df["etape"] = ""   # on note ici la première règle qui exclut l'entreprise


def exclure(condition, motif):
    # on n'écrase pas une entreprise déjà exclue par une règle précédente
    df.loc[condition & (df["etape"] == ""), "etape"] = motif
    print(f"{motif:45s} reste {(df['etape'] == '').sum()}")


def simplifier(nom):
    # "Glencore PLC" -> "glencore" pour comparer les noms MSCI et ceux des bases charbon
    nom = str(nom).lower().replace(".", "").replace(",", "").replace("&", " ")
    mots_inutiles = ["plc", "inc", "ltd", "corp", "co", "sa", "ag", "nv", "se", "holdings", "group", "the"]
    return " ".join(m for m in nom.split() if m not in mots_inutiles)


df["nom_simple"] = df["name"].apply(simplifier)

# ---------------------------------------------------------------- bases charbon
# Global Coal Exit List : part du chiffre d'affaires issue du charbon
# Attention : la colonne est une fraction (0.03 = 3 %) même si l'en-tête dit "in %"
gcel = pd.read_excel("Urgewald GCEL 2026 V1.0.xlsx", sheet_name="GCEL", header=3).iloc[1:]
gcel["part_charbon"] = pd.to_numeric(gcel["Coal Share of Revenue"], errors="coerce")
gcel = gcel[gcel["part_charbon"] >= 0.01]
noms_gcel = set(gcel["Parent Company"].apply(simplifier)) | set(gcel["Company"].apply(simplifier))

# Global Coal Mine Tracker : propriétaires des mines, écrits "BHP [50%]; Mitsubishi Corp [50%]"
mines = pd.read_excel("Global Coal Mine Tracker, August 2026.xlsx", sheet_name="Non-closed mines")
mines["production"] = pd.to_numeric(mines["Production (Mtpa)"], errors="coerce")
mines = mines[(mines["Status"] == "Operating") & (mines["production"] > 0.5)]
noms_mines = set()
for proprietaires in mines["Parent Company"].dropna():
    for proprietaire in proprietaires.split(";"):
        if "[" in proprietaire:
            nom, part = proprietaire.split("[")
            if float(part.replace("%]", "")) >= 10:
                noms_mines.add(simplifier(nom))

# ---------------------------------------------------------------- étape A : ce qu'on refuse
taxo = df["EST_EU_TAXONOMY_MAX_REV"].fillna(0)   # part du chiffre d'affaires alignée Taxonomie UE (%)
odd = lambda i: df[f"SDG_{i:02d}_NET_ALIGNMENT_SCORE"]

# A1 énergies fossiles
exclure(df["gics_sector_name"] == "Energy", "A1 Pétrole et gaz")
electricien_sale = (df["gics_sector_name"] == "Utilities") & (taxo < 50) & (df["INTENSITY_SCOPE_1"] >= 100)
exclure(electricien_sale, "A1 Électricité carbonée")
exclure(df["nom_simple"].isin(noms_gcel), "A1 Charbon (GCEL >= 1 % du CA)")
exclure(df["nom_simple"].isin(noms_mines), "A1 Mines de charbon")

# A2 financement des fossiles : toutes les financières sauf paiement et notation
paiement = df["industry_group"].isin(["Commercial Services", "Software"])
exclure((df["gics_sector_name"] == "Financials") & ~paiement, "A2 Financières")

# A3 secteurs incompatibles avec les limites planétaires
exclure(df["industry_group"].isin(["Airlines", "Auto Manufacturers", "Auto Parts&Equipment", "Agriculture"]),
        "A3 Aérien, automobile, négoce agricole")

# A4 garde-fous
exclure(df[["IVA_COMPANY_RATING", "ITR", "INTENSITY_SCOPE_1"]].isna().any(axis=1), "A4 Données manquantes")
exclure(df["ENVIRONMENT_CONTROVERSY_SCORE"] <= 1, "A4 Controverse environnementale")
exclure((df["SOCIAL_CONTROVERSY_SCORE"] == 0) | (df["GOVERNANCE_CONTROVERSY_SCORE"] == 0),
        "A4 Controverse sociale ou gouvernance")
exclure(df["TOB_PRODUCER"] > 0, "A4 Tabac")
exclure(df["CWEAP_TIE"] > 0, "A4 Armes controversées")
exclure((odd(6) <= -5) | (odd(12) <= -5) | (odd(14) <= -5) | (odd(15) <= -5), "A4 ODD <= -5")

# ---------------------------------------------------------------- étape B : test Article 9
contribue = (odd(13) >= 2) | (odd(7) >= 2) | (odd(6) >= 2) | (odd(12) >= 2) | (taxo >= 20)
ne_nuit_pas = (odd(6) > -2) & (odd(12) > -2) & (odd(13) > -2) & (odd(14) > -2) & (odd(15) > -2) & (df["ITR"] <= 3)
gouvernance = df["GOVERNANCE_PILLAR_SCORE"] >= 3
exclure(~(contribue & ne_nuit_pas & gouvernance), "B Échoue au test Article 9")
df["perimetre_404"] = df["etape"] == ""

# ---------------------------------------------------------------- étape C : score Holocène
# 50 % contribution (comparée à tout le périmètre)
# 25 % température implicite + 25 % intensité carbone (comparées au secteur)
p = df[df["perimetre_404"]].copy()
p["contribution"] = (odd(6).clip(lower=0) + odd(7).clip(lower=0) + odd(12).clip(lower=0)
                     + odd(13).clip(lower=0) + taxo / 10)
p["intensite_totale"] = p["INTENSITY_SCOPE_1"] + p["INTENSITY_SCOPE_2"] + p["INTENSITY_SCOPE_3"]

# percentile = "fait mieux que X % des entreprises comparées"
p["pct_contribution"] = p["contribution"].rank(pct=True) * 100
p["pct_trajectoire"] = p.groupby("gics_sector_name")["ITR"].rank(pct=True, ascending=False) * 100
p["pct_pollution"] = p.groupby("gics_sector_name")["intensite_totale"].rank(pct=True, ascending=False) * 100
p["score_Holocene"] = (0.5 * p["pct_contribution"] + 0.25 * p["pct_trajectoire"]
                       + 0.25 * p["pct_pollution"]).round()

colonnes_score = ["pct_contribution", "pct_trajectoire", "pct_pollution", "score_Holocene"]
df[colonnes_score] = p[colonnes_score]
exclure(df["score_Holocene"] < 60, "C Score Holocène < 60")

# ---------------------------------------------------------------- étape D : revue qualitative
# nos données n'ont pas de colonne "or" ou "saumon" : seule étape avec des noms écrits à la main
exclure(df["name"].str.contains("Newmont|Barrick|Agnico Eagle|Northern Star|Franco-Nevada|Wheaton|Chow Tai Fook"),
        "D Or")
exclure(df["name"].str.contains("Mowi|Salmar"), "D Saumon d'élevage")
exclure(df["name"].str.contains("Industria de Diseno|Hennes & Mauritz|Fast Retailing|Associated British Foods"),
        "D Fast fashion")
exclure(df["name"].str.contains("Carnival|Royal Caribbean|Amadeus IT"), "D Croisières et vols")

df.loc[df["etape"] == "", "etape"] = "Sélection 125"
df.to_csv("resultats/etape_1_extra_financier.csv", index=False)
print("\nFichier écrit : resultats/etape_1_extra_financier.csv")
