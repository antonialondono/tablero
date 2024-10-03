import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Tablero', layout='wide')
st.title('Deja volar tu imaginación')


drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.colorpicker ('Selecciona el color')# Set background color to white
bg_color = '#000000'

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)

