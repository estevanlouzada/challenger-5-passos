import streamlit as st
from components import header


def render_proposta_analitica():
    header.render_header("Proposta Analítica")
    tab1, tab2 , tab3, tab4 = st.tabs(["Visao", "Indicadores", "Dashboard", "Storyteling"])

    with tab1:
        st.header("Visão geral da análise")
        st.write("Introdução explicando como a análise foi realizada.")

    with tab2:
        st.header("Indicadores de Performance:")
        st.write("Descrição dos principais indicadores que foram analisados, como notas, evolução acadêmica, taxas de sucesso, etc.")

    with tab3:
        st.header("Dashboard Interativo:")
        st.write("Um link ou embedding do dashboard que você criou para exibir os dados de forma interativa. Caso seja possível, adicione filtros para visualização por diferentes métricas (ano, área de estudo, faixa etária, etc).")
        
    with tab4:
        st.header("Storytelling:")
        st.write("Apresentação da história dos dados, destacando como as descobertas podem impactar as decisões da ONG.")