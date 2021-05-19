import streamlit as st
from multiapp import MultiApp
from apps import home, Addition, Subtraction, Multiply, Division, Mod # import your app modules here

app = MultiApp()

st.markdown(""" # Simple Calculator """)

st.text("Use The Drop Down Menu Below To Navigate Between Homepage & Calculator.")

# Add all your application here

app.add_app("Home", home.app)
app.add_app("Calculator for Addition", Addition.app)
app.add_app("Calculator for Subtraction", Subtraction.app)
app.add_app("Calculator for Multiplication", Multiply.app)
app.add_app("Calculator for Division", Division.app)
app.add_app("Calculator for Modulus", Mod.app)

# The main app
app.run()