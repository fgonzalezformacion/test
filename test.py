
import streamlit as st
while True:
    try:
        num1 = st.int(input("Ingresa el primer número: "))
        num2 = st.int(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print("La suma es:", resultado)
        break
    except ValueError:
        print("ese número no es válido, por favor ingresa un entero")
