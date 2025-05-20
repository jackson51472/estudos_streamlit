import streamlit as st

if "conta" not in st.session_state:
    st.session_state.conta = []
if "resultado" not in st.session_state:
    st.session_state.resultado = 0

def montar_calculadora():
    for linha in layout:
        cols = st.columns(4)
        for i, valor in enumerate(linha):
            if valor in texto_botoes:
                texto = texto_botoes[valor]
                if valor == '=':
                    if cols[i].button(texto, key=f"btn_{valor}", use_container_width=True):
                        calcular_resultado()
                elif valor == 'C':
                    if cols[i].button(texto, key=f"btn_{valor}", use_container_width=True):
                        limpar_conta()
                else:
                    if cols[i].button(texto, key=f"btn_{valor}", use_container_width=True):
                        adicionar_item(valor)
            else:
                if cols[i].button(str(valor), key=f"btn_{valor}", use_container_width=True):
                    adicionar_item(valor)

def calcular_resultado():
    try:
        expressao = ''.join(str(item) for item in st.session_state.conta)
        resultado = eval(expressao)
        st.session_state.resultado = resultado
        st.session_state.conta = [resultado]
    except Exception as e:
        st.error(f"Erro: {str(e)}")

def adicionar_item(item):
    st.session_state.conta.append(item)

def limpar_conta():
    st.session_state.conta.clear()
    st.session_state.resultado = 0

st.title("Calculadora")

expressao_atual = ''.join(str(item) for item in st.session_state.conta)
st.markdown(f"## Expressão: {expressao_atual}")

layout = [
    [1, 2, 3, '+'],
    [4, 5, 6, '-'],
    [7, 8, 9, '*'],
    ['=', 0, 'C', '/']
]

texto_botoes = {
    '+': 'Soma',
    '-': 'Subtração',
    '*': 'Multiplicação',
    '/': 'Divisão',
    'C': 'Limpar',
    '=': '='
}

montar_calculadora()

st.markdown(f"## Resultado: {st.session_state.resultado}")