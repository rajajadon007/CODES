import streamlit as st
import pdfplumber
import pandas as pd

# Open the PDF file
with pdfplumber.open('your_pdf_file.pdf') as pdf:
    text = ""
    # Extract text from all pages
    for page in pdf.pages:
        text += page.extract_text()

# convert text into DataFrame
df = pd.DataFrame({'text':text.split("\n")})

# Write the DataFrame to a CSV file
df.to_csv('your_pdf_text.csv', index=False)

# Allow the user to download the CSV file
st.write("Here is the extracted text from the pdf:")
st.dataframe(df)
st.markdown("You can download the csv file by clicking the following button:")
download_button = st.button('Download CSV')
if download_button:
    st.write("The extracted text is downloaded as csv file!")
    st.markdown("Please find the downloaded csv file.")
