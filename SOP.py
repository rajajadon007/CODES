import streamlit as st
import json
import pdfplumber
from pandas.io.json import json_normalize
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    pages = []
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        pages.append({'page_number': i+1, 'text': text})
    df = pd.DataFrame(pages)
    if 'page_number' not in df.columns:
        df['page_number'] = df.index
    if df.index.name != 'page_number':
        df.set_index('page_number', inplace=True)
    st.write(df, height =1000,width=1000)
    search_term = st.text_input("Enter a search term:")
    if search_term:
        search_result = df[df['text'].str.contains(search_term, case=False)]
        st.write("Results for search term '{}':".format(search_term))
        st.write(search_result, height =1000,width=1000)
       
