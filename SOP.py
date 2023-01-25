import streamlit as st
import json
import pdfplumber
from pandas.io.json import json_normalize
import pandas as pd

import streamlit as st

with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    pages = []
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        pages.append({'page_number': i+1, 'text': text})
    df = pd.DataFrame(pages)
    df.set_index('page_number', inplace=True)
    st.write(df, height =1000,width=1000)

search_term = st.text_input("Enter a value from column 2:")
if search_term:
    result = df.query("column_2 == @search_term")
    if result.empty:
        st.warning("No match found.")
    else:
        st.write("The corresponding value in column 6 is:", result['column_6'].values[0])



