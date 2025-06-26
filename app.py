import streamlit as st
import json
from backend.ollama_client import OllamaClient
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Assistente de Estudo",
    page_icon="📚",
    layout="wide"
)

# Inicialização do cliente Ollama
@st.cache_resource
def get_ollama_client():
    return OllamaClient()

client = get_ollama_client()

# Título e descrição
st.title("📚 Assistente de Estudo")
st.markdown("""
Este assistente utiliza IA para ajudá-lo nos estudos, ao oferecer:
- Respostas para perguntas específicas
- Resumos da matéria
- Planos de estudo personalizados
""")

# Sidebar para configurações
with st.sidebar:
    st.header("⚙️ Configurações")
    model = st.selectbox(
        "Modelo",
        ["llama2", "mistral"],
        index=0
    )
    client.set_model(model)
    
    st.markdown("---")
    st.markdown("### 📝 Como utilizar")
    st.markdown("""
    1. Escolha uma funcionalidade no menu acima
    2. Siga as instruções específicas de cada secção
    3. Aguarde pela resposta do assistente
    """)

# Funcionalidades principais
tab1, tab2, tab3 = st.tabs(["📝 Perguntas", "📚 Resumos", "📋 Plano de Estudos"])

with tab1:
    st.header("Faça perguntas")
    question = st.text_area("Digite a sua pergunta:", height=100)
    context = st.text_area("Forneça o contexto (opcional):", height=150)
    
    if st.button("Obter Resposta", key="answer"):
        if question:
            with st.spinner("A gerar resposta..."):
                response = client.answer_question(question, context)
                st.markdown("### Resposta:")
                st.write(response)
        else:
            st.warning("Por favor, digite uma pergunta.")

with tab2:
    st.header("Gere resumos")
    text = st.text_area("Cole o texto para resumir:", height=200)
    
    if st.button("Gerar Resumo", key="summary"):
        if text:
            with st.spinner("A gerar resumo..."):
                summary = client.generate_summary(text)
                st.markdown("### Resumo:")
                st.write(summary)
        else:
            st.warning("Por favor, cole um texto para resumir.")

with tab3:
    st.header("Plano de Estudos")
    topic = st.text_input("Digite o tópico de estudo:")
    
    if st.button("Gerar Plano", key="plan"):
        if topic:
            with st.spinner("A gerar plano de estudos..."):
                plan = client.generate_study_plan(topic)
                
                # Exibição do plano
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Conceitos Principais")
                    for concept in plan["main_concepts"]:
                        st.markdown(f"- {concept}")
                    
                    st.subheader("Tópicos")
                    for topic in plan["topics"]:
                        st.markdown(f"- {topic}")
                
                with col2:
                    st.subheader("Exercícios Sugeridos")
                    for exercise in plan["exercises"]:
                        st.markdown(f"- {exercise}")
                    
                    st.subheader("Recursos")
                    for resource in plan["resources"]:
                        st.markdown(f"- {resource}")
                
                # Visualização do progresso sugerido
                st.subheader("Progresso Sugerido")
                fig = go.Figure(data=[
                    go.Bar(
                        x=["Conceitos", "Tópicos", "Exercícios"],
                        y=[len(plan["main_concepts"]), len(plan["topics"]), len(plan["exercises"])],
                        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c']
                    )
                ])
                fig.update_layout(
                    title="Distribuição do Plano de Estudos",
                    xaxis_title="Categoria",
                    yaxis_title="Quantidade de Itens"
                )
                st.plotly_chart(fig)
        else:
            st.warning("Por favor, digite um tópico de estudo.")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com ❤️ através de Ollama e Streamlit") 