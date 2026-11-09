import streamlit as st
from google import genai
from google.genai import types

# Configuração da página do aplicativo para celular
st.set_page_config(page_title="J.A.R.V.I.S.", page_icon="🤖")
st.title("🤖 J.A.R.V.I.S. OS")

# Caixa para colocar a chave API com segurança na tela
api_key = st.sidebar.text_input("AQ.Ab8RN6IAuEBbXfgA7nleGit76obiKjSbTuZtW8iFquU-mGECGw", type="password")

instrucoes_do_sistema = """
Você é o J.A.R.V.I.S., o assistente virtual ultra-inteligente criado por Tony Stark.
Você deve agir de forma extremamente leal, inteligente, levemente sarcástica e analítica.
Sempre chame o usuário de 'Senhor' ou 'Senhora'. 
Use termos técnicos quando apropriado e seja direto nas respostas.
"""

if api_key:
    client = genai.Client(api_key=api_key)
    
    # Inicializa o histórico do chat se não existir
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostra as mensagens anteriores na tela
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Entrada do usuário (barra de mensagem igual WhatsApp)
    if prompt := st.chat_input("O que deseja, Senhor?"):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Resposta do Jarvis
        with st.chat_message("assistant"):
            with st.spinner("Processando..."):
                resposta = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=instrucoes_do_sistema,
                        temperature=0.7,
                    )
                )
                st.write(resposta.text)
        st.session_state.messages.append({"role": "assistant", "content": resposta.text})
else:
    st.warning("Por favor, insira sua chave API na barra lateral para inicializar o J.A.R.V.I.S.")
