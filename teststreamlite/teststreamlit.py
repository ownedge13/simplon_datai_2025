import streamlit as st
st.title ("Tableau de Bord Simple")

if st.button ("Cliquez-moi"):
    st.write ("Vous avez cliqué sur le bouton !")

âge = st.slider ("age", 0, 100, 25)

st.write (f"Vous avez {âge} ans")

nom = st.text_input("Entrez votre nom")
if nom:
    st.write(f"Bonjour, {nom} !")

details = st.checkbox("Montrez les détails")
if details:
    st.write("Les détails sont affichés")

import sounddevice as sd
import numpy as np 

def sinusoids(a,f,Fs,T,phase):


    t = np.arange(0,Fs*T) # pour une seconde
    s = 0 
    for i,freq in enumerate(f):

        s += a[i] * np.sin(2*np.pi*freq*t/Fs + 2*np.pi/360*phase[i])
    return s

N = 1
a = np.random.rand(N)
f = np.random.rand(N)*256
phase = np.random.randn(N)*360
Fs = 44100 
T = 2

a[0] = 1
f[0] = 440

x = sinusoids(a,f,Fs,T,phase)

x = x/np.abs(x).max() 
sd.play(x,Fs)