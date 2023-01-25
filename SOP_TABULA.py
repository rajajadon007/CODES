from docx import Document
import pandas as pd
import streamlit as st


document = Document('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.docx')
for table in document.tables:
    data = []
    keys = None
    for i, row in enumerate(table.rows):
        text = (cell.text for cell in row.cells)
        if i == 0:
            keys = tuple(text)
            continue
        row_data = dict(zip(keys, text))
        data.append(row_data)
    df = pd.DataFrame(data)
    st.write(df, height=1000, width=1000)
