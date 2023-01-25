import streamlit
import tabula
import json

df = tabula.read_pdf("SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf", pages="2")
json_data = df.to_json(orient='records')
st.write(json_data)
