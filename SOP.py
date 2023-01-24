import streamlit as st
import json

with open('export.json') as f:
    data = json.load(f)
    
st.write(data)
