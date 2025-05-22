# 1. Ingresar la cantidad en dolares
# 2. Realizar la formula para convertir a euros
# 3. Imprimir el resultado en la consola

import streamlit as st

st.title('Conversión de Dolares a Euros')

dolares = st.number_input('Introduce la cantidad de dolares')

euros = float(dolares) * 1.13455

st.button('Procesar', on_click=print(f'{dolares} Dolares son: {euros} Euros'))

