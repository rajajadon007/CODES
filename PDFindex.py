import streamlit as st
import pdfplumber
import pandas as pd
with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    df_list = []
    for page in pdf.pages:
           df_list.append(page.extract_table())
        if table:   
            df = pd.DataFrame(table[1:], columns=table[0])
            df.index+=1
            df_list.append(df)
   
    final_df = pd.concat(df_list, ignore_index=True)
   
    st.dataframe(final_df)
