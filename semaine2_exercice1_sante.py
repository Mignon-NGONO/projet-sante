#=============================================================
# AKIENI  ACADEMY-Projet sante publique
# semaine 2 - Exercice 1: Fiche patient CHU B/Z
# votre nom : _______________________________________________
# Date : _______________________________________________
# ============================================================

#---SECTION 1 : VARIABLES PATIENT ---
# TODO : Declarer toutes les variables patient ci -dessous 
nom_patient = 'MAVOUNGOU Celestine'
age_patient = '42'
sexe_patient = 'F'
departement_patient = 'BRAZZAVILLE'
couverture_sociale = 'CNSS'

#---SECTION 2 : VARIABLES CONSULTATION ---
# TODO : Declarer les variables consulatation
type_consultation = 'URGENCES'
cout_consultation_fcfa = 15000.0
nb_consultation = 1
remise_cnss_pct = 30.0
diagnostic_principal = 'PALUDISME GRAVE'

#--- SECTION 3 : VARIABLES HOPITAL---
# TODO : Declarer les variables hopital
nom_hopital = 'CHU B/Z'
ville_hopital = 'B/Z'
nb_lits_total = 320
nb_lits_occupes = 284
nb_medecins_actifs = 47

#--- SECTION 4 : CALCULS ---
# TODO : Calculer le cout total apres remise CNSS
cout_total_fcfa = cout_consultation_fcfa * (1-(remise_cnss_pct/100))

# TODO : Calculer le taux d'occupation (en pourcentage,arrondi a 1 decimale)
taux_occupation_pct = round((nb_lits_occupes/nb_lits_total)* 100,1)

# TODO : Calculer le ratio consulatations par medecin (ce jour)
# Hypothese : 120 consultations ont eu lieu ce matin dans toutes l'hopital
nb_consultations_hopital = 120
ratio_consultations_medecin = nb_consultations_hopital / nb_medecins_actifs
#--- SECTION5 : AFFICHAGE ---
# TODO : Afficher une fiche complete avec f-strings
print('=' * 60)
print(f'FICHE PATIENT : {nom_patient.upper()}')
print('=' * 60)
print(f'Age          : {age_patient} ans')
print(f'Sexe         : {sexe_patient}')
print(f'Departement  : {departement_patient}')
print(f'Couverture   : {couverture_sociale}')
print('-' * 60)
print(f'CONSULTATION')
print(f'Type         : {type_consultation}')
print(f'Diagnostic   : {diagnostic_principal}')
print(f'Cout unitaire: {cout_consultation_fcfa:,.0f} FCFA'.replace(',', ' '))
print(f'Remise CNSS  : {remise_cnss_pct}%')
print(f'COUT TOTAL   : {cout_total_fcfa:,.1f} FCFA'.replace(',', ' '))
print('-' * 60)
print(f'HOPITAL      : {nom_hopital}')
print(f'Ville        : {ville_hopital}')
print(f'Lits occupes : {nb_lits_occupes}/{nb_lits_total} ({taux_occupation_pct}%)')
print(f'Medecins actifs : {nb_medecins_actifs}')
print(f'Ratio consult.  : {ratio_consultations_medecin} consultations / medecin ce matin')
print('-' * 60)
print(f'STATUT       : Prise en charge validee')
print('=' * 60)

