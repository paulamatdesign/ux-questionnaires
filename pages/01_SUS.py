import streamlit as st
import pandas as pd
import openpyxl as pxl
#from plotnine import ggplot, aes, geom_col, labs

st.title("SUS Score Calculator")

# Chargement du fichier
uploaded_file = st.file_uploader("Choisir un fichier Excel", type=["xlsx", "xls"], label_visibility="collapsed")

if uploaded_file is not None:

    # Lecture des données
    df_raw = pd.read_excel(uploaded_file)

    df_processed = df_raw.copy()

    # Apply SUS scoring rules
    for i, col in enumerate(df_processed.columns, start=1):
        if i % 2 == 1:  
            # Odd-numbered items
            df_processed[col] = df_processed[col] - 1
        else:           
            # Even-numbered items
            df_processed[col] = 5 - df_processed[col]

    # Sum across the 10 items
    df_processed["User score"] = df_processed.sum(axis=1) * 2.5
    col = df_processed.pop("User score")   # remove the column
    df_processed.insert(0, "User score", col)  # reinsert at position 0

    score = df_processed["User score"].mean()

    tab1, tab2, tab3 = st.tabs(["SUS Score", "Processed Data", "Raw Data"], )

    with tab1:
        st.metric("Score", score, border=True)

    with tab2:
        st.write(df_processed)

    with tab3:
        st.write(df_raw)

    #     p = (
    #         ggplot(plot_df, aes(x="colonne", y="moyenne")) +
    #         geom_col() +
    #         labs(title="Moyenne de la colonne", x="", y="Moyenne")
    #     )

    #     st.pyplot(p.draw())
