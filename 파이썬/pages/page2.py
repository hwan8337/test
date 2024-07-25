import streamlit as st
text = st.text_input("입력")
if st.button("save"):
    st.session_state.text = text