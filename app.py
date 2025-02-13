import streamlit as st
from pages import home, proposta_analitica, dashboard, conclusao
from components import sidebar
from utils import config


def bootstrap():
    # st.set_page_config deve ser a primeira linha
    st.set_page_config(page_title="Minha App Streamlit", layout="wide")

        # Definir a página Home como padrão
    menu_selection = st.session_state.get("menu_selection", "Home")
    
    # Sidebar para navegação, com o valor default selecionado
    menu_selection = sidebar.render_sidebar(default_selection=menu_selection)
    
    # Conteúdo principal com tabs
    if menu_selection == "Home":
        home.render_home()

    elif menu_selection == "Proposta Analítica":
         proposta_analitica.render_proposta_analitica()

    elif menu_selection == "Dashboard":
       dashboard.render_dashboard()
       
    elif menu_selection == "Conclusao":
        conclusao.render_conclusao()
    


bootstrap()