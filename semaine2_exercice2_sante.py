# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================

# ---DONNES BRUTES ---
budget_fcfa     = 87_450_000 # underscire pour lisibilite des grands nombres
nb_consultations_exit = 4823
nb_hospitalisations = 1247
nb_deces = 18
nb_lits_total = 180
nb_lits_occupes = 143
nb_medecins = 22
nb_infirmieres = 58
population_dept = 128_000
taux_eur_fcfa = 655.957
taux_usd_fcfa = 600.0

# ---A COMPLETER ---
# 1.conversions devises
budget_eur = round(budget_fcfa/taux_eur_fcfa, 2)
budget_usd = round(budget_fcfa/taux_usd_fcfa, 2)

#2. Indicateurs OMS 
densite_medicale = (nb_medecins/population_dept) * 1000
taux_mortalite =(nb_deces/nb_hospitalisations) * 1000
taux_occupation = (nb_lits_occupes/nb_lits_total) * 100

#3. Division entiere et modulo
budget_medicaments = int(budget_fcfa * 0.35)
cout_journalier_meds = 450_000
jours_stock = (budget_medicaments // cout_journalier_meds)  #division entiere //
jours_restants = (budget_medicaments % cout_journalier_meds) # modulo %

# 4.Puissance pour projection
budget_n_plus_2  = round(budget_fcfa*(1.08**2),2) # ** pour la puissance

#---AFFICHAGE RAPPORT ---
print("===RAPPORT TRIMESTRIEL Q4 2025 -Hopital General Pointe-Noire===")
print("\nBUDGET")
print(f"   Depenses Q4         : {budget_fcfa:_} FCFA".replace("_"," "))
print(f"   En euros            : {budget_eur:_} EUR".replace("_"," "))
print(f"   En dollars          : {budget_usd:_} USD".replace("_"," "))
print("\nINDICATEURS OMS")
print(f"   densite medicale    : {densite_medicale:.1f} medecins/ 1000hab [Norme OMS : >= 2.3]")
print(f"   taux mortaliite     : {taux_mortalite/10:.1f}%                   [Seuil alerte : > 2%]")
print(f"   taux occupation     : {taux_occupation:.1f}%                          [Optimal : 70-85%]")
print("\nANALYSE PHARMACIE")
print(f"   budget medicaments   : {budget_medicaments:_} FCFA".replace("_"," "))
print(f"   jours de stock       : {jours_stock} jours")
print(f"   jours depassement    : 0 jours")
