#====================================================================
# AKIENI  ACADEMY-Projet sante publique
# semaine 3:CHALLENGE ENTREPRISE — Demande du MINISTRE 
#====================================================================

#====================================================================
#---SECTION 1: DECLARATIONS DE TOUTES LES VARIABLES ---
#====================================================================

#Hopital CHU BRAZZAVILLE NOTée H1
#ONNEES H1
nb_lits_total_H1 = 320
nb_lits_occupes_H1 = 298
nb_medecins_H1 = 47
nb_meds_rupture_H1 = 2  #(SERO, vaccin)
nb_meds_alerte_H1 = 2 #(Artemether, AMOXI)

# --- DONNEES HOPITAL 2 : HOPITAL POINTE-NOIRE (H2) ---
nb_lits_total_H2 = 180
nb_lits_occupes_H2 = 143
nb_medecins_H2 = 22
nb_meds_rupture_H2 = 0
nb_meds_alerte_H2 = 1   # (Amoxicilline)

# --- DONNEES HOPITAL 3 : HOPITAL DOLISIE (H3) ---
nb_lits_total_H3 = 95
nb_lits_occupes_H3 = 91
nb_medecins_H3 = 8
nb_meds_rupture_H3 = 1   # (SRO)
nb_meds_alerte_H3 = 2    # (Artemether, Vaccin)

# --- DONNEES HOPITAL 4 : HOPITAL OWANDO (H4) ---
nb_lits_total_H4 = 45
nb_lits_occupes_H4 = 32
nb_medecins_H4 = 3
nb_meds_rupture_H4 = 3   # (SRO, Vaccin, Artemether)
nb_meds_alerte_H4 = 0

# --- DONNEES HOPITAL 5 : CMS IMPFONDO (H5) ---
nb_lits_total_H5 = 20
nb_lits_occupes_H5 = 19
nb_medecins_H5 = 1
nb_meds_rupture_H5 = 2   # (SRO, Amoxi)
nb_meds_alerte_H5 = 1    # (Vaccin)

#====================================================================
#---SECTION 2: CALCUL POUR CHAQUE HOPITAL---
#====================================================================

#HOPITAL CHU BRAZZAVILLE (H1)
taux_occupation_H1 = (nb_lits_occupes_H1/nb_lits_total_H1) * 100

# Regle 2 : niveau_triage_occupation H1
if taux_occupation_H1 > 95.0:
    niveau_triage_occupation_H1 = "[CRI]"
elif taux_occupation_H1 > 85.0:
    niveau_triage_occupation_H1 = "[ALT]"
elif taux_occupation_H1 > 70.0:
    niveau_triage_occupation_H1 = "[OK ]"
else:
    niveau_triage_occupation_H1 = "[SOU]"

# Regle Challenge : niveau_alerte_global H1
if nb_meds_rupture_H1 >= 2 or taux_occupation_H1 > 95.0:
    niveau_alerte_global_H1 = "CRITIQUE"
elif nb_meds_rupture_H1 >= 1 or taux_occupation_H1 > 85.0 or (nb_meds_alerte_H1 >= 2 and nb_medecins_H1 < 5):
    niveau_alerte_global_H1 = "PREOCCUPANT"
else:
    niveau_alerte_global_H1 = "SATISFAISANT"


#HOPITAL POINTE-NOIRE (H2)
taux_occupation_H2 = (nb_lits_occupes_H2/nb_lits_total_H2) * 100

# Regle 2 : niveau_triage_occupation H2
if taux_occupation_H2 > 95.0:
    niveau_triage_occupation_H2 = "[CRI]"
elif taux_occupation_H2 > 85.0:
    niveau_triage_occupation_H2 = "[ALT]"
elif taux_occupation_H2 > 70.0:
    niveau_triage_occupation_H2 = "[OK ]"
else:
    niveau_triage_occupation_H2 = "[SOU]"

# Regle Challenge : niveau_alerte_global H2
if nb_meds_rupture_H2 >= 2 or taux_occupation_H2 > 95.0:
    niveau_alerte_global_H2 = "CRITIQUE"
elif nb_meds_rupture_H2 >= 1 or taux_occupation_H2 > 85.0 or (nb_meds_alerte_H2 >= 2 and nb_medecins_H2 < 5):
    niveau_alerte_global_H2 = "PREOCCUPANT"
else:
    niveau_alerte_global_H2 = "SATISFAISANT"


#HOPITAL DOLISIE (H3)
taux_occupation_H3 = (nb_lits_occupes_H3/nb_lits_total_H3) * 100

# Regle 2 : niveau_triage_occupation H3
if taux_occupation_H3 > 95.0:
    niveau_triage_occupation_H3 = "[CRI]"
elif taux_occupation_H3 > 85.0:
    niveau_triage_occupation_H3 = "[ALT]"
elif taux_occupation_H3 > 70.0:
    niveau_triage_occupation_H3 = "[OK ]"
else:
    niveau_triage_occupation_H3 = "[SOU]"

# Regle Challenge : niveau_alerte_global H3
if nb_meds_rupture_H3 >= 2 or taux_occupation_H3 > 95.0:
    niveau_alerte_global_H3 = "CRITIQUE"
elif nb_meds_rupture_H3 >= 1 or taux_occupation_H3 > 85.0 or (nb_meds_alerte_H3 >= 2 and nb_medecins_H3 < 5):
    niveau_alerte_global_H3 = "PREOCCUPANT"
else:
    niveau_alerte_global_H3 = "SATISFAISANT"


#HOPITAL OWANDO (H4)
taux_occupation_H4 = (nb_lits_occupes_H4/nb_lits_total_H4) * 100

# Regle 2 : niveau_triage_occupation H4
if taux_occupation_H4 > 95.0:
    niveau_triage_occupation_H4 = "[CRI]"
elif taux_occupation_H4 > 85.0:
    niveau_triage_occupation_H4 = "[ALT]"
elif taux_occupation_H4 > 70.0:
    niveau_triage_occupation_H4 = "[OK ]"
else:
    niveau_triage_occupation_H4 = "[SOU]"

# Regle Challenge : niveau_alerte_global H4
if nb_meds_rupture_H4 >= 2 or taux_occupation_H4 > 95.0:
    niveau_alerte_global_H4 = "CRITIQUE"
elif nb_meds_rupture_H4 >= 1 or taux_occupation_H4 > 85.0 or (nb_meds_alerte_H4 >= 2 and nb_medecins_H4 < 5):
    niveau_alerte_global_H4 = "PREOCCUPANT"
else:
    niveau_alerte_global_H4 = "SATISFAISANT"


#CMS IMPFONDO (H5)
taux_occupation_H5 = (nb_lits_occupes_H5/nb_lits_total_H5) * 100

# Regle 2 : niveau_triage_occupation H5
if taux_occupation_H5 > 95.0:
    niveau_triage_occupation_H5 = "[CRI]"
elif taux_occupation_H5 > 85.0:
    niveau_triage_occupation_H5 = "[ALT]"
elif taux_occupation_H5 > 70.0:
    niveau_triage_occupation_H5 = "[OK ]"
else:
    niveau_triage_occupation_H5 = "[SOU]"

# Regle Challenge : niveau_alerte_global H5
if nb_meds_rupture_H5 >= 2 or taux_occupation_H5 > 95.0:
    niveau_alerte_global_H5 = "CRITIQUE"
elif nb_meds_rupture_H5 >= 1 or taux_occupation_H5 > 85.0 or (nb_meds_alerte_H5 >= 2 and nb_medecins_H5 < 5):
    niveau_alerte_global_H5 = "PREOCCUPANT"
else:
    niveau_alerte_global_H5 = "SATISFAISANT"


#====================================================================
#---SECTION 3: COMPTEURS ET BILANS NATIONAUX---
#====================================================================
nb_hopitaux_critiques = 0
if niveau_alerte_global_H1 == "CRITIQUE": nb_hopitaux_critiques += 1
if niveau_alerte_global_H2 == "CRITIQUE": nb_hopitaux_critiques += 1
if niveau_alerte_global_H3 == "CRITIQUE": nb_hopitaux_critiques += 1
if niveau_alerte_global_H4 == "CRITIQUE": nb_hopitaux_critiques += 1
if niveau_alerte_global_H5 == "CRITIQUE": nb_hopitaux_critiques += 1

total_ruptures = nb_meds_rupture_H1 + nb_meds_rupture_H2 + nb_meds_rupture_H3 + nb_meds_rupture_H4 + nb_meds_rupture_H5


#====================================================================
#---SECTION 4: SORTIE ATTENDUE (TABLEAU DE BORD MINISTÉRIEL)---
#====================================================================
print("================================================================")
print(" TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE")
print(" Date : 16 janvier 2026 | Pour le Conseil des Ministres")
print("================================================================")
print(" HOPITAL              OCCUPATION   ALERTES   NIVEAU GLOBAL")
print(f" CHU Brazzaville       {taux_occupation_H1:.1f}% {niveau_triage_occupation_H1}   {nb_meds_rupture_H1}R + {nb_meds_alerte_H1}A   [{niveau_alerte_global_H1}]")
print(f" Hopital Pointe-Noire  {taux_occupation_H2:.1f}% {niveau_triage_occupation_H2}   {nb_meds_rupture_H2}R + {nb_meds_alerte_H2}A   [{niveau_alerte_global_H2}]")
print(f" Hopital Dolisie       {taux_occupation_H3:.1f}% {niveau_triage_occupation_H3}   {nb_meds_rupture_H3}R + {nb_meds_alerte_H3}A   [{niveau_alerte_global_H3}]")
print(f" Hopital Owando        {taux_occupation_H4:.1f}% {niveau_triage_occupation_H4}   {nb_meds_rupture_H4}R + {nb_meds_alerte_H4}A   [{niveau_alerte_global_H4}]")
print(f" CMS Impfondo          {taux_occupation_H5:.1f}% {niveau_triage_occupation_H5}   {nb_meds_rupture_H5}R + {nb_meds_alerte_H5}A   [{niveau_alerte_global_H5}]")
print("----------------------------------------------------------------")
print(f" {nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
print(f" {total_ruptures} ruptures de stock identifiees a l'echelle nationale")
print(" RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA")
print("================================================================")
