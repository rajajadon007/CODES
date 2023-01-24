import streamlit as st
import pdfplumber
import pandas as pd


with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    text = ""
    
    for page in pdf.pages:
        text += page.extract_text()
    # Write the extracted text to a CSV file
    with open('your_pdf_text.csv', 'w') as f:
        f.write(text)
file_upload = st.file_uploader("Upload your CSV file", type=["csv"])

if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.dataframe(df)
