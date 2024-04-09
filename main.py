import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1h3YyXq6n-_-2I_N7DuvdD-srgeMDPD5zINgbi5rGseU/edit#gid=0"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)

url = "https://docs.google.com/spreadsheets/d/1h3YyXq6n-_-2I_N7DuvdD-srgeMDPD5zINgbi5rGseU/edit#gid=0"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
