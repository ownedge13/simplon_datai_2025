import streamlit as st
import mysql.connector

# Titre de l'application
st.title("Connexion à une Base de Données SQL (MySQL/MariaDB)")

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='root',
    database='ma_base_de_donnees',
    auth_plugin='caching_sha2_password'
)

cursor = conn.cursor()

# Création de la Table (si elle n'existe pas)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        email VARCHAR(255)
    )
''')
conn.commit()

# Formulaire pour ajouter un nouvel utilisateur
st.subheader("Ajouter un Nouvel Utilisateur")
nom_utilisateur = st.text_input("Nom de l'utilisateur")
email_utilisateur = st.text_input("Email de l'utilisateur")
if st.button("Ajouter"):
    if nom_utilisateur and email_utilisateur:
        cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)", (nom_utilisateur, email_utilisateur))
        conn.commit()
        st.success(f"Utilisateur '{nom_utilisateur}' ajouté avec succès !")
    else:
        st.warning("Veuillez remplir tous les champs.")

# Affichage des Utilisateurs Existants
st.subheader("Utilisateurs Existants")
cursor.execute("SELECT * FROM utilisateurs")
utilisateurs = cursor.fetchall()
for utilisateur in utilisateurs:
    st.write(f"Nom: {utilisateur[1]}, Email: {utilisateur[2]}")

# Fermeture de la connexion à la base de données
conn.close()
