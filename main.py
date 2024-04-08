import os
import streamlit as st
def get_device_name():
    try:
        device_name = os.getenv('COMPUTERNAME')
        return device_name
    except Exception as e:
        st.write("Error: ", e)
        return None

device_name = get_device_name()
if device_name:
    st.write("Device Name: ", device_name)
else:
    st.write("Failed to retrieve device name")
