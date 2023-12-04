import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# Fonction pour l'onglet "Graphique à Barres"
def onglet_graphique_barres():
    st.header("Graphique à barres interactif")
    # Créez des données pour le graphique à barres
    categories = ['A', 'B', 'C', 'D', 'E']
    valeurs = [5, 10, 8, 12, 6]

    # Créez un graphique à barres interactif
    fig, ax = plt.subplots()
    ax.bar(categories, valeurs)
    st.pyplot(fig)

# Fonction pour l'onglet "Graphique Circulaire"
def onglet_graphique_circulaire():
    st.header("Graphique circulaire interactif")
    # Créez des données pour le graphique circulaire
    donnees = {'Labels': ['A', 'B', 'C', 'D', 'E'],
               'Valeurs': [25, 20, 15, 10, 30]}

    # Créez un graphique circulaire interactif
    fig = px.pie(donnees, names='Labels', values='Valeurs')
    st.plotly_chart(fig)

# Liste des noms d'onglets
onglets = ["Graphique à Barres", "Graphique Circulaire"]

# Permettez à l'utilisateur de sélectionner un onglet
selection = st.selectbox("Sélectionnez un onglet", onglets)

# Utilisez des structures conditionnelles pour afficher le contenu de l'onglet sélectionné
if selection == "Graphique à Barres":
    onglet_graphique_barres()
else:
    onglet_graphique_circulaire()