import streamlit as st
from pymongo import MongoClient

st.title("Connexion à une Base de Données NoSQL (MongoDB)")

client = MongoClient("mongodb://mongoscooby.ownedge.fr:27017/")
db = client.ma_base_de_donnees
collection = db.utilisateurs

st.subheader("Ajouter un Nouvel Utilisateur")
nom_utilisateur = st.text_input("Nom de l'utilisateur")
email_utilisateur = st.text_input("Email de l'utilisateur")
if st.button("Ajouter"):
    if nom_utilisateur and email_utilisateur:
        nouvel_utilisateur = {
            "nom": nom_utilisateur,
            "email": email_utilisateur
        }
        collection.insert_one(nouvel_utilisateur)
        st.success(f"Utilisateur '{nom_utilisateur}' ajouté avec succès !")
    else:
        st.warning("Veuillez remplir tous les champs.")

st.subheader("Utilisateurs Existants")
utilisateurs = collection.find()
for utilisateur in utilisateurs:
    st.write(f"Nom: {utilisateur['nom']}, Email: {utilisateur['email']}")

client.close()