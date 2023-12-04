import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Lecture et Affichage de Données depuis Différents Fichiers")

# Menu déroulant pour sélectionner l'onglet
onglet_selectionne = st.sidebar.radio("Sélectionnez un onglet", ["Fichier CSV", "Fichier Excel", "Fichier JSON"])

# Gestion de l'onglet "Fichier CSV"
if onglet_selectionne == "Fichier CSV":
    st.header("Lecture de données depuis un fichier CSV")
    fichier_csv = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

    if fichier_csv is not None:
        data = pd.read_csv(fichier_csv)
        st.dataframe(data)

# Gestion de l'onglet "Fichier Excel"
if onglet_selectionne == "Fichier Excel":
    st.header("Lecture de données depuis un fichier Excel")
    fichier_excel = st.file_uploader("Téléchargez un fichier Excel", type=["xls", "xlsx"])

    if fichier_excel is not None:
        data = pd.read_excel(fichier_excel)
        st.dataframe(data)

# Gestion de l'onglet "Fichier JSON"
if onglet_selectionne == "Fichier JSON":
    st.header("Lecture de données depuis un fichier JSON")
    fichier_json = st.file_uploader("Téléchargez un fichier JSON", type=["json"])

    if fichier_json is not None:
        data = pd.read_json(fichier_json)
        st.dataframe(data)