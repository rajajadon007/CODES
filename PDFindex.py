import streamlit as st
import pdfplumber
import pandas as pd
with pdfplumber.open('y.pdf') as pdf:
    df_list = []
    for page in pdf.pages:
        df_list.append(page.extract_table())
    df = pd.concat(df_list, ignore_index=True)
    df.index+=1
    st.dataframe(df)
