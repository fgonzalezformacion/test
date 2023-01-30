
import streamlit as st

st.title("Sumador de números")

num1 = st.number_input("Introduce el primer número:")
num2 = st.number_input("Introduce el segundo número:")

result = num1 + num2

st.write("El resultado de la suma es:", result)
