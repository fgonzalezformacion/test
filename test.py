
while True:
    try:
        num1 = int(st.input("Ingresa el primer número: "))
        num2 = int(st.input("Ingresa el segundo número: "))
        resultado = num1 + num2
        st.print("La suma es:", resultado)
        break
    except ValueError:
        st.print("ese número no es válido, por favor ingresa un entero")
