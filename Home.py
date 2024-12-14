import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.image("images/20241030_115331.png", width=200)

with col2:
    st.title("Paul Grant")
    portfolio_description = '''A Data Scientist in training. Leveraging Python to 
    explore data-driven insights and build innovative solutions.'''
    st.info(portfolio_description)


st.write("Below you can find some of the apps I have built in Python. "
         "Feel free to contact me!")

df = pd.read_csv("data.csv", sep=";")

col4, col5 = st.columns(2)

with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
