import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import seaborn as sns

class DataVisualizeDashEconomico:

    @staticmethod
    def alunos_idade_2020(
        alunos_anos: pd.DataFrame,
    ):
        # Contagem de alunos por idade
        age_counts = alunos_anos["IDADE_ALUNO_2020"].value_counts().reset_index()
        age_counts.columns = ["Idade", "Quantidade de Alunos"]
        age_counts = age_counts.sort_values("Idade")

        # Criando o gráfico com Plotly Express
        fig = px.bar(
            age_counts,
            x="Idade",
            y="Quantidade de Alunos",
            title="Alunos x Idade em 2020",
            text="Quantidade de Alunos",
            color_discrete_sequence=["seagreen"]
        )

        # Ajustes estéticos
        fig.update_traces(textposition="outside")
        fig.update_layout(
            title_font_size=18,
            xaxis_title="Idade",
            yaxis_title="Quantidade de Alunos",
            showlegend=False,
            width=800,
            height=400
        )

        # Exibir no Streamlit
        st.plotly_chart(fig, use_container_width=True)


    @staticmethod
    def alunos_genero(
        data: pd.DataFrame,
    ):
        # Contagem de alunos por gênero
        gender_counts = data["GENERO_ALUNO"].value_counts().reset_index()
        gender_counts.columns = ["Gênero", "Quantidade"]

        # Mapeia os valores para termos legíveis
        gender_counts["Gênero"] = gender_counts["Gênero"].replace({"F": "Feminino", "M": "Masculino"})

        # Criar gráfico de pizza
        fig = px.pie(
            gender_counts,
            values="Quantidade",
            names="Gênero",
            title="Alunos por Gênero",
            color="Gênero",
            color_discrete_map={"Feminino": "lightskyblue", "Masculino": "darkblue"},
            hole=0.3
        )

        # Adicionar rótulos de porcentagem e valores
        fig.update_traces(
            textinfo="value+percent",
            textfont_size=14,
            pull=[0, 0.1]  # Destaca a fatia masculina
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)


    @staticmethod
    def alunos_motivo_inativacao(
        data: pd.DataFrame,
    ):
        
        # Contagem de ocorrências por motivo de inativação
        motivo_counts = data["MotivoInativacao"].value_counts().reset_index()
        motivo_counts.columns = ["Motivo da Inativação", "Quantidade de Alunos"]
        
        # Criando o gráfico horizontal
        fig = px.bar(
            motivo_counts,
            x="Quantidade de Alunos",
            y="Motivo da Inativação",
            orientation='h',
            title="Alunos x Motivo de Inativação (de 2021 a 2024)",
            text="Quantidade de Alunos",
            color="Quantidade de Alunos",
            color_continuous_scale="Blues"
        )
        
        # Ajustes estéticos
        fig.update_traces(textposition='outside')
        fig.update_layout(
            xaxis_title="Quantidade de Alunos",
            yaxis_title="Motivo da Inativação",
            title_font_size=18,
            height=600,
            width=1000
        )
        
        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)