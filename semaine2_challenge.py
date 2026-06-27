#====================================================================
# AKIENI  ACADEMY-Projet sante publique
# semaine 2:CHALLENGE ENTREPRISE — Demande Urgente du Responsable DSS 
#====================================================================

#====================================================================

#---SECTION 1: DECLARATIONS DE TOUTES LES VARIABLES ---

#====================================================================

#Hopital District Kinkala NOTée h_1
#DONNES h1
h1_budget_trim_fcfa = 12_500_000
h1_nb_consultation_ext = 1_847
h1_nb_hospitalisations = 312
h1_nb_deces_hospitaliers = 8
h1_nb_lits_totaux  = 45
h1_nb_lits_occupes = 41
h1_nb_medecins_permanants = 3
h1_population_desservie  = 85_000
#CMS de VINDZA NOTée h2
#DONNES h2
h2_budget_trim_fcfa = 6_800_000
h2_nb_consultation_ext = 923
h2_nb_hospitalisations =87
h2_nb_deces_hospitaliers = 2
h2_nb_lits_totaux = 20
h2_nb_lits_occupes = 14
h2_nb_medecins_permanants = 1
h2_population_desservie = 42_000
#HOPITAL DE KINDAMBA NOTée h3
#DONNEES h3
h3_budget_trim_fcfa = 9_200_000
h3_nb_consultation_ext = 1_234
h3_nb_hospitalisations = 201
h3_nb_deces_hospitaliers = 11
h3_nb_lits_totaux = 35
h3_nb_lits_occupes = 33
h3_nb_medecins_permanants = 2
h3_population_desservie = 67_000
#====================================================================

#---SECTION 2: CALCUL POUR CHAQUE HOPITAL---

#====================================================================

#HOPITAL DISTRICT KINKALA
#calcul du nombre totals patients
h1_totales_patients = h1_nb_consultation_ext + h1_nb_hospitalisations
#cout moyen par patient 
h1_cout_moyen_patients = round(h1_budget_trim_fcfa /h1_totales_patients ,2)
h1_taux_occupation = (h1_nb_lits_occupes/h1_nb_lits_totaux)*100
h1_densite_medicale = (h1_nb_medecins_permanants/h1_population_desservie)*1000
h1_taux_mortalite = (h1_nb_deces_hospitaliers/h1_nb_hospitalisations)*1000
h1_situation_critique = ((h1_taux_mortalite >2.0 ) or (h1_densite_medicale < 0.05))

#CMS DE VINDZA h2
#calcul du nombre totals patients
h2_totales_patients = h2_nb_consultation_ext + h2_nb_hospitalisations
#cout moyen par patient 
h2_cout_moyen_patients = round(h2_budget_trim_fcfa / h2_totales_patients, 2)
h2_taux_occupation = (h2_nb_lits_occupes / h2_nb_lits_totaux) * 100
h2_densite_medicale = (h2_nb_medecins_permanants / h2_population_desservie) * 1000
h2_taux_mortalite = (h2_nb_deces_hospitaliers / h2_nb_hospitalisations) * 1000
h2_situation_critique = ((h2_taux_mortalite >2.0 ) or (h2_densite_medicale < 0.05))

#HOPITAL DE KINDAMBA h3
#calcul du nombre totals patients
h3_totales_patients = h3_nb_consultation_ext + h3_nb_hospitalisations
#cout moyen par patient 
h3_cout_moyen_patients = round(h3_budget_trim_fcfa / h3_totales_patients, 2)
h3_taux_occupation = (h3_nb_lits_occupes / h3_nb_lits_totaux) * 100
h3_densite_medicale = (h3_nb_medecins_permanants / h3_population_desservie) * 1000
h3_taux_mortalite = (h3_nb_deces_hospitaliers / h3_nb_hospitalisations) * 1000
h3_situation_critique = ((h3_taux_mortalite >2.0 ) or (h3_densite_medicale < 0.05))

#====================================================================

#---SECTION 3 L'ANALYSE BUDGETAIRE---

#====================================================================

cout_un_medecin = 1_200_000
h1_medecin_recruter = 5 - h1_nb_medecins_permanants
h2_medecin_recruter = 5 - h2_nb_medecins_permanants
h3_medecin_recruter = 5 - h3_nb_medecins_permanants
cout_total_de_recrutement =(h1_medecin_recruter + h2_medecin_recruter + h3_medecin_recruter) * cout_un_medecin
budget_total_actuel = h1_budget_trim_fcfa + h2_budget_trim_fcfa + h3_budget_trim_fcfa
budget_suffit = budget_total_actuel >=cout_total_de_recrutement

#====================================================================

#---SECTION 4 AFFICHAGE---

#====================================================================
print("======================================================================")
print("  RAPPORT COMPARATIF CONSOLIDÉ — DISTRICT SANITAIRE DU POOL (DSS)")
print("======================================================================")

# --- 1. HÔPITAL DISTRICT KINKALA (h1) ---
print(f"\n1. HOPITAL DISTRICT KINKALA")
print(f"   - COUT MOYEN PAR PATIENT    : {h1_cout_moyen_patients:_} FCFA".replace("_", " "))
print(f"   - TAUX D'OCCUPATION DES LITS : {h1_taux_occupation:.1f}%")
print(f"   - DENSITE MEDICALE         : {h1_densite_medicale:.3f} médecins / 1000 hab")
print(f"   - SITUATION CRITIQUE       : {h1_situation_critique}")

# --- 2. CMS DE VINDZA (h2) ---
print(f"\n2. CMS DE VINDZA")
print(f"   - COUT MOYEN PAR PATIENT    : {h2_cout_moyen_patients:_} FCFA".replace("_", " "))
print(f"   - TAUX D'OCCUPATION DES LITS : {h2_taux_occupation:.1f}%")
print(f"   - DENSITE MEDICALE         : {h2_densite_medicale:.3f} médecins / 1000 hab")
print(f"   - SITUATION CRITIQUE       : {h2_situation_critique}")

# --- 3. HÔPITAL DE KINDAMBA (h3) ---
print(f"\n3. HOPITAL DE KINDAMBA")
print(f"   - COUT MOYEN PAR PATIENT    : {h3_cout_moyen_patients:_} FCFA".replace("_", " "))
print(f"   - TAUX D'OCCUPATION DES LITS : {h3_taux_occupation:.1f}%")
print(f"   - DENSITE MEDICALE         : {h3_densite_medicale:.3f} médecins / 1000 hab")
print(f"   - SITUATION CRITIQUE       : {h3_situation_critique}")

print("\n======================================================================")
