import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/20241030_115331.png")

with col2:
    st.title("Paul Grant")
    content = '''A Data Scientist in Training. Leveraging Python to 
    explore data-driven insights and build innovative solutions.'''
    st.info(content)
