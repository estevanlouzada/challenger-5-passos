import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 


data = {

    "Nome": ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Jr', 'Mbapé',],
    "Velocidade":[90, 85, 88, 80],
    'Forca': [85, 80, 60, 60],
    'Agilidade': [88, 92, 90, 90],
    'Inteligencia': [89,95, 90, 60]
}

df = pd.DataFrame(data)

st.title("Radar de alunos da passos-mágicos")

st.subheader("Tabela de Alunos")

selected_player = st.selectbox("Selecionar um jogador", df['Nome'])


#filtrar os dados do jogador selecionado 

player_data = df[df["Nome"] == selected_player].iloc[0]

def create_radar_chart(player_data):
    categories = ["Velocidade", "Forca", "Agilidade", "Inteligencia"]
    values = [player_data[cat] for cat in categories]

    fig = go.Figure()

    #adiciona o grafico de radar 
    fig.add_trace(go.Scatterpolar(
        r = values,
        theta= categories, 
        fill='toself',
        name=player_data["Nome"]
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
                #escala maxima dos atributos
            )
        ),
        showlegend=False
    )
    return fig

#exibir o radar 
st.subheader(f"Radas de Desempenho: {selected_player}")
fig = create_radar_chart(player_data)
st.plotly_chart(fig)
