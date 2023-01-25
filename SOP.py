import streamlit as st
import json
import pdfplumber
from pandas.io.json import json_normalize

with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    text = ""
  
    for page in pdf.pages:
        text += page.extract_text()

    data = {'text': text}
    df = json_normalize(data)
    st.write(df['Input: Periodic Event  6' ])
    st.write(df)
       

