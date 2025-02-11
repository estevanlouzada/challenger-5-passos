import streamlit as st
from components import header
import plotly.express as px 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from utils import dashboard_graph, data_loader



def render_dashboard():

    # CSS para estilizar a linha de separação
    st.markdown(
        """
        <style>
        hr {
            margin: 0;
            padding: 0;
            border: none;
            border-top: 2px solid #ddd; /* Estiliza a linha */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    header.render_header("Dashboard")
    tab1, tab2, tab3 = st.tabs(["Dashboard da Associação", "Interatividade", "insights"])


    #load
    df_2020 = data_loader.load_data_2020()
    df_2021 = data_loader.load_data_2021()
    df_2022 = data_loader.load_data_2022()

    

    with tab1:

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(label="Anos 2020 / 2021 / 2022", value="Alunos")
        col2.metric(label="Quantidade de alunos 2020", value=f"{df_2020.shape[0]}", delta=f"{0}",  border=True)
        col3.metric(label="Quantidade de alunos 2021", value=f"{df_2021.shape[0]}", delta=f"{df_2021.shape[0] - df_2020.shape[0]}" , border=True)
        col4.metric(label="Quantidade de alunos 2022", value=f"{df_2022.shape[0]}", delta=f"{df_2022.shape[0] - df_2021.shape[0]}", border=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # Segunda linha: Três gráficos
        col1, col2, col3 = st.columns(3)

        

        with col1:
            dashboard_graph.DataVisualizer.alunos_ponto_virada(df_2020, df_2021, df_2022)

        with col2:
            dashboard_graph.DataVisualizer.alunos_bolsas_estudos(df_2020, df_2021, df_2022)

        with col3:
            dashboard_graph.DataVisualizer.alunos_fases(df_2020, df_2021, df_2022)

        st.markdown("<hr>", unsafe_allow_html=True)

        # Terceira linha: Dois gráficos
        col1, col2 = st.columns(2)

        

        with col1:
            dashboard_graph.DataVisualizer.plot_alunos_pedras(df_2020, df_2021, df_2022)

        with col2:
            dashboard_graph.DataVisualizer.plot_media_indicadores(df_2020, df_2021, df_2022)
            

    with tab2:
        st.header("Interatividade")
        st.write(
            "Demonstração das funcionalidades interativas (filtros, drill down, etc)."
        )
        # Configuração inicial da página

        # Explicação adicional
        st.markdown("""
        **Observações:**
        1. O gráfico usa as colunas como categorias automaticamente
        2. As cores são atribuídas automaticamente pelo Streamlit
        3. Para mais personalização, recomendo usar Plotly
        """)


    with tab3:
        st.header("Insights")
        st.write(
            "Resumo dos principais insights que o dashboard fornece para ajudar na tomada de decisões."
        )



