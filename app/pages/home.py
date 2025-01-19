import streamlit as st
from components import header
from utils import data_loader
import requests
import plotly.express as px 
import pandas as pd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image

def filter_columns(df, filters: list): # adiciono no array o padrão que existe nas colunas e que não quero que tenha na saída final
        selected_columns = [True] * len(df.columns)  # Inicializa todas as colunas como True
        for index, column in enumerate(df.columns):
            if any(filter in column for filter in filters): selected_columns[index] = False
        return df[df.columns[selected_columns]]

def render_home():
    header.render_header("Objetivo do Trabalho 🎯")
    st.markdown("O **Datathon** é uma oportunidade de aplicar conhecimentos em ciência de dados para resolver problemas reais e impactar positivamente a sociedade. Neste contexto, o nosso projeto se concentra na **ONG Passos Mágicos**, uma instituição que atua na promoção da **educação** como ferramenta para transformar a vida de crianças e jovens em situação de vulnerabilidade social.")
    st.markdown("---")
    st.markdown(" ### Objetivo Principal:")
    st.markdown("Através deste trabalho, buscamos utilizar os **dados educacionais e socioeconômicos** fornecidos pela ONG para **analisar** e **criar soluções preditivas** que possam ajudar a **Passos Mágicos** a aprimorar seu impacto social.")
    st.markdown("A proposta é:")
    st.markdown("- **Entender** melhor a evolução do desempenho escolar dos estudantes atendidos")
    st.markdown("- **Identificar** padrões e insights que possam apoiar a ONG em suas decisões estratégicas")
    st.markdown(" - **Gerar soluções preditivas** que ajudem a ONG a antecipar necessidades e otimizar seus esforços")
    st.markdown("A aplicação de dados permitirá que a ONG tenha uma visão mais clara do impacto de suas ações, possibilitando decisões mais informadas e estratégias mais eficazes para alcançar seus objetivos sociais.")
    st.markdown("---")

    # Título Principal
    st.markdown("### Os Princípios da Passos Mágicos")

    # Contêiner para a imagem de cabeçalho
    with st.container():
        st.markdown(
            """
            <style>
            .narrow-image {
                max-width: 50%; /* Ajuste este valor conforme necessário */
                margin: 0 auto; /* Centraliza a imagem horizontalmente */
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        image_header = Image.open("assets/passos_magicos1.png")
        st.image(image_header, caption="Passos Mágicos", use_container_width=True,  output_format = 'PNG',  
              )
    
    st.markdown("---")  # Separador visual

    # Contêiner para a Introdução e Missão da ONG
    with st.container():
      st.markdown("### Nossa Missão")
      st.markdown(
            f"""
            A Passos Mágicos é uma instituição sem fins lucrativos dedicada a transformar vidas através da educação.
            Nossa missão é fornecer educação de qualidade e expandir horizontes para crianças e jovens em situação
            de vulnerabilidade, capacitando-os a atingir seu pleno potencial.
            """,
          unsafe_allow_html=True
        )
    
    with st.container():
        image_header2 = Image.open("assets/passos_magicos2.png")
        st.image(image_header2, caption="Passos Mágicos", use_container_width=True)
    
    st.markdown("---")  # Separador visual

    # Contêiner para o Como Trabalhamos
    with st.container():
      st.markdown("### Como Trabalhamos")
      st.markdown(
          """
          Utilizamos uma metodologia multifacetada e própria, integrando psicologia e psicopedagogia,
          assistência social e expansão de horizontes. Nossos pilares são:
          *   **Educação de Qualidade:** Programa de aceleração do conhecimento com foco em alfabetização,
              português, matemática e inglês.
          *   **Assistência Psicológica e Psicopedagógica:** Acompanhamento individualizado e suporte para os
              alunos.
          *   **Expansão da Visão de Mundo:** Atividades e passeios culturais para ampliar horizontes.
          *   **Protagonismo:** Incentivo ao desenvolvimento da autonomia e resolução de problemas.

          Desde 2022, a assistência social tem fortalecido nosso trabalho, reconhecendo a importância do apoio familiar.
          """
      )
    with st.container():
      image_header3 = Image.open("assets/passos_magicos3.png")
      st.image(image_header3, caption="Passos Mágicos", use_container_width=True)
    
    st.markdown("---")  # Separador visual

    # Contêiner para o Impacto na Comunidade
    with st.container():
      st.markdown("### Nosso Impacto na Comunidade")
      st.markdown(
          """
          A Passos Mágicos atende à comunidade de Embu-Guaçu, SP, uma cidade com cerca de 66.970 habitantes.
          Em 2023, beneficiamos mais de 1.100 indivíduos, o que representa uma porcentagem significativa de
          estudantes da escola pública e da população local. Nossa instituição preza pela diversidade
          em seu corpo discente, onde existe a harmonia entre diferentes etnias. Contamos com uma representação
          variada, com 1,3% alunos de etnia amarela, 47,4% brancos, 41,4% pardos e 10% pretos. Além disso, nosso ambiente é
          marcado pela equidade de gênero, com 442 meninos e 506 meninas, proporcionando uma atmosfera inclusiva e enriquecedora
          para todos os nossos alunos.
          """
      )
    with st.container():
        image_header4 = Image.open("assets/passos_magicos-pontos-sociais.png")
        st.image(image_header4, caption="Passos Mágicos", use_container_width=True)
    
    st.markdown("---")  # Separador visual
    
    with st.container():
        st.markdown("### Nas estrelas do sucesso nossos preciosos diamantes:")
        descritivo_evolutivo = '''
            Avaliação de desenvolvimento educacional em medidas de variabilidade (variância e desvio padrão),
            combinadas com as medidas de posicionamento (média, mediana e modal), resultando a nota padronizada
                Quartzo - 2,405 e 5,506 - Média subtraido de um desvio padrão
                Ágata - intervalo a cima de 5,506 até 6.868 valor da média
                Ametista - 6,868 at;e 8,23 média mais um desvio padrão 
                Topázio - 8,23 limite anterior ao máximo '''
        st.write(descritivo_evolutivo)
    
    
    st.markdown("---")  # Separador visual

    with st.container():
        st.title('Dash de acompanhamento - ORG Alunos - Dash ')
        df = data_loader.load_data('')
        df_2020_21 = filter_columns(df, ['2022'])
        dados = df_2020_21['INSTITUICAO_ENSINO_ALUNO_2020'].value_counts()

        dtpedras = df_2020_21['PEDRA_2021'].value_counts()
        dtpedras_ano_passado = df_2020_21['PEDRA_2020'].value_counts()

        ametista, agata, quartzo, topazio , outro = dtpedras
        ametista2, agata2, quartzo2, topazio2 , outro2 = dtpedras_ano_passado

    
        col1, col2, col3, col4 = st.columns(4)

        col1.metric(label="Ametista :gem:", value=f"{ametista}", delta=f"{ametista - ametista2} neste ano",border=True )
        col2.metric("Agata :gem:", f"{agata}", f"{agata - agata2} neste ano",border=True)
        col3.metric("Quartzo :gem:", f"{quartzo}", f"{quartzo - quartzo2} neste ano",border=True)
        col4.metric("Topazio :gem:", f"{topazio}", f"{topazio - topazio2} neste ano",border=True)

    st.dataframe(dados)