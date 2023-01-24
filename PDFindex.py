import streamlit as st
import pdfplumber
import pandas as pd


with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    text = ""
  
    for page in pdf.pages:
        text += page.extract_text()


df = pd.DataFrame({'text':text.split("\n")})
df.to_csv('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.csv', index=False)
st.write("Here is the extracted text from the pdf:")
st.dataframe(df,width=800)
st.markdown("You can download the csv file by clicking the following button:")
download_button = st.button('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.csv')
if download_button:
    st.write("The extracted text is downloaded as csv file!")
    st.markdown("Please find the downloaded csv file.")
