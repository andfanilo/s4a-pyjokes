import pyjokes
import streamlit as st

with st.sidebar:
    selected_lang = st.selectbox("Select language", ("en", "de", "es", "gl", "eus"))
    selected_categoty = st.selectbox("Joke Category", ("all", "neutral", "chuck"))

st.title(":joy: Random Joke app")

if st.button("Random joke!"):
    st.info(pyjokes.get_joke())
