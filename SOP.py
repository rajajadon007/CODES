import streamlit as st
import json
import pdfplumber
from pandas.io.json import json_normalize

with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    text = ""
    pages = []
    for i, page in enumerate(pdf.pages):
        text += page.extract_text()
        pages.append({'page_number': i+1, 'text': text})
    df = json_normalize(pages)
    df.set_index('page_number', inplace=True)
    st.write(df, height =1000,width=1000)


       

