import streamlit as st
from components import header
from utils import data_loader
import plotly.express as px 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def filter_columns(df, filters: list): # adiciono no array o padrão que existe nas colunas e que não quero que tenha na saída final
        selected_columns = [True] * len(df.columns)  # Inicializa todas as colunas como True
        for index, column in enumerate(df.columns):
            if any(filter in column for filter in filters): selected_columns[index] = False
        return df[df.columns[selected_columns]]


def render_proposta_analitica():
    header.render_header("Proposta Analítica")
    tab1, tab2 , tab3, tab4 = st.tabs(["Visao", "Indicadores", "Dashboard", "Storyteling"])

    with tab1:
        st.header("Visão geral da análise")
        st.write("Introdução explicando como a análise foi realizada.")
        with st.container():
            st.markdown("### Nas estrelas do sucesso nossos preciosos diamantes:")
            descritivo_evolutivo = '''
                Avaliação de desenvolvimento educacional em medidas de variabilidade (variância e desvio padrão),
                combinadas com as medidas de posicionamento (média, mediana e modal), resultando a nota padronizada
                    Quartzo - 2,405 e 5,506 - Média subtraido de um desvio padrão
                    Ágata - intervalo a cima de 5,506 até 6.868 valor da média
                    Ametista - 6,868 at;e 8,23 média mais um desvio padrão 
                    Topázio - 8,23 limite anterior ao máximo '''
            st.write(descritivo_evolutivo)
        
        
            st.markdown("---")  # Separador visual
        with st.container():
            st.title('Dash de acompanhamento - ORG Alunos - Dash ')
            df = data_loader.load_data('')
            df_2020_21 = filter_columns(df, ['2022'])
            dados = df_2020_21['INSTITUICAO_ENSINO_ALUNO_2020'].value_counts()

            dtpedras = df_2020_21['PEDRA_2021'].value_counts()
            dtpedras_ano_passado = df_2020_21['PEDRA_2020'].value_counts()

            ametista, agata, quartzo, topazio , outro = dtpedras
            ametista2, agata2, quartzo2, topazio2 , outro2 = dtpedras_ano_passado


            col1, col2, col3, col4 = st.columns(4)

            col1.metric(label="Ametista :gem:", value=f"{ametista}", delta=f"{ametista - ametista2} neste ano",border=True )
            col2.metric("Agata :gem:", f"{agata}", f"{agata - agata2} neste ano",border=True)
            col3.metric("Quartzo :gem:", f"{quartzo}", f"{quartzo - quartzo2} neste ano",border=True)
            col4.metric("Topazio :gem:", f"{topazio}", f"{topazio - topazio2} neste ano",border=True)

        st.dataframe(dados)
    with tab2:
        st.header("Indicadores de Performance:")
        st.write("Descrição dos principais indicadores que foram analisados, como notas, evolução acadêmica, taxas de sucesso, etc.")

    with tab3:
        st.header("Dashboard Interativo:")
        st.write("Um link ou embedding do dashboard que você criou para exibir os dados de forma interativa. Caso seja possível, adicione filtros para visualização por diferentes métricas (ano, área de estudo, faixa etária, etc).")
        
    with tab4:
        
        vulnerabilidade_embu_guacu = '''
        ## Vulnerabilidade Socioeconômica e Deficiências Educacionais em Embu-Guaçu

        ### 1. Vulnerabilidade Socioeconômica em Embu-Guaçu

        Embu-Guaçu, município localizado na Região Metropolitana de São Paulo, apresenta diversas características socioeconômicas que refletem vulnerabilidade. A seguir, são apresentados alguns indicadores importantes:

        #### **Índice de Desenvolvimento Humano (IDH)**

        - **IDH de Embu-Guaçu (2010):** 0,749, considerado **bom**. Este valor está abaixo da média do estado de São Paulo (0,783) e do Brasil (0,765), indicando que ainda existem desafios nas áreas de educação, saúde e renda.

        #### **Acesso a Serviços Básicos**

        - A cidade enfrenta desafios em termos de **infraestrutura urbana**, com problemas no **saneamento básico** e **transporte público**.
        - Em termos de **saúde**, a cobertura e a qualidade dos serviços são limitadas, o que compromete a qualidade de vida da população.

        #### **Violência e Segurança Pública**

        - Embu-Guaçu, como muitas cidades periféricas, enfrenta **alto índices de violência**, com uma taxa de homicídios e crimes contra o patrimônio frequentemente superior à média estadual.
        - Em 2020, Embu-Guaçu estava em 17º lugar no ranking de Exposição à Violência (IECV)

        ### 2. Deficiência no Aprendizado ou Aspectos Educacionais

        A educação é um fator chave para o desenvolvimento, mas em Embu-Guaçu, algumas dificuldades contribuem para a manutenção da vulnerabilidade da população. A seguir, estão os principais indicadores:

        #### **Taxa de Analfabetismo**

        - **Taxa de analfabetismo (2010)**: Embu-Guaçu apresenta uma taxa de analfabetismo de aproximadamente **6,07%**. Isso reflete a existência de uma defasagem no acesso e na qualidade da educação básica.

        #### **Desempenho Escolar**

        - **IDEB (Índice de Desenvolvimento da Educação Básica)**: O IDEB de Embu-Guaçu é de **5,8** no ensino fundamental, o que está abaixo da meta esperada (6,6) para 2021. Esse dado reflete dificuldades no aprendizado, especialmente nas séries iniciais.

        #### **Abandono e Reprovação Escolar**
        
        -  2023 São paulo teve uma taxa e abandono de **5,70%** a taxa de abandono em Embu-Guaçu para nascidos em 2003 é de 9% para nascidos em 2004 é de 7% e para nascidos em 2005 é de 6% todos taxas maiores do que do estado.
        - **Taxa de Evasão Escolar**: A taxa de abandono escolar tende a ser mais alta em regiões com baixa renda, como Embu-Guaçu, onde fatores como **trabalho infantil**, **dificuldades financeiras** e **infraestrutura escolar precária** contribuem para a evasão.

        #### **Falta de Acesso a Educação de Qualidade**

        - Embora existam escolas públicas, há **falta de recursos**, **professores qualificados** e **materiais didáticos** adequados. Isso reflete uma defasagem na qualidade do ensino oferecido à população local.

        #### **Capacidade de Inclusão Educacional**

        - A inclusão de crianças com **deficiência física ou mental** também enfrenta desafios em Embu-Guaçu.

        '''
        st.markdown(vulnerabilidade_embu_guacu, unsafe_allow_html=True)
        # dados do ideb 
        df_ideb = data_loader.load_data_ideb('')
        # Filtra o DataFrame
        mask = (df_ideb['rede'] == 'Municipal') & (df_ideb['6_ao_9_ano'] == True)
        df_ideb_infantil_municipal = df_ideb[mask]

        # Valores de referência para a linha horizontal
        embu_guacu_2017 = 4.9
        embu_guacu_2019 = 4.6
        embu_guacu_2021 = 4.9
        embu_guacu_2023 = 4.7

        # Criação dos Box Plots com Plotly Express
        fig1 = px.box(df_ideb_infantil_municipal, y='ideb_2017', title='IDEB 2017')
        fig1.add_hline(y=embu_guacu_2017, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2017}')

        fig2 = px.box(df_ideb_infantil_municipal, y='ideb_2019', title='IDEB 2019')
        fig2.add_hline(y=embu_guacu_2019, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2019}')

        fig3 = px.box(df_ideb_infantil_municipal, y='ideb_2021', title='IDEB 2021')
        fig3.add_hline(y=embu_guacu_2021, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2021}')

        fig4 = px.box(df_ideb_infantil_municipal, y='ideb_2023', title='IDEB 2023')
        fig4.add_hline(y=embu_guacu_2023, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2023}')

        # Título geral
        st.title('IDEB dados dos municipios do estado de São Paulo ')
        st.markdown(' ### <span style="color: yellow; font-weight: bold;">Ensino infantil final (6º ao 9º ano)</span> dos municípios em comparação com a rede municipal de Embu-Guaçu ', unsafe_allow_html=True)

        # Exibe os gráficos no Streamlit em um layout de grid
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)
        with col3:
            st.plotly_chart(fig3, use_container_width=True)
        with col4:
            st.plotly_chart(fig4, use_container_width=True)

        mask = (df_ideb['rede'] == 'Municipal') & (df_ideb['1_ao_5_ano'] == True)
        df_ideb_infantil_final_municipal = df_ideb[mask]
        # Valores de referência para a linha horizontal
        embu_guacu_infantil_inicial_2017 = 6.1
        embu_guacu_infantil_inicial_2019 = 5.7
        embu_guacu_infantil_inicial_2021 = 5.5
        embu_guacu_infantil_inicial_2023 = 5.9

        # Criação dos Box Plots com Plotly Express
        fig1 = px.box(df_ideb_infantil_final_municipal, y='ideb_2017', title='IDEB 2017')
        fig1.add_hline(y=embu_guacu_infantil_inicial_2017, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2017}')

        fig2 = px.box(df_ideb_infantil_final_municipal, y='ideb_2019', title='IDEB 2019')
        fig2.add_hline(y=embu_guacu_infantil_inicial_2019, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2019}')

        fig3 = px.box(df_ideb_infantil_final_municipal, y='ideb_2021', title='IDEB 2021')
        fig3.add_hline(y=embu_guacu_infantil_inicial_2021, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2021}')

        fig4 = px.box(df_ideb_infantil_final_municipal, y='ideb_2023', title='IDEB 2023')
        fig4.add_hline(y=embu_guacu_infantil_inicial_2023, line_dash="dash", line_color="red", annotation_text=f'Embu-Guaçu: {embu_guacu_2023}')


        # Título geral
        st.title('IDEB dados dos municipios do estado de São Paulo ')
        st.markdown(' ### <span style="color: yellow; font-weight: bold;">Ensino inicial infantil (1° ao 5°ano)</span> dos municípios em comparação com a rede municipal de Embu-Guaçu ',  unsafe_allow_html=True)

        # Exibe os gráficos no Streamlit em um layout de grid
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)
        with col3:
            st.plotly_chart(fig3, use_container_width=True)
        with col4:
            st.plotly_chart(fig4, use_container_width=True)

        # Título principal
        st.title("Transformando Vidas: O Impacto da ONG Passos Magicos em Embu-Guaçu")

        # --- 1. Objetivo do Storytelling ---
        st.header("1. O Propósito")
        st.markdown("""
        A Passos Mágicos é uma instituição sem fins lucrativos dedicada a fornecer educação de qualidade e transformar vidas através da educação.
        Fundada em 1992, expandimos nosso alcance para atender crianças e jovens em situação de vulnerabilidade em Embu-Guaçu, SP.
        Nosso objetivo é demonstrar o quanto impactamos socialmente, no psicológico e pedagógico os nos alunos que atendemos.
        Queremos mostrar como transformamos vidas, contribuímos para a comunidade e engajamos nossos apoiadores com uma mensagem clara e inspiradora.
        """)

        # --- 2. Organização dos Dados ---
        st.header("2. Pilares do Impacto")
        st.markdown("""
        Organizamos nossos dados em três pilares principais:
        """)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Desempenho Social")
            st.markdown("""
            * Participação em atividades comunitárias
            * Melhoria nas relações interpessoais
            * Engajamento em projetos sociais
            """)
        with col2:
            st.subheader("Desempenho Psicossocial")
            st.markdown("""
            * Níveis de autoestima e motivação
            * Bem-estar emocional
            * Redução da evasão escolar
            * Superação de traumas
            """)
        with col3:
            st.subheader("Desempenho Pedagógico")
            st.markdown("""
            * Notas escolares
            * Taxa de aprovação
            * Prêmios acadêmicos
            * Progresso em disciplinas específicas
            """)

        # --- 3. Personas e Histórias Individuais ---
        st.header("3. Histórias que Inspiram")
        st.markdown("""
        Conheça alguns alunos cujas histórias ilustram o impacto da nossa ONG:
        """)

        # Exemplo de dados - Substitua com seus dados reais
        data_personas = {
            "Nome": ["Élida Coelho da Silva", "Sábrina Novais"],
            "História": [
                "Sou profundamente grata                                         \
                por essa chance, pois                                 \
                sempre foi um sonho realizar                                 \
                um curso ligado às exatas.                                 \
                Originária de uma família humilde, concluir os 5 anos desse curso                      \
                tão relevante para a sociedade parecia                      \
                um desafio inalcançável. Acredito que a                      \
                formação vai além do diploma, ele                      \
                transforma nossa visão de mundo e abre                      \
                portas para novas oportunidades,                      \
                sonhos e perspectivas de vida.",                                 
                "Eu participei de um programa chamado                         \
                    Vem Ser. Eu tinha aulas de português,          \
                    matemática e inglês, Eu no Comando, em          \
                    que a gente teve a oportunidade de          \
                    entrevistar diversos profissionais de diversas áreas. […] Hoje eu sou universitária da Passos Mágicos \
                    na UNISA pra estudar o curso que eu sempre quis.”"          
            ],
            "Foto": [
                "assets/elida.png", # Substitua com as fotos reais
                 "assets/sabrina.png"
            ], 
            "Resultados": [
                "Aluna Passos Mágicos e formada na  \
                    Estácio de Sá em Engenharia Civil.",
                "Aluna Passos Mágicos e universitária 2024 na UNISA."
            ]
        }

        df_personas = pd.DataFrame(data_personas)

        for index, row in df_personas.iterrows():
            col1, col2 = st.columns(2)
            with col1:
                st.image(row['Foto'], caption=row['Nome'], width=300)
            with col2:
                st.subheader(row['Nome'])
                st.write(f"**História:** {row['História']}")
                st.write(f"**Resultados:** {row['Resultados']}")

        # --- 4. Construção da Narrativa ---
        st.header("4. Nossa Jornada: Desafio, Solução e Impacto")
        st.markdown("""
        Estruturamos nosso storytelling em três atos:
        """)

        # Ato 1 - O desafio
        st.subheader("Ato 1 - O Desafio")
        st.markdown("""
        Na comunidade mais carente de Embu-Guaçu, onde a falta de assistência e as altas taxas de jovens que não concluem o ensino médio
                     devido à escassez de recursos e suporte são uma realidade, foi nesse cenário que a organização Passos entrou para transformar a vida das pessoas.
        """)


         # --- 2 Nossa solução ---
        st.subheader("Ato 2 - A nossa solução impacta na evolução de Notas")
        st.markdown(
            """
        Após a realização de provas diagnósticas no início e fim do ano, observamos uma evolução média de 77% nas notas dos alunos.
        """
        )
        # Evolução das notas por fase
        data_notas = {
            "Fase": [
                "Alfa",
                "Fase 1",
                "Fase 2",
                "Fase 3",
                "Fase 4",
                "Fase 5",
                "Fase 6",
                "Fase 7",
                "Média Geral",
            ],
            "Evolução": [57, 124, 75, 92, 64, 76, 47, 78, 77],
        }
        df_notas = pd.DataFrame(data_notas)
        fig_notas = px.bar(
            df_notas, x="Fase", y="Evolução", labels={"Evolução": "% de Evolução"}
        )
        st.plotly_chart(fig_notas, use_container_width=True)
        # Ato 3 - O impacto
        st.subheader("Ato 3 - O Impacto com a metodologia Passos Mágicos")
        st.markdown("""
        Após o programa, observamos que os alunos aumentaram suas notas em matemática, português e passaram a participar de atividades comunitárias.
        """)
        st.markdown(
            """
        Nosso Programa de Aceleração do Conhecimento (PAC) é central em nossa metodologia, com foco na individualidade de cada estudante.
        Formamos turmas por proficiência, oferecendo aulas de alfabetização, português, matemática e inglês.
        O PAC inclui apoio psicológico, psicopedagógico, suporte sociofamiliar, ampliação da visão de mundo, bolsas de estudo e encaminhamento profissional.
        """
        )

        # Dados do PAC
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""<h3 style='text-align: center;'>+ 11.500 h</h3> <h4 style='text-align: center;'>de aulas no PAC</h4>""",
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f"""<h3 style='text-align: center;'>118</h3> <h4 style='text-align: center;'>crianças alfabetizadas fora da idade</h4>""",
                unsafe_allow_html=True,
            )

        st.subheader("Crescimento do PAC desde 2016")
        data_crescimento = {
            "Ano": [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
            "Alunos": [70, 300, 550, 812, 841, 824, 970, 1100],
        }
        df_crescimento = pd.DataFrame(data_crescimento)
        fig_crescimento = px.line(
            df_crescimento,
            x="Ano",
            y="Alunos",
            markers=True,
            labels={"Alunos": "Número de Alunos"},
        )
        st.plotly_chart(fig_crescimento, use_container_width=True)
        st.markdown("---")

        # --- 5. Visualização dos Dados ---
        st.header("5. Visualizando o Nosso Progresso")
        st.markdown("""
        Utilizamos gráficos para tornar nossos dados mais compreensíveis:
        """)

        st.markdown(
            """
        A Passos Mágicos tem o compromisso de atender à comunidade de Embu-Guaçu, beneficiando 1.100 indivíduos, o que equivale a cerca de 9.8% dos estudantes da rede pública e 1.8% da população local.
        """
        )
        col1, col2 = st.columns(2)
        with col1:
            # Gráfico de etnias
            st.subheader("Alunos por Etnia")
            data_etnias = {
                "Etnias": ["Brancos", "Pardos", "Pretos", "Amarelos"],
                "Porcentagem": [47.4, 41.4, 10, 1.3],
            }
            df_etnias = pd.DataFrame(data_etnias)
            fig_etnias = px.bar(
                df_etnias,
                x="Etnias",
                y="Porcentagem",
                labels={"Porcentagem": "% de Alunos"},
            )
            st.plotly_chart(fig_etnias, use_container_width=True)

        with col2:
            # Gráfico de faixa etária
            st.subheader("Alunos por Faixa Etária")
            data_idade = {
                "Faixa Etária": [
                    "7 a 10 anos",
                    "11 a 14 anos",
                    "15 a 18 anos",
                    "19 a 21 anos",
                ],
                "Porcentagem": [37.2, 44.5, 17.7, 0.5],
            }
            df_idade = pd.DataFrame(data_idade)
            fig_idade = px.bar(
                df_idade,
                x="Faixa Etária",
                y="Porcentagem",
                labels={"Porcentagem": "% de Alunos"},
            )
            st.plotly_chart(fig_idade, use_container_width=True)

        # Gênero
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""<h3 style='text-align: center;'>👧 Meninas</h3> <h2 style='text-align: center;'>53.4%</h2>""",
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f"""<h3 style='text-align: center;'>👦 Meninos</h3> <h2 style='text-align: center;'>46.6%</h2>""",
                unsafe_allow_html=True,
            )
        st.markdown("---")
                # --- 6. Vem ser dados ---

        st.subheader("6. Vem Ser")
        st.markdown(
            """
            Programa para apoiar nossos alunos no vestibular, com aulas, acompanhamento psicológico e simulados.
            """
        )
        st.markdown(
            f"""<h3 style='text-align: center;'>12</h3> <h4 style='text-align: center;'>alunos do Vem Ser 2023 foram aprovados em faculdades</h4>""",
            unsafe_allow_html=True,
        )

        # Gráfico de universitários por ano
        data_universitarios = {
            "Ano": [2018, 2019, 2020, 2021, 2022, 2023],
            "Universitários": [1, 2, 26, 51, 71, 94],
            "Vem Ser": [None, None, None, 12, 59, 71],
        }
        df_universitarios = pd.DataFrame(data_universitarios)
        fig_universitarios = px.line(
            df_universitarios,
            x="Ano",
            y=["Universitários", "Vem Ser"],
            markers=True,
            labels={"value": "Número de Universitários"},
        )
        st.plotly_chart(fig_universitarios, use_container_width=True)

        st.markdown("---")
        # --- 7. Ingresso no mercado de trabalho ---
        st.header("7. Ingresso no Mercado de Trabalho")
        st.markdown(
            """
            Estabelecemos conexões entre nossos alunos e oportunidades de emprego.
            """
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""<h3 style='text-align: center;'>38</h3> <h4 style='text-align: center;'>alunos no mercado de trabalho</h4>""",
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f"""<h3 style='text-align: center;'>+45%</h3> <h4 style='text-align: center;'>aumento na renda familiar nos primeiros salários</h4>""",
                unsafe_allow_html=True,
            )

        # Gráfico de vínculo empregatício
        data_vinculo = {
            "Vínculo": [
                "Estágio",
                "CLT",
                "Pessoa Jurídica",
                "Autônomo",
                "Empregado Doméstico",
            ],
            "Porcentagem": [47.4, 44.7, 5.3, 2.6, 0],
        }
        df_vinculo = pd.DataFrame(data_vinculo)
        fig_vinculo = px.bar(
            df_vinculo,
            x="Vínculo",
            y="Porcentagem",
            labels={"Porcentagem": "% de Alunos"},
        )
        st.plotly_chart(fig_vinculo, use_container_width=True)
        st.markdown("---")
       
        # --- 5. Fechamento Inspirador ---
        st.header("6. O Futuro que Queremos Construir")
        st.markdown("""
        Imagine o impacto que podemos alcançar juntos se mais jovens tiverem essa oportunidade! Com o seu apoio contínuo, podemos transformar mais vidas e comunidades.
        """)






