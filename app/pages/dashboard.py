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

    with tab3:
        st.header("Insights")
        st.write(
            "Resumo dos principais insights que o dashboard fornece para ajudar na tomada de decisões."
        )
