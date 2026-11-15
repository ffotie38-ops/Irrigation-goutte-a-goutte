# --- APPLICATION DE CALCUL D'IRRIGATION (VERSION JUPYTER) ---

print("=== CALCULATEUR D'IRRIGATION GOUTTE-À-GOUTTE ==_\n")

# Saisie des données via des champs interactifs dans Jupyter
culture = input("1. Nom de la culture (ex: Tomate, Poivron) : ")
surface_m2 = float(input("2. Surface de la parcelle (en m²) : "))
et0 = float(input("3. Évapotranspiration de référence (ET0 en mm/jour, ex: 4.5) : "))
kc = float(input("4. Coefficient cultural de la plante (Kc, ex: 1.15) : "))
debit_goutteur = float(input("5. Débit d'un goutteur Gotaboot (en L/h, ex: 2.0) : "))
nb_goutteurs = int(input("6. Nombre total de goutteurs sur la parcelle : "))

# Moteur de calcul agronomique
etc = et0 * kc
volume_total_litres = etc * surface_m2
debit_total = debit_goutteur * nb_goutteurs

if debit_total > 0:
    temps_arrosage_heures = volume_total_litres / debit_total
    temps_arrosage_minutes = temps_arrosage_heures * 60
else:
    temps_arrosage_minutes = 0

# Affichage propre des résultats dans Jupyter
print("\n" + "="*45)
print(f"       RAPPORT D'IRRIGATION : {culture.upper()}")
print("="*45)
print(f"• Besoin journalier de la culture (ETc) : {etc:.2f} mm/jour")
print(f"• Volume d'eau total nécessaire : {volume_total_litres:.2f} Litres/jour")
print(f"• Débit total du système Gotaboot : {debit_total:.2f} L/h")
print(f"⏱️  TEMPS D'ARROSAGE RECOMMANDÉ : {temps_arrosage_minutes:.1f} minutes par jour")
print("="*45)
