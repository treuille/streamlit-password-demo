import streamlit as st

password = st.text_input("password", type="password")

password = os.environ("path")

if password == password:
  st.balloons()
  st.success("You got in!")
else:
  st.error("Incorrect")
