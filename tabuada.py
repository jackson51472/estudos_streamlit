import streamlit as st
import pandas as pd

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

dark_mode = st.sidebar.toggle("Modo escuro", value=st.session_state.dark_mode)

st.session_state.dark_mode = dark_mode

if dark_mode:
    custom_css = '''
    <style>
    .stApp {
      background-color: #343434;
    }

    .stApp, .stMarkdown, .stText, p, div {
      color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6 {
      color: #ffffff !important;
    }

    .stSlider, .stCheckbox, .stRadio label {
      color: #ffffff !important;
    }

    .element-container div {
      color: #ffffff !important;
    }

    [data-testid="stSidebar"] {
        background-color: #848484 !important;
    }
    </style>
    '''
else:
    custom_css = '''
    <style>
    </style>
    '''

st.title("Tabuada em Streamlit")
st.markdown(custom_css, unsafe_allow_html=True)

numero = st.select_slider("Selecione um número que você deseja a tabuada", options=range(1, 101), value=10)
linhas = st.select_slider("Selecione até qual número você deseja saber a tabuada", options=range(1, 101), value=10)

st.write(pd.DataFrame({
    'Soma': [f'{numero} + {i} = {numero + (i)}' for i in range(linhas)],
    'Subtração': [f'{numero} - {i} = {numero - (i)}' for i in range(linhas)],
    'Multiplicação': [f'{numero} x {i} = {numero * (i)}' for i in range(linhas)],
    'Divisão': [f'{numero} / {i + 1} = {"Indefinido" if i + 1 == 0 else (numero / (i + 1)):.2f}' for i in
                range(linhas)],
}))