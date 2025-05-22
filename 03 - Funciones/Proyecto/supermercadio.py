import streamlit as st
import pandas as pd

if 'table_data' not in st.session_state:
    st.session_state.table_data = pd.DataFrame(columns=['Producto', 'Precio', 'Cantidad', 'Subtotal'])

st.title('Supermercado')

with st.form('producto_form'):
    producto_nombre = st.text_input('Introduce el nombre del producto')
    producto_precio = st.number_input('Introduce el precio del producto')
    producto_cantidad = st.number_input('Introduce la cantidad de producto')

    subtotal_boton = st.form_submit_button('Comprar Producto')
