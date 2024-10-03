import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Tablero', layout='wide')
st.title('Dibujo libre!!!')
st.subheader("Deja volar tu imaginación")


drawing_mode = st.sidebar.selectbox(
    "Selecciona el modo de dibujo",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
)
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.sidebar.color_picker ('Selecciona el color del trazo')# Set background color to white
bg_color = st.sidebar.color_picker ('Selecciona el color del fondo')

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=400,
    key="canvas",
    drawing_mode = drawing_mode
)

