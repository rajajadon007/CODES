import json
import PyPDF2
with open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
   
    text = ''
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()
 
    data = {'text': text}
    st.write(data)
