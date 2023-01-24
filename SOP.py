import json
import PyPDF2
with open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
   
    text = ''
    for page in range(pdf_reader.pages):
        text += pdf_reader.getPage(page).extractText()
 
    data = {'text': text}
    with open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf.json', 'w') as json_file:
       json.dump(data, json_file)
