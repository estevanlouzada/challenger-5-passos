import streamlit as st
from components import header
import plotly.express as px 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def render_dashboard():
    header.render_header("Dashboard")
    tab1, tab2, tab3 = st.tabs(["Estrutura", "Interatividade", "insights"])

    with tab1:
        st.header("Estrutura do Dashboard")
        st.write(
            "Breve descrição do que cada parte do dashboard representa (indicadores, filtros, gráficos)."
        )

    # Primeira linha: Métricas principais
    st.markdown("## Dashboard de Análise de Dados")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(label="Vendas Totais", value="R$ 200K", delta="+5%")
    col2.metric(label="Novos Usuários", value="1.2K", delta="+12%")
    col3.metric(label="Taxa de Conversão", value="3.4%", delta="+0.5%")
    col4.metric(label="Churn", value="2.8%", delta="-0.3%")

    # Segunda linha: Três gráficos
    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.title("Indicador de Ponto de Virada por Ano")

        # Dados fornecidos
        data = {
            'Ano': [2020, 2020, 2021, 2021, 2022, 2022],
            'Categoria': ['Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não'],
            'Quantidade de Alunos': [94, 607, 108, 576, 113, 749]
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
            title='Distribuição de Alunos por Ano e Categoria',
            labels={'Quantidade de Alunos': 'Quantidade de Alunos', 'Ano': 'Ano'},
            height=500,
            width=800,
            color_discrete_map={'Sim': '#1f77b4', 'Não': '#ff7f0e'}
        )

        # Ajustar layout
        fig.update_layout(
            yaxis_range=[0, 800],
            plot_bgcolor='rgba(0,0,0,0)',
            title_font_size=20
        )

        # Exibir gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        
        st.title("Quantidade de Bolsistas x Escola Pública")

        # Estruturação dos dados em formato wide
        data = {
            'Ano': [2020, 2021, 2022, 2023],
            'Bolsista': [500, 598, 555, 754],
            'Escola Pública': [199, 198, 200, 129]
        }

        df = pd.DataFrame(data).set_index('Ano')

        # Criar o gráfico
        st.bar_chart(
            df,
            height=500,
            use_container_width=True
        )

    with col3:
        st.title("Quantidade de Alunos nas Fases por Ano")

        # Estruturar os dados
        data = {
            '2020': [82, 172, 155, 122, 55, 54, 38, 0, 0],
            '2021': [120, 136, 162, 115, 59, 50, 0, 0, 0],
            '2022': [190, 192, 155, 148, 76, 60, 0, 0, 0]
        }

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
            height=600,
            title='Distribuição de Alunos por Fase e Ano',
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

        # Exibir no Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # Terceira linha: Dois gráficos
    col1, col2 = st.columns(2)

    with col1:
                # Título do aplicativo
        st.title('Quantidade de Alunos por Categoria (Pedra)/Ano')

        # Criar dados de exemplo
        dados = {
            'Ano': [2020,2020,2020,2020, 2021,2021,2021,2021, 2022,2022,2022,2022],
            'Categoria': ['Quartzo', 'Agata', 'Ametista', 'Topazio', 'Quartzo', 'Agata', 'Ametista', 'Topazio','Quartzo', 'Agata', 'Ametista', 'Topazio'],
            'Quantidade de Alunos': [120, 80, 60, 90, 135, 90, 65, 85,150, 100, 70, 88 ]
        }

         # Criar DataFrame
        df1 = pd.DataFrame(dados)

        # Criar gráfico interativo com Plotly
        fig1 = px.bar(
            df1,
            x='Ano',
            y='Quantidade de Alunos',
            color='Categoria',
            barmode='group',
            title='Distribuição de Alunos por Ano e Categoria',
            labels={'Quantidade de Alunos': 'Quantidade de Alunos', 'Ano': 'Ano'},
            height=500,
            width=800,
            color_discrete_map={'Quartzo': '#1f77b4', 'Agata': '#ff7f0e', "Topazio": "#ff000e"}
        )

        # Ajustar layout
        fig1.update_layout(
            yaxis_range=[0, 800],
            plot_bgcolor='rgba(0,0,0,0)',
            title_font_size=20
        )

        # Exibir gráfico no Streamlit
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        def plot_media_indicadores(dfs, anos):
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
                color="Indicador",
                markers=True,
                title="Média dos Indicadores por Ano"
            )
            fig.update_traces(line=dict(width=2))
            fig.show()

                    # Exibir gráfico no Streamlit
            st.plotly_chart(fig, use_container_width=True)

        # Simulação de DataFrames com os dados fictícios
        df_2020 = pd.DataFrame({'INDE': [10000.0, 9500.5, 8900.2], 'IEG': [10500.3, 10200.4, 10900.1], 'IDA': [5300.4, 5400.6, 5200.0]})
        df_2021 = pd.DataFrame({'INDE': [9000.2, 9400.1, 9300.5], 'IEG': [10700.5, 10200.4, 10100.3], 'IDA': [5100.4, 5000.2, 5200.1]})
        df_2022 = pd.DataFrame({'INDE': [8000.4, 8500.6, 8700.3], 'IEG': [9600.7, 9700.4, 9500.2], 'IDA': [4900.5, 4700.1, 4800.3]})

        # Chama a função com os DataFrames
        plot_media_indicadores([df_2020, df_2021, df_2022], [2020, 2021, 2022])

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



