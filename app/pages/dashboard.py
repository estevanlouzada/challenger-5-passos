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

    with tab2:
        st.header("Interatividade")
        st.write(
            "Demonstração das funcionalidades interativas (filtros, drill down, etc)."
        )
        # Configuração inicial da página
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

