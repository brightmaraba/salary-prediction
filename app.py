import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Select To Predict or Explore the Data", ("Predict", "Explore"))
st.sidebar.image("Motivation.png", use_column_width=True)


if page == 'Predict':
    show_predict_page() # show the predict page
else:
    show_explore_page()
