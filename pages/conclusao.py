import streamlit as st
from components import header



def render_conclusao():
    
    # Seção de Conclusão
    st.header("🔍 Conclusão")
    st.write("Ao longo do desenvolvimento deste projeto, analisamos diversos fatores que influenciam o desempenho acadêmico, psicossocial e psicopedagógico dos alunos atendidos pela Passos Mágicos. Os dados levantados revelaram padrões importantes, auxiliando na compreensão dos desafios enfrentados pelos estudantes.")
    st.markdown("---")
    
    # Criando colunas para melhor visualização
    a, b = st.columns(2)
    
    with a:
        st.subheader("💎 Pedras")
        st.write("A maioria dos alunos está entre Ágata e Ametista, indicando uma evolução no desempenho. O crescimento da Pedra Topázio mostra um impacto positivo do programa.")
        
        st.subheader("🚪 Evasão")
        st.write("A taxa de evasão preocupa, com 19% dos casos devido à falta de retorno nas tentativas de contato. Melhorar a comunicação pode reduzir esse problema.")
        
        st.subheader("📈 Ponto de Virada")
        st.write("Entre 2020 e 2022, o número de alunos que atingiram esse marco aumentou, mas o percentual caiu de 18,8% para 15,1% devido ao crescimento da base de alunos.")
    
    with b:
        st.subheader("🧠 Indicador Psicossocial")
        st.write("Os indicadores IAA e IPS mostraram bons resultados, com o IAA acima de 8 e o IPS, após ajustes, também próximo desse valor.")
        
        st.subheader("🎓 Indicador Psicopedagógico")
        st.write("Os índices IPP e IPV apresentaram resultados positivos quando segmentados, indicando boa participação dos alunos.")
        
        st.subheader("📚 Indicador Acadêmico")
        st.write("O IEG teve um retorno positivo, mas o IDA continua sendo o mais desafiador, apresentando desempenho inferior aos demais.")
    
    st.markdown("---")
    
    # Considerações finais
    st.header("📌 Considerações Finais")
    st.write("Os dados demonstram que a Passos Mágicos tem sido fundamental na evolução acadêmica e social dos alunos. Apesar dos desafios, os resultados são positivos e mostram impacto significativo na vida dos estudantes. Estratégias para comunicação, suporte psicopedagógico e melhorias acadêmicas podem ampliar ainda mais esse impacto.")
