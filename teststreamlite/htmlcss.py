import streamlit as st

# Personnalisation du bouton avec du HTML et CSS
button_html = """
    <style>
        .custom-button {
            background-color: green;
            color: white;
            border: 1px solid black;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
    <a href="#" class="custom-button" id="custom-button">Cliquez-moi</a>
"""

# Afficher le code HTML avec unsafe_allow_html=True
st.markdown(button_html, unsafe_allow_html=True)

# Vérifier si le bouton a été cliqué
if st.button("Cliquez-moi"):
    st.write("Vous avez cliqué sur le bouton !")