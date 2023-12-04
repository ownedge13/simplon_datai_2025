import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_20newsgroups

st.title('Application de visualisation de données en temps réel')

# Récupérez les données à partir du serveur Flask (en utilisant un extrait du dataset 20 Newsgroups)
response = requests.get('http://localhost:5000/api/data')
data = response.json()

# Créez un DataFrame pandas pour une meilleure manipulation des données
df = pd.DataFrame(data, columns=['Text', 'Category'])

# Affichez les données brutes si l'utilisateur le souhaite
if st.checkbox('Afficher les données brutes'):
    st.write(df)

# Ajoutez un filtre pour sélectionner des catégories de newsgroups
newsgroups = fetch_20newsgroups(subset='all')
categories = newsgroups.target_names
selected_categories = st.multiselect('Sélectionnez des catégories de newsgroups', categories)
if selected_categories:
    filtered_data = df[df['Category'].isin(selected_categories)]
else:
    filtered_data = df

# Affichez les statistiques descriptives
st.subheader('Statistiques descriptives')
st.write(filtered_data.describe())

# Créez un histogramme pour la distribution des données
st.subheader('Histogramme de la longueur des textes')
plt.hist(filtered_data['Text'].str.len(), bins=50, color='skyblue')
st.pyplot(plt)

# Créez un graphique à barres pour compter les articles par catégorie de newsgroup
st.subheader('Nombre d\'articles par catégorie de newsgroup')
category_counts = filtered_data['Category'].value_counts()
st.bar_chart(category_counts)

# Vous pouvez ajouter d'autres graphiques, des statistiques et des fonctionnalités en fonction de vos besoins
