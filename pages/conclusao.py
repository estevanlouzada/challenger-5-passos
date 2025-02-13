import streamlit as st
from components import header



def render_conclusao():
    
    tab1, tab2 = st.tabs(["Conclusão", "Conclusão descritiva"])

    with tab1:
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
    with tab2:

        texto_conclusao = """ 
# Conclusão

Ao longo do desenvolvimento deste projeto, analisamos diversos fatores que influenciam o desempenho acadêmico, psicossocial e psicopedagógico dos alunos atendidos pela Passos Mágicos. Os dados levantados revelaram padrões importantes, auxiliando na compreensão dos desafios enfrentados pelos estudantes, bem como dos pontos de virada que podem transformar suas trajetórias educacionais.

Os principais aspectos analisados foram **Pedras, Ponto de Virada, Evasão, Indicador Psicossocial, Indicador Psicopedagógico** e **Indicador Acadêmico**, cada um trazendo insights relevantes sobre o impacto do projeto na vida dos alunos.

## Pedras

A análise das "pedras" demonstrou que a maioria dos alunos está enquadrada entre as categorias **Ágata** e **Ametista**, indicando uma evolução contínua no desempenho anual dos estudantes. Além disso, historicamente, observa-se um crescimento na **Pedra Topázio**, a de maior valor agregado, evidenciando que a atuação da Passos Mágicos tem contribuído significativamente para o progresso educacional das crianças e jovens da região.

## Evasão

Um ponto de atenção relevante é a retenção dos alunos. Entre os motivos de evasão identificados, destaca-se que **19% dos casos estão relacionados à falta de retorno às tentativas de contato**. Esse dado sugere que novas estratégias de comunicação com os alunos e suas famílias podem ser implementadas para reduzir a evasão e fortalecer o vínculo com a comunidade.

## Ponto de Virada

Entre **2020 e 2022**, houve um crescimento expressivo no número de alunos que alcançaram o **Ponto de Virada**. Entretanto, ao analisar a evolução percentual, observamos uma queda de **18,8% (2021) para 15,1% (2022)** no percentual de alunos que atingiram esse marco. Vale ressaltar que essa redução não indica um menor desempenho dos estudantes, já que a base de alunos aumentou em **26% entre 2021 e 2022**.

## Indicador Psicossocial

No âmbito psicossocial, avaliamos dois indicadores principais: **IAA** e **IPS**. O **IAA**, que mede o atendimento e acompanhamento dos alunos, apresentou resultados positivos, com uma média superior a **8**. Já o **IPS**, quando analisado de forma geral, ficou abaixo de **7**. Entretanto, ao segmentar os dados por fase e excluir outliers, percebe-se que a média se aproxima de **8**. Apesar de alguns casos que demandam acompanhamento mais próximo, os dados indicam que a Passos Mágicos tem obtido um impacto significativo no desenvolvimento emocional e social dos alunos.

## Indicador Psicopedagógico

Na análise psicopedagógica, o **Índice de Permanência e Valorização (IPV)** tem se mantido estável, indicando um bom nível de retenção e satisfação dos alunos no ambiente escolar. Já o **Índice de Progresso Pessoal (IPP)**, essencial para medir o desenvolvimento individual, apresenta certa variação na média geral, influenciada pela chegada de novos alunos que ainda estão desenvolvendo suas habilidades sociais e enfrentando desafios mais complexos.

## Indicador Acadêmico

No que diz respeito ao desempenho acadêmico, o **Índice de Engajamento (IEG)** apresentou um retorno bastante positivo. No entanto, outros indicadores indicam a necessidade de um monitoramento mais próximo. O **Índice de Atenção Nutricional (IAN)**, que avalia aspectos relacionados à nutrição e bem-estar dos alunos, tem mostrado uma queda linear ao longo dos anos. Já o **Índice de Desenvolvimento Acadêmico (IDA)**, que mede o progresso educacional, continua sendo o mais desafiador, apresentando o menor desempenho entre os indicadores. Apesar de uma recuperação em **2022**, após uma queda brusca em **2021**, o **IDA ainda permanece abaixo dos demais**, reforçando a importância de estratégias para potencializar o aprendizado e o desenvolvimento dos alunos.

## Considerações Finais

Os dados analisados demonstram que a **Passos Mágicos** tem desempenhado um papel fundamental na evolução acadêmica e social dos alunos atendidos. Apesar dos desafios identificados, os resultados refletem o impacto positivo do projeto na vida das crianças e jovens, contribuindo para o desenvolvimento contínuo e a construção de novas oportunidades. 

A adoção de estratégias focadas em **comunicação, suporte psicopedagógico e melhoria nos indicadores acadêmicos** pode fortalecer ainda mais os resultados e ampliar o impacto do programa no futuro.
 """
        st.markdown(texto_conclusao)