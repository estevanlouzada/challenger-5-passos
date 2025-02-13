import streamlit as st


def render_sidebar(default_selection="Home"):
    with st.sidebar:
        st.title("Menu")
        menu_selection = st.radio("Selecione uma seção:", ["Home", "Proposta Analítica", "Dashboard", "Conclusao"], index = ["Home", "Proposta Analítica", "Dashboard", "Conclusao"].index(default_selection))
        st.session_state["menu_selection"] = menu_selection


        st.title("Integrantes do Grupo 49")
        st.markdown("**Estevan Louzada Souza**\
        \n estevan.louzada@gmail.com\
        \n **Amanda Beatriz da Silva**\
        \n amanda.beatriz@gmail.com\
        \n **Gabriel Ramalho Abahit**\
        \n gabahit@hotmail.com")


    return menu_selection