import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(
    page_title = 'Home',
    page_icon = ':)',
    layout = 'wide'
    )

st.title ('Hello World!')
df = pd.read_csv('startup_funding2018.csv')
st.dataframe(df)

data = pd.DataFrame(
    np.random.randn(20,3),
                     columns = ['Company_Name', 'Amount', 'Round/Series']
                     )


st.bar_chart(data)
st.line_chart(data)


