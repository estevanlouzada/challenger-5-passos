import streamlit as st
from components import header


def render_proposta_preditiva():
    header.render_header("Proposta Preditiva")
    tab1, tab2, tab3, tab4 = st.tabs(["Descrição", "Métodos", "Resultados", "Deploy"])

    with tab1:
        st.header("Descrição do modelo preditivo:")
        st.write("Detalhes sobre como o modelo foi desenvolvido (algoritmo escolhido, pré-processamento dos dados, etc).")

    with tab2:
        st.header("Métodos e Técnicas:")
        st.write("Explicar as técnicas de machine learning ou deep learning utilizadas.")

    with tab3:
        st.header("Resultados:")
        st.write("Mostrar as métricas de desempenho do modelo, como acurácia, F1-score, etc.")

    with tab4:
        st.header("Deploy no Streamlit:")
        st.write("Link ou embed do modelo preditivo, se possível, para visualização interativa.")
        
        
        