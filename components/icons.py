import streamlit as st

def display_icons_quartzo():
    # HTML para incluir ícones do Font Awesome
    st.markdown('''
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <i class="fas fa-gem" style="font-size:60px;color:purple;margin:5px;padding:0;"></i>  <!-- Ícone de Crystal Ball (Cristal) -->
    ''', unsafe_allow_html=True)

def ametista_markdown():
    return '''
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <i class="fas fa-gem" style="font-size:20px;color:purple;margin:0;padding:0;"></i>  <!-- Ícone de Crystal Ball (Cristal) -->
    '''
def quartzo_markdown():
    return '''
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <i class="fas fa-gem" style="font-size:20px;color:red;margin:0;padding:0;"></i>  <!-- Ícone de Crystal Ball (Cristal) -->
    '''
def Agata_markdown():
    return '''
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <i class="fas fa-gem" style="font-size:20px;color:blue;margin:0;padding:0;"></i>  <!-- Ícone de Crystal Ball (Cristal) -->
    '''
def Topazio_markdown():
    return '''
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <i class="fas fa-gem" style="font-size:20px;color:#4B98C0;margin:0;padding:0;"></i>  <!-- Ícone de Crystal Ball (Cristal) -->
    '''


def teste_markdown():
         # Exemplo com HTML para adicionar estilo ao emoji
    st.markdown("""
        <span style="font-size: 50px; color: red;">😀</span>
        <span style="font-size: 50px; color: green;">😎</span>
        <span style="font-size: 50px; color: blue;">❤️</span>
    """, unsafe_allow_html=True)

