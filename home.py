import streamlit as st
from PIL import Image

def app():
    st.subheader(""" A simple web-based calculator """)
    image = Image.open('images.jpg')
    st.image(image)
    