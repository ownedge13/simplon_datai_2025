import streamlit as st
import requests
import pandas as pd

st.title('Application de Visualisation de Données')

# Récupérez les données à partir du serveur Flask
response = requests.get('http://localhost:5000/api/actors')  # Utilisez l'URL correcte pour accéder à vos données
data = response.json()

# Créez un DataFrame pandas à partir des données
df = pd.DataFrame(data)

# Affichez les données dans Streamlit
st.dataframe(df)

# Vous pouvez maintenant ajouter d'autres éléments d'interface utilisateur, des graphiques, des filtres, etc.
