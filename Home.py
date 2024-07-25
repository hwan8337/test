import streamlit as st

if st.button("Home"):
    st.switch_page("Home.py")
if st.button("Page 1"):
    st.switch_page("./pages/page1.py")
if st.button("Page 2"):
    st.switch_page("./pages/page2.py")