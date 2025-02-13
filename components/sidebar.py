import streamlit as st


def render_sidebar(default_selection="Home"):
    with st.sidebar:
        st.title("Menu")
        menu_selection = st.radio("Selecione uma seção:", ["Home", "Proposta Analítica", "Proposta Preditiva", "Dashboard", "Conclusao"], index = ["Home", "Proposta Analítica", "Proposta Preditiva", "Dashboard", "Conclusao"].index(default_selection))
        st.session_state["menu_selection"] = menu_selection
    return menu_selection