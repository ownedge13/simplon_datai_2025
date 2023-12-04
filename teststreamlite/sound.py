import streamlit as st
import numpy as np
st.title("Signal Sinusoïdal en fonction de la Fréquence")
freq = st.slider("Sélectionnez la fréquence (en Hz)", 1, 44000, 1)
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * freq * t)
st.line_chart(signal)