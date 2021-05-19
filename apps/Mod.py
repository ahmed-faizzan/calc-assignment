import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():

    a = st.number_input("Please enter First Number")
    b = st.number_input("Please enter Second Number")
    c = a%b
    st.text("The Modulus is")
    st.write(c)