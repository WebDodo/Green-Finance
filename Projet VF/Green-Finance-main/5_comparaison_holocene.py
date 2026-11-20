# Fonds Holocène Actions Monde - Partie 5 : notre méthode appliquée aux indices
# Question : si on note le MSCI World et l'indice Paris-Aligned avec NOTRE méthode, que donnent-ils ?
# On compare trois portefeuilles :
#   - le fonds Holocène (49 lignes, nos poids)
#   - le MSCI World (1 247 entreprises, poids de marché)
#   - une approximation de l'indice Paris-Aligned : le MSCI World sans les exclusions
#     réglementaires Paris-Aligned (énergies fossiles, charbon, armes controversées, tabac,
#     violations du Pacte mondial), repondéré. Le vrai indice va plus loin (il réduit aussi
#     le poids des entreprises les plus émettrices) : c'est donc une approximation.
# À lancer après 1_selection_extra_financiere.py et 2_portefeuille.py. Pas de téléchargement.

import pandas as pd

df = pd.read_csv("resultats/etape_1_extra_financier.csv")
pf = pd.read_excel("resultats/Holocene_Portefeuille.xlsx", sheet_name="Portefeuille")

# ---------------------------------------------------------------- score Holocène pour TOUT l'univers
# même formule qu'à l'étape C, mais les percentiles sont calculés sur les 1 247 entreprises
odd = lambda i: df[f"SDG_{i:02d}_NET_ALIGNMENT_SCORE"]
taxo = df["EST_EU_TAXONOMY_MAX_REV"].fillna(0)
df["contribution"] = (odd(6).clip(lower=0) + odd(7).clip(lower=0) + odd(12).clip(lower=0)
                      + odd(13).clip(lower=0) + taxo / 10)
df["intensite_totale"] = df["INTENSITY_SCOPE_1"] + df["INTENSITY_SCOPE_2"] + df["INTENSITY_SCOPE_3"]
df["score_univers"] = (0.5 * df["contribution"].rank(pct=True) * 100
                       + 0.25 * df.groupby("gics_sector_name")["ITR"].rank(pct=True, ascending=False) * 100
                       + 0.25 * df.groupby("gics_sector_name")["intensite_totale"].rank(pct=True, ascending=False) * 100)

# ---------------------------------------------------------------- les poids des trois portefeuilles
poids_fonds = df["isin"].map(pf.set_index("ISIN")["Poids"]).fillna(0)
poids_msci = df["Weight in MSCI World"].fillna(0)

exclu_pab = (df["etape"].str.startswith(("A1 Pétrole", "A1 Charbon", "A1 Mines", "A1 Électricité"))
             | (df["TOB_PRODUCER"] > 0) | (df["CWEAP_TIE"] > 0)
             | (df["SOCIAL_CONTROVERSY_SCORE"] == 0) | (df["GOVERNANCE_CONTROVERSY_SCORE"] == 0))
poids_pab = poids_msci.where(~exclu_pab, 0)

portefeuilles = {"Fonds Holocène": poids_fonds,
                 "Indice Paris-Aligned (approximation)": poids_pab,
                 "MSCI World": poids_msci}

# ---------------------------------------------------------------- les indicateurs
df["empreinte"] = df["FOOTPRINT_SCOPE_1"] + df["FOOTPRINT_SCOPE_2"] + df["FOOTPRINT_SCOPE_3"]
meilleur_odd = df[["SDG_06_NET_ALIGNMENT_SCORE", "SDG_07_NET_ALIGNMENT_SCORE",
                   "SDG_12_NET_ALIGNMENT_SCORE", "SDG_13_NET_ALIGNMENT_SCORE"]].max(axis=1)
df["passe_article_9"] = df["perimetre_404"] * 100                       # passe nos étapes A et B
df["contribution_forte"] = ((meilleur_odd >= 5) | (taxo >= 1)) * 100    # notre règle de l'étape C
df["vert_zero"] = (taxo == 0) * 100
df["exclu_par_nous"] = df["etape"].str.startswith("A") * 100            # refusé à notre étape A


def moyenne(colonne, poids):
    ok = df[colonne].notna() & (poids > 0)
    return (df.loc[ok, colonne] * poids[ok]).sum() / poids[ok].sum()


indicateurs = {
    "Score Holocène moyen (/100)": "score_univers",
    "Part du poids qui passe notre test Article 9 (%)": "passe_article_9",
    "Part du poids avec une contribution forte (%)": "contribution_forte",
    "Part du poids refusée à notre étape A (%)": "exclu_par_nous",
    "Part du poids sans aucune activité verte (%)": "vert_zero",
    "CA aligné Taxonomie UE (%)": "EST_EU_TAXONOMY_MAX_REV",
    "Empreinte carbone scopes 1+2+3 (tCO2e / M$ investi)": "empreinte",
    "Température implicite (°C)": "ITR",
}
comparaison = pd.DataFrame({nom: [moyenne(c, w) for c in indicateurs.values()]
                            for nom, w in portefeuilles.items()}, index=indicateurs.keys())
print(comparaison.round(1))

# ---------------------------------------------------------------- pourquoi le poids des indices est refusé
# pour le MSCI World et l'indice Paris-Aligned : à quelle étape de notre méthode leur poids disparaît
etape_courte = df["etape"].str.split(" ").str[0].replace({"Sélection": "Retenue (C, D)", "Portefeuille": "Retenue (C, D)"})
refus = pd.DataFrame({nom: w.groupby(etape_courte).sum() / w.sum() * 100
                      for nom, w in portefeuilles.items() if nom != "Fonds Holocène"}).fillna(0)
print("\nOù notre méthode écarte le poids des indices (%) :\n", refus.round(1))

with pd.ExcelWriter("resultats/Comparaison_methode_Holocene.xlsx") as fichier:
    comparaison.to_excel(fichier, sheet_name="Comparaison")
    refus.to_excel(fichier, sheet_name="Où le poids est écarté")
print("\nFichier écrit : resultats/Comparaison_methode_Holocene.xlsx")
