import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/20241030_115331.png")

with col2:
    st.title("Paul Grant")
    portfolio_description = '''A Data Scientist in Training. Leveraging Python to 
    explore data-driven insights and build innovative solutions.'''
    st.info(portfolio_description)


st.write("Below you can find some of the apps I have built in Python. "
         "Feel free to contact me!")
