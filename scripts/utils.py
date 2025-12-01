import streamlit as st

def header():
    st.html(
        """
            <style>
                h2 {
                    margin-top: 1.5rem;
                    font-weight: 400 !important;
                    opacity: 0.6 !important;
                    font-size: medium !important;
                    text-transform: uppercase;
                    letter-spacing: normal !important;
                }
        """
    )
    if st.button("Home", icon=":material/arrow_back:", type="tertiary"):
        st.switch_page("Home.py")