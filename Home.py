import streamlit as st

st.set_page_config("UX Scores", initial_sidebar_state="collapsed")
st.title("UX Scores")

st.write("Welcome! Select a questionnaire to start calculating UX scores.")

if st.button("System Usability Scale (SUS)", icon=":material/arrow_forward:", width="stretch"):
    st.switch_page("pages/01_SUS.py")
if st.button("UMUX-Lite", icon=":material/arrow_forward:", width="stretch"):
    st.switch_page("pages/02_UMUX-Lite.py")
if st.button("UEQ-S", icon=":material/arrow_forward:", width="stretch"):
    st.switch_page("pages/03_UEQ-S.py")
