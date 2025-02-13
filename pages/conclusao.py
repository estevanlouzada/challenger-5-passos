import streamlit as st
from components import header



def render_conclusao():
    header.render_header("Conclusao")
    tab1, tab2, tab3 = st.tabs(["Estrutura", "Interatividade", "insights"])
    
    with tab1:
        st.header("Impacto dos Resultados")
        st.write("Como as análises e previsões podem apoiar as ações da ONG.")
        

    with tab2:
        st.header("Recomendações:")
        st.write("Sugestões de melhorias ou novas áreas de exploração.")
        
    with tab3:
        st.header("Próximos passos:")
        st.write("Como os resultados podem ser utilizados em futuros projetos ou iniciativas.")