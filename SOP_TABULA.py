import streamlit as st
import json

df = tabula.read_pdf(
    "SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf", stream=False, pages='all')
st.dataframe(df)


st.write(df)
