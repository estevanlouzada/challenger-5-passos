import streamlit as st
from components import header
import plotly.express as px 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from utils import dashboard_graph, data_loader, dashboard_socioeconomico
import plotly.express as px
import plotly.graph_objects as go 



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
    tab1, tab2, tab3 = st.tabs(["Dashboard da Associação", "Dashboard Socioeconômico", "insights"])


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
        st.header("Dashboard Socioeconômico")

        # Explicação adicional
        st.markdown("""
        **Observações:**
        1. Os graficos tratam de informações de quantidade de alunos e distribuições.
        2. Da distribuição presente entre gênero na associação alunos e alunas.  
        3. Dispersão de evação e informações sobre os motivos mais recorrentes.
        """)


        df_alunos_idade = pd.read_csv('data/powerbi_idade_aluno.csv', sep=',')
        df_aluno_genero = pd.read_csv('data/powerbi_genero.csv', sep=',')
        df_motivo_inatividade = pd.read_csv('data/powerbi_motivo_inativacao.csv', sep=',')   
        col1, col2 = st.columns(2)
        with col1:
            dashboard_socioeconomico.DataVisualizeDashEconomico.alunos_idade_2020(df_alunos_idade)
        with col2:
            dashboard_socioeconomico.DataVisualizeDashEconomico.alunos_genero(df_aluno_genero)
        st.markdown("<hr>", unsafe_allow_html=True)
        # Segunda linha: Três gráficos

        dashboard_socioeconomico.DataVisualizeDashEconomico.alunos_motivo_inativacao(df_motivo_inatividade)
        st.markdown("<hr>", unsafe_allow_html=True)



    with tab3:
        st.header("Insights")
        st.write(
            "Resumo dos principais insights que o dashboard fornece para ajudar na tomada de decisões."
        )


        df_tot = pd.read_csv('data/pede_total.csv', sep=';')

        select = ['NOME', 'INDE', 'INDE_CONCEITO', 'PEDRA',  'IAA', 'IEG', 'IPS', 'IDA', 'IPP',
       'IPV', 'IAN', 'ANO']

        df = df_tot[select]    


        df["Selecionado"] = False

        st.title("Radar de alunos da passos-mágicos")

        st.subheader("Tabela de Alunos")

        
        if "selected_player" not in st.session_state:
            st.session_state.selected_player = None

        edited_df = st.data_editor(
            df, 
            column_config = {"Selecionado": st.column_config.CheckboxColumn()},
            disabled=['NOME','INSTITUICAO_ENSINO_ALUNO','IDADE_ALUNO','INDE','PEDRA','IAA','IEG','IPS','IDA','IPP','IPV','IAN','ANO','ANO_INGRESSO','INDICADO_BOLSA'], 
            hide_index=True
        )

        selected_row = edited_df[edited_df["Selecionado"]]


        if not selected_row.empty:
            player_data = selected_row.iloc[0]
            st.session_state.selected_player = player_data
            
        
        if selected_row.empty:
            selected_row = edited_df.iloc[0,:]
            player_data = edited_df.iloc[0,:]
            st.session_state.selected_player = player_data

        def create_radar_chart(player_data):
            categories = ['IAA','IEG','IPS','IDA','IPP','IPV','IAN']
            values = [player_data[cat] for cat in categories]
            fig = go.Figure()
            #adiciona o grafico de radar 
            fig.add_trace(go.Scatterpolar(
                r = values,
                theta= categories, 
                fill='toself',
                name=player_data["NOME"]
            ))
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0,10]
                        #escala maxima dos atributos
                    )
                ),
                showlegend=False
            )
            return fig
        #exibir o radar 

        
        st.subheader(f"Radar de Desempenho: {player_data["NOME"] }")
        fig = create_radar_chart(st.session_state.selected_player)
        st.plotly_chart(fig)








