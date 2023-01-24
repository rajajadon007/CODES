import json
import pdfplumber


with pdfplumber.open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf') as pdf:
    text = ""
  
    for page in pdf.pages:
        text += page.extract_text()
   
    data = {'text': text}
    with open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.json', 'w') as json_file:
        json.dump(data, json_file)
        st.write(data)


