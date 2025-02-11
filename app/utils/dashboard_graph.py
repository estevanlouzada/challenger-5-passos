import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import seaborn as sns


class DataVisualizer:
    """
    Handles all data preprocessing to create graphs
    """

    
    @staticmethod
    def alunos_ponto_virada(
        df_2020: pd.DataFrame,
        df_2021: pd.DataFrame,
        df_2022: pd.DataFrame
    ):
        """
        recive de dataframes
        
        Args:
            df_2020: Input DataFrame
            df_2021: Input DataFrame
            df_2022: Input DataFrame
        Returns:
            plot data visualize graph alunos de ponto de virada
        """

        select_sim = lambda x: x== 'Sim'
        select_nao = lambda x: x == 'Não'

        quantidade_alunos = [ df_2020['PONTO_VIRADA'].apply(select_sim).sum(), df_2020['PONTO_VIRADA'].apply(select_nao).sum(),
                             df_2021['PONTO_VIRADA'].apply(select_sim).sum(), df_2021['PONTO_VIRADA'].apply(select_nao).sum(),
                             df_2022['PONTO_VIRADA'].apply(select_sim).sum(), df_2022['PONTO_VIRADA'].apply(select_nao).sum()]

        data = {
            'Ano': [2020, 2020, 2021, 2021, 2022, 2022],
            'Categoria': ['Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não'],
            'Quantidade de Alunos': quantidade_alunos
        }

        # Criar DataFrame
        df = pd.DataFrame(data)
        # Criar gráfico interativo com Plotly
        fig = px.bar(
            df,
            x='Ano',
            y='Quantidade de Alunos',
            color='Categoria',
            barmode='group',
            title='',
            labels={'Quantidade de Alunos': 'Quantidade de Alunos', 'Ano': 'Ano'},
            height=420,
            width=800,
            color_discrete_map={'Sim': '#1f77b4', 'Não': '#ff7f0e'}
        )
        # # Ajustar layout
        # fig.update_layout(
        #     yaxis_range=[0, 800],
        #     plot_bgcolor='rgba(0,0,0,0)',
        #     title_font_size=20
        # )
        st.markdown("#### **Indicador Ponto de Virada por Ano**",
        unsafe_allow_html=True)
        # Exibir gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=False)


    @staticmethod
    def alunos_bolsas_estudos(
        df_2020: pd.DataFrame,
        df_2021: pd.DataFrame,
        df_2022: pd.DataFrame
    ):
        """
        recive de dataframes
        
        Args:
            df_2020: Input DataFrame
            df_2021: Input DataFrame
            df_2022: Input DataFrame
        Returns:
            plot data visualize graph alunos e bolsas de estudo
        """
        bolsista_publica_2020 = df_2020['INSTITUICAO_ENSINO_ALUNO'].apply(lambda x: x == 'Escola Pública' ).sum()
        bolsista_publica_2021 = df_2021['INSTITUICAO_ENSINO_ALUNO'].apply(lambda x: x == 'Escola Pública' ).sum()
        bolsista_publica_2022 = df_2022['BOLSISTA'].apply(lambda x: x != 'Sim' ).sum()

        n_bolsista_publica_2020 = df_2020['INSTITUICAO_ENSINO_ALUNO'].apply(lambda x: x != 'Escola Pública' ).sum()
        n_bolsista_publica_2021 = df_2021['INSTITUICAO_ENSINO_ALUNO'].apply(lambda x: x != 'Escola Pública' ).sum()
        n_bolsista_publica_2022 = df_2022['BOLSISTA'].apply(lambda x: x == 'Sim' ).sum()

        data = {
            'Ano': [2020, 2021, 2022],
            'Bolsista': [bolsista_publica_2020, bolsista_publica_2021, bolsista_publica_2022],
            'Escola Pública': [n_bolsista_publica_2020, n_bolsista_publica_2021, n_bolsista_publica_2022]
        }

        # Estruturação dos dados em formato wide
        data = {
            'Ano': [2020, 2021, 2022, 2023],
            'Bolsista': [500, 598, 555, 754],
            'Escola Pública': [199, 198, 200, 129]
        }
        df = pd.DataFrame(data).set_index('Ano')

        st.markdown("#### **Quantidade de Bolsas X Escola Pública**",
        unsafe_allow_html=True)
        # Criar o gráfico
        st.bar_chart(
            df,
            height=420,
            use_container_width=True
        )

    @staticmethod
    def alunos_fases(
        df_2020: pd.DataFrame,
        df_2021: pd.DataFrame,
        df_2022: pd.DataFrame
    ):
        """
        recive de dataframes
        
        Args:
            df_2020: Input DataFrame
            df_2021: Input DataFrame
            df_2022: Input DataFrame
        Returns:
            plot data visualize graph alunos e bolsas de estudo
        """

        dfs = [df_2020, df_2021, df_2022]
        anos = [2020, 2021, 2022]

        # Chama a função e imprime o resultado

        data = {}
        for df, ano in zip(dfs, anos):
            # Conta a quantidade de cada fase (0 a 8)
            fases = df['FASE'].value_counts().reindex(range(9), fill_value=0)
            data[str(ano)] = fases.tolist()
        
    
        fases = [f'Fase {i}' for i in range(9)]

        df = pd.DataFrame(data, index=fases).T.reset_index()
        df = df.melt(id_vars='index', var_name='Fase', value_name='Quantidade')
        df.columns = ['Ano', 'Fase', 'Quantidade']

        # Criar gráfico horizontal com Plotly
        fig = px.bar(
            df,
            x='Quantidade',
            y='Fase',
            color='Ano',
            orientation='h',
            height=420,
            # title='Distribuição de Alunos por Fase e Ano',
            labels={'Quantidade': 'Número de Alunos', 'Fase': ''},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        # Ajustar layout
        fig.update_layout(
            xaxis_range=[0, 1000],
            yaxis={'categoryorder': 'total ascending'},
            plot_bgcolor='rgba(0,0,0,0)',
            legend_title_text='Ano'
        )

        st.markdown("#### **Alunos nas Fases por Ano**",
        unsafe_allow_html=True)
        # Exibir no Streamlit
        st.plotly_chart(fig, use_container_width=True)


    @staticmethod
    def plot_media_indicadores(
        df_2020: pd.DataFrame,
        df_2021: pd.DataFrame,
        df_2022: pd.DataFrame
    ):
        
        """
        recive de dataframes
        
        Args:
            df_2020: Input DataFrame
            df_2021: Input DataFrame
            df_2022: Input DataFrame
        Returns:
            plot data visualize graph alunos e indicadores 
        """
        colunas_indicadores = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']

        # DataFrame consolidado para médias
        dados_consolidados = pd.DataFrame()

        dfs, anos = [df_2020[colunas_indicadores], df_2021[colunas_indicadores], df_2022[colunas_indicadores]], [2020, 2021, 2022]

        # DataFrame para armazenar os dados consolidados
        dados_consolidados = []
        for df, ano in zip(dfs, anos):
            # Calcula a média para cada indicador
            medias = df.mean()
            for indicador, media in medias.items():
                dados_consolidados.append({"Ano": ano, "Indicador": indicador, "Média": media})
        # Cria um DataFrame com as informações consolidadas
        df_consolidado = pd.DataFrame(dados_consolidados)
        # Plot com Plotly
        fig = px.line(
            df_consolidado,
            x="Ano",
            y="Média",
            height=420,
            color="Indicador",
            markers=True,
            # title="Média dos Indicadores por Ano"
        )
        fig.update_traces(line=dict(width=2))

        st.markdown("#### **Média dos Indicadores por Ano**",
        unsafe_allow_html=True)
        # Exibir gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)


    @staticmethod
    def plot_alunos_pedras(
        df_2020: pd.DataFrame,
        df_2021: pd.DataFrame,
        df_2022: pd.DataFrame
    ):
        
        """
        recive de dataframes
        
        Args:
            df_2020: Input DataFrame
            df_2021: Input DataFrame
            df_2022: Input DataFrame
        Returns:
            plot data visualize graph alunos e indicadores 
        """
        dfs = [df_2020, df_2021, df_2022]
        anos = [2020, 2021, 2022]

        registros = []
    
        for df, ano in zip(dfs, anos):
            # Agrupa e soma a quantidade de cada tipo de pedra
            agrupamento = df.groupby('PEDRA').size().reindex(['Quartzo', 'Ágata', 'Ametista', 'Topázio'], fill_value=0)
        
            # Monta os registros
            for pedra, quantidade in agrupamento.items():
                registros.append({'Ano': ano, 'Categoria': pedra, 'Quantidade de Alunos': quantidade})

        # Criar gráfico interativo com Plotly
        fig1 = px.bar(
            registros,
            x='Ano',
            y='Quantidade de Alunos',
            color='Categoria',
            barmode='group',
            title='',
            labels={'Quantidade de Alunos': 'Quantidade de Alunos', 'Ano': 'Ano'},
            height=420,
            width=800,
            color_discrete_map={'Quartzo': '#1f77b4', 'Agata': '#ff7f0e', "Topazio": "#ff000e"}
        )
        # Ajustar layout
        fig1.update_layout(
            yaxis_range=[0, 800],
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.markdown("#### **Quantidade de Alunos por Categoria(Pedra)/Ano**",
        unsafe_allow_html=True)
        # Exibir gráfico no Streamlit
        st.plotly_chart(fig1, use_container_width=True)