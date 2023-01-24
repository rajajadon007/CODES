import streamlit as st
import pdfplumber
import pandas as pd


with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    text = ""
  
    for page in pdf.pages:
        text += page.extract_text()


df = pd.DataFrame({'text':text.split("\n")})
st.dataframe(df,width=800)
df_cols = df[["text"]]
df_json = df_cols.to_json(orient='index')
st.write(df_json)

