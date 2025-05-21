import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def carrega_vendas(arquivo):
    try:
        df = pd.read_csv(arquivo, delimiter=";")
        colunas_necessarias = ["Vendedor", "Venda", "Valor_Medio"]
        if not all(coluna in df.columns for coluna in colunas_necessarias):
            st.error("Arquivo não contém as colunas necessárias: Vendedor, Venda, Valor_Medio")
            return None

        df["Venda"] = pd.to_numeric(df["Venda"], errors="coerce")
        df["Valor_Medio"] = pd.to_numeric(df["Valor_Medio"], errors="coerce")

        if df["Venda"].isnull().any() or df["Valor_Medio"].isnull().any():
            st.warning("Alguns valores não puderam ser convertidos. Eles serão excluídos da análise.")
            df = df.dropna(subset=["Venda", "Valor_Medio"])
        return df

    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None


st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Dashboard de Vendas")
st.subheader("Visualização e Filtragem de Dados de Vendas")

with st.expander("ℹ️ Instruções de Uso"):
    st.write("""
    1. Carregue um arquivo TXT com delimitador ";" contendo os dados de vendas.
    2. O arquivo deve conter, no mínimo, as colunas: Vendedor, Venda e Valor_Medio.
    3. Selecione o tipo de busca desejado.
    4. Use o slider para filtrar os dados conforme necessário.
    """)

## Parte aonde eu selecio o meu arquivo para ser mostrado
arquivo_vendas = st.file_uploader("Escolha um arquivo de vendas (.txt)"
                                  "\n Na pasta Vendas tem um arquivo pronto para exemplo", type=["txt"])

if arquivo_vendas is not None:

## Selecioonando o tipo de
    tipo = st.selectbox("Tipo de busca", options=["Total de vendas", "Valor medio"])
    base_vendas = carrega_vendas(arquivo_vendas)
    if tipo == "Total de vendas":
        min_v, max_v = int(base_vendas["Venda"].min()), int(base_vendas["Venda"].max())
        venda_selecionada = st.slider("Selecione o intervalo de vendas dos vendedores", min_v, max_v, (min_v, max_v))

        filtro_vendas = base_vendas[
            (base_vendas["Venda"] >= venda_selecionada[0]) & (base_vendas["Venda"] <= venda_selecionada[1])]

        with st.container():
            coluna1, coluna2 = st.columns(2)

            ## Coluna com a tabela do arquivo que foi passado
            with coluna1:
                st.write(f"Dados filtrados com vendas entre {venda_selecionada[0]} e {venda_selecionada[1]}:")
                st.dataframe(filtro_vendas)

            ## coluna com o grafico que vai ser criado com o matplotlib
            with coluna2:
                st.write("Gráfico de Vendas:")
                fig, ax = plt.subplots()
                filtro_vendas.plot(kind="bar", x="Venda", y="Valor_Medio", ax=ax)
                st.pyplot(fig)

    else:
        min_v, max_v = int(base_vendas["Valor_Medio"].min()), int(base_vendas["Valor_Medio"].max())
        venda_selecionada = st.slider("Selecione o intervalo de valor medio de vendas dos vendedores", min_v, max_v, (min_v, max_v))

        filtro_vendas = base_vendas[
            (base_vendas["Valor_Medio"] >= venda_selecionada[0]) & (base_vendas["Valor_Medio"] <= venda_selecionada[1])]

        with st.container():
            coluna1, coluna2 = st.columns(2)

    ## Coluna com a tabela do arquivo que foi passado
            with coluna1:
                st.write(f"Dados filtrados com media de vendas entre {venda_selecionada[0]} e {venda_selecionada[1]}:")
                st.dataframe(filtro_vendas)

    ## coluna com o grafico que vai ser criado com o matplotlib
            with coluna2:
                st.write("Gráfico de Media de Vendas:")
                fig, ax = plt.subplots()
                filtro_vendas.plot(kind="bar", x="Valor_Medio", y="Venda", ax=ax)
                st.pyplot(fig)