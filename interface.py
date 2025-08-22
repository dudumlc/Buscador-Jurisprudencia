import streamlit as st
import pandas as pd
import os
from utils.model import generate_response

st.title("📚Buscador de Jurisprudência")

# Nome do arquivo Excel
excel_file = "output/jurisprudencia_extraida.xlsx"

# Verifica se o arquivo existe
if not os.path.exists(excel_file):
    st.error(f"Arquivo '{excel_file}' não encontrado na pasta do projeto.")
else:
    # Lê o Excel
    df = pd.read_excel(excel_file)

    # Filtro de texto para Tema
    tema_digitado = st.text_input("Digite o Tema:")

    # Filtro de selectbox para Ramo do Direito
    if "RAMO_DO_DIREITO" in df.columns:
        ramos_unicos = df["RAMO_DO_DIREITO"].dropna().unique()
        ramo_selecionado = st.selectbox(
            "Selecione o Ramo do Direito:",
            options=[""] + list(ramos_unicos),  # adiciona opção vazia
            index=0
        )
    else:
        st.warning("Coluna 'RAMO_DO_DIREITO' não encontrada no Excel.")
        ramo_selecionado = ""

    # Botão para filtrar
    if st.button("Filtrar", type="primary", use_container_width=True):
        # Estilo do botão (vermelho)
        st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: red;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

        # Aplica filtros
        df_filtrado = df.copy()

        if ramo_selecionado:
            df_filtrado = df_filtrado[df_filtrado["RAMO_DO_DIREITO"] == ramo_selecionado]

        if tema_digitado:
            df_filtrado = df_filtrado[df_filtrado["TEMA"].str.contains(tema_digitado, case=False, na=False)]

        # Exibir resultados
        if not df_filtrado.empty:
            st.write(f'{len(df_filtrado)} correspondentes encontrados.')

            # CSS para alterar o fundo do conteúdo interno do expander
            st.markdown("""
            <style>
            /* Área interna do expander quando aberto */
            details[open] > div {
                background-color: #f0f0f0 !important; /* cinza claro */
                padding: 10px;
                border-radius: 5px;
            }
            </style>
            """, unsafe_allow_html=True)

            # Teste

            for _, row in df_filtrado.iterrows():

                # Initialize session state for the expander's expanded state
                if 'my_expander_expanded' not in st.session_state:
                    st.session_state.my_expander_expanded = False
                    
                with st.expander(f"**TESE:** {row.get('DESTAQUE', '')}"):
                    st.write(f"**PROCESSO:** {row.get('PROCESSO', '')}")
                    st.write(f"**TEMA:** {row.get('TEMA', '')}")
                    st.write(f"**RESUMO IA:** {generate_response(row.get('INTEIRO_TEOR', ''))}")
                    st.markdown(f"**ACESSE AQUI O INFORMATIVO:** [LINK]({row.get('LINK', '')})")
        else:
            st.warning("Nenhum resultado encontrado.")

