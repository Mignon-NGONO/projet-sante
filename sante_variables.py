# =====================================================================
#MENTOR AKIENI ACADEMY
#PRESENTATIONS DE MES VARIABLES DANS LE CADRE DE DATA SCIENCE CHEZ AKIENI ACADEMY
#DURONT 24 SEMAINES ILS SERONT AJOUTER OU VOIR ACTUALISER
# =====================================================================

# =====================================================================
# SECTION A : CONSTANTES NATIONALES ET NORMES OMS
# =====================================================================

TAUX_EUR_FCFA = 655.957  # Taux fixe CFA / Euro
TAUX_USD_FCFA = 600.0    # Taux approximatif Dollar
SEUIL_OMS_DENSITE_MEDICALE = 2.3  # Médecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0 # Pourcentage minimum
SEUIL_MORTALITE_ALERTE = 2.0      # Seuil d'alerte en %
SEUIL_RUPTURE_STOCK_JOURS = 30    # Jours minimum de stock

# Liste des 12 départements de la République du Congo
DEPARTEMENTS_CONGO = [
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# =====================================================================
# SECTION B : VARIABLES DES 5 HÔPITAUX
#QUI SERONT ABREGER SUIVANT CETTE LOGIQUE: h1;h2,h3,4 et h5
# =====================================================================

# --- Hôpital 1 : CHU de Brazzaville (Données réelles du support)
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits_total = 320
h1_nb_lits_occupes = 284
h1_nb_medecins_actifs = 47
h1_nb_infirmiers = 123

# --- Hôpital 2 : Hôpital Général de Pointe-Noire (Anticipation / Exercice 2)
h2_nom = "Hôpital Général de Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Kouilou"
h2_type = "Hôpital Général"
h2_nb_lits_total = 180
h2_nb_lits_occupes = 143
h2_nb_medecins_actifs = 22
h2_nb_infirmiers = 58

# --- Hôpital 3 : Hôpital de Dolisie (Anticipation)
h3_nom = "Hôpital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hôpital Général"
h3_nb_lits_total = 120
h3_nb_lits_occupes = 85
h3_nb_medecins_actifs = 12
h3_nb_infirmiers = 34

# --- Hôpital 4 : Hôpital de district Owando (Anticipation)
h4_nom = "Hôpital de district d'Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "Hôpital de District"
h4_nb_lits_total = 80
h4_nb_lits_occupes = 45
h4_nb_medecins_actifs = 5
h4_nb_infirmiers = 18

# --- Hôpital 5 : Centre de santé de Impfondo (Anticipation)
h5_nom = "Centre de santé d'Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de Santé"
h5_nb_lits_total = 40
h5_nb_lits_occupes = 32
h5_nb_medecins_actifs = 2
h5_nb_infirmiers = 10

# =====================================================================
# SECTION C : VARIABLES DES 5 MÉDICAMENTS ESSENTIELS (Anticipation)
# =====================================================================

# Médicament 1 : Artéméther-Luméfantrine (Antipaludéen)
m1_nom = "Artéméther-Luméfantrine"
m1_quantite_dispo = 8450
m1_seuil_rupture = 2000
m1_prix_unitaire_fcfa = 3500.0

# Médicament 2 : Amoxicilline 500mg (Antibiotique)
m2_nom = "Amoxicilline 500mg"
m2_quantite_dispo = 3200
m2_seuil_rupture = 800
m2_prix_unitaire_fcfa = 850.0

# Médicament 3 : Paracétamol
m3_nom = "Paracétamol"
m3_quantite_dispo = 12000
m3_seuil_rupture = 3000
m3_prix_unitaire_fcfa = 200.0

# =====================================================================
# SECTION D : CALCULS STATISTIQUES ET FINANCIERS AVANCÉS (Semaine 2)
# =====================================================================

# 1. Calcul des valeurs financières de stock pour chaque médicament
valeur_m1 = m1_quantite_dispo * m1_prix_unitaire_fcfa
valeur_m2 = m2_quantite_dispo * m2_prix_unitaire_fcfa
valeur_m3 = m3_quantite_dispo * m3_prix_unitaire_fcfa

# 2. Valeur totale de l'ensemble du stock de la pharmacie
valeur_totale_stock = valeur_m1 + valeur_m2 + valeur_m3

# 3. Calcul du prix moyen d'un médicament dans le catalogue (arrondi à 2 décimales)
prix_moyen_medicament = round((m1_prix_unitaire_fcfa + m2_prix_unitaire_fcfa + m3_prix_unitaire_fcfa) / 3, 2)

# 4. Calcul du volume total de boîtes de médicaments en stock
volume_total_boites = m1_quantite_dispo + m2_quantite_dispo + m3_quantite_dispo

# 5. Calcul du seuil de sécurité global (somme des seuils de rupture)
seuil_securite_total = m1_seuil_rupture + m2_seuil_rupture + m3_seuil_rupture

# 6. Marge de sécurité (De combien de boîtes dépassons-nous le seuil critique ?)
marge_securite_boites = volume_total_boites - seuil_securite_total

# 7. Calculs hospitaliers (Taux d'occupation des lits pour le CHU de Brazzaville)
taux_occupation_h1 = round((h1_nb_lits_occupes / h1_nb_lits_total) * 100, 1)


# =====================================================================
# SECTION E : AFFICHAGE DU RAPPORT DU MINISTÈRE DE LA SANTÉ
# =====================================================================
print("=" * 65)
print("   MINISTÈRE DE LA SANTÉ - EXERCICE DE SIMULATION ANALYTIQUE S2   ")
print("=" * 65)

print(f"Structure analysée : {h1_nom} ({h1_ville})")
print(f" -> Taux d'occupation des lits : {taux_occupation_h1}%")
print(f" -> Personnel disponible       : {h1_nb_medecins_actifs} médecins / {h1_nb_infirmiers} infirmiers")

print("-" * 65)
print("             RAPPORT FINANCIER & LOGISTIQUE PHARMACIE          ")
print("-" * 65)
print(f"Valeur Stock {m1_nom} : {valeur_m1:,} FCFA")
print(f"Valeur Stock {m2_nom} : {valeur_m2:,} FCFA")
print(f"Valeur Stock {m3_nom} : {valeur_m3:,} FCFA")
print(f"--> VALEUR TOTALE DU STOCK EN PHARMACIE : {valeur_totale_stock:,} FCFA")

print("-" * 65)
print("                     INDICATEURS CLÉS (KPIs)                   ")
print("-" * 65)
print(f" -> Prix moyen d'un médicament en catalogue : {prix_moyen_medicament} FCFA")
print(f" -> Volume total de médicaments en stock    : {volume_total_boites:,} boîtes")
print(f" -> Marge de sécurité avant alerte globale  : {marge_securite_boites:,} boîtes")
print("=" * 65)

