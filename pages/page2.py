import streamlit as st
st.image("images/10003.jpg")
text = st.text_input("입력")
if st.button("save"):
    st.session_state.text = text