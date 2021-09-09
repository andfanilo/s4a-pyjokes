import pyjokes
import streamlit as st

with st.sidebar:
    selected_categoty = st.selectbox("Joke Category", ("all", "chuck"))

st.title(":joy: Random Joke app")

if st.button("Random joke!"):
    st.info(pyjokes.get_joke())
