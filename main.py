import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1h3YyXq6n-_-2I_N7DuvdD-srgeMDPD5zINgbi5rGseU/edit#gid=0"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1])


editable_df = st.dataframe(data, editable=True)

# Update the Google Sheet with the edited DataFrame
if st.button("Update Google Sheet"):
    conn.write(editable_df, worksheet="YOUR_WORKSHEET_NAME_HERE")

# Display the updated DataFrame
st.dataframe(editable_df)
