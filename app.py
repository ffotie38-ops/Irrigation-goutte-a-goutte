import streamlit as st

st.set_page_config(page_title="Calculateur d'Irrigation Gotaboot", page_icon="🌱", layout="centered")

st.title("🌱 Calculateur d'Irrigation Goutte-à-Goutte")
st.write("Application de gestion et de calcul du temps d'arrosage pour le système Gotaboot.")

st.sidebar.header("Paramètres de la Parcelle")

culture = st.sidebar.text_input("Nom de la culture", value="Tomate")
surface_m2 = st.sidebar.number_input("Surface de la parcelle (en m²)", min_value=1.0, value=100.0)
et0 = st.sidebar.number_input("Évapotranspiration (ET0 en mm/jour)", min_value=0.1, value=4.5)
kc = st.sidebar.number_input("Coefficient cultural (Kc)", min_value=0.1, value=1.15)
debit_goutteur = st.sidebar.number_input("Débit d'un goutteur Gotaboot (L/h)", min_value=0.1, value=2.0)
nb_goutteurs = st.sidebar.number_input("Nombre total de goutteurs", min_value=1, value=200)

if st.button("Calculer l'irrigation", type="primary"):
    etc = et0 * kc
    volume_total_litres = etc * surface_m2
    debit_total = debit_goutteur * nb_goutteurs
    
    if debit_total > 0:
        temps_arrosage_heures = volume_total_litres / debit_total
        temps_arrosage_minutes = temps_arrosage_heures * 60
    else:
        temps_arrosage_minutes = 0
        
    st.success(f"### Rapport d'irrigation pour : {culture.upper()}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Besoin journalier (ETc)", value=f"{etc:.2f} mm/j")
        st.metric(label="Volume d'eau total", value=f"{volume_total_litres:.1f} Litres")
    with col2:
        st.metric(label="Débit total du système", value=f"{debit_total:.1f} L/h")
        st.metric(label="⏱️ Temps d'arrosage", value=f"{temps_arrosage_minutes:.1f} min")
        
    st.info("💡 Conseil : Ajustez les paramètres dans le menu à gauche pour recalculer instantanément.")
