import socket
import streamlit as st
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        st.write("Error: ", e)
        return None

ip_address = get_ip_address()
if ip_address:
    st.write("IP Address: ", ip_address)
else:
    st.write("Failed to retrieve IP address")
