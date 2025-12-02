import streamlit as st
import numpy as np
from scipy import stats

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

def ci(x):
    sd = x.std(ddof=1)
    n = len(x)
    se = sd / np.sqrt(n)
    dfree = n - 1
    t_crit = stats.t.ppf(1 - 0.05/2, dfree)
    errormargin = t_crit * se
    ci_low = x.mean() - errormargin
    ci_high = x.mean() + errormargin
    return [ci_low, ci_high]

def sus_as_grade(s):
        if s <= 60:
            return "F"
        elif s <= 70:
            return "D"
        elif s <= 80:
            return "C"
        elif s <= 90:
            return "B"
        else:
            return "A"

def sus_as_acceptability(s):

    if s <= 50:
        return "NAC"   # Not Acceptable
    elif s <= 62:
        return "MAL"   # Marginal Low
    elif s <= 70:
        return "MAH"   # Marginal High
    else:
        return "ACP"   # Acceptable
