import streamlit as st
from components import header
from PIL import Image



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