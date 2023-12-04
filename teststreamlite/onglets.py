import streamlit as st

# Créez trois sections distinctes pour chaque onglet
def onglet1():
    st.header("Onglet 1")
    st.write("Contenu de l'onglet 1")

def onglet2():
    st.header("Onglet 2")
    st.write("Contenu de l'onglet 2")

def onglet3():
    st.header("Onglet 3")
    st.write("Contenu de l'onglet 3")

# Liste des noms d'onglets
onglets = ["Onglet 1", "Onglet 2", "Onglet 3"]

# Permettez à l'utilisateur de sélectionner un onglet
selection = st.selectbox("Sélectionnez un onglet", onglets)

# Utilisez des structures conditionnelles pour afficher le contenu de l'onglet sélectionné
if selection == "Onglet 1":
    onglet1()
elif selection == "Onglet 2":
    onglet2()
else:
    onglet3()