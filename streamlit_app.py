import streamlit as st

password = st.text_input("password")

st.help(st.text_input)

if password == "123":
  st.balloons()
  st.success("You got in!")
else:
  st.error("Incorrect")
