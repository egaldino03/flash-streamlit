import streamlit as st
import pandas as pd

st.set_page_config(page_title='finance-app', page_icon='💰')

st.markdown('''
# Boas vindas!
            
## Nosso app financeiro!
            
Espero que curta a experiência da nossa solução para organização financeira.
''')

file_upload = st.file_uploader(label='Faça o upload dos dados aqui', type=['csv'])

if file_upload:
    df = pd.read_csv(file_upload)

    columns_fmt = {'Valor': st.column_config.NumberColumn('Valor', format='R$ %.2f') }
    st.dataframe(df, hide_index=True, column_config=columns_fmt)