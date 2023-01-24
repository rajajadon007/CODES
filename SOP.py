import streamlit as st

with open('export.json') as f:
    data = json.load(f)
    
st.write(data)
