import streamlit as st
import pdfplumber
import pandas as pd
with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    table_list = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            table_list.append(table)
   
    final_df = pd.concat(table_list, ignore_index=True,join='outer')
   
    st.dataframe(final_df)
