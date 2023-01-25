import streamlit
import tabula
import json


df = tabula.read_pdf("example.pdf", pages="all")


json_data = df.to_json(orient='records')


st.write(json_data)
