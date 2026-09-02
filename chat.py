import streamlit as st
from langchain_core.messages import HumanMessage

from modelo_openai import mensagens, modelo


def abrir_chat(prompt, modelo, mensagens):
    if "mensagens" not in st.session_state:
        st.session_state["mensagens"] = list(mensagens)

    mensagens = st.session_state["mensagens"]

    if prompt:
        mensagens.append(HumanMessage(content=prompt))
        try:
            resposta = modelo.invoke(mensagens)
        except Exception:
            st.error("Não foi possível consultar a OpenAI. Verifique sua chave no arquivo .env.")
            return

        mensagens.append(resposta)
        st.session_state["mensagens"] = mensagens

    for mensagem in st.session_state["mensagens"]:
        if mensagem.type == "ai":
            role = "assistant"
        elif mensagem.type == "human":
            role = "user"
        else:
            continue

        with st.chat_message(role):
            st.write(mensagem.content)


def meu_app():
    st.header("VicthorGPT", divider=True)
    st.markdown("#### Converse com o ChatGPT integrado no Streamlit")
    prompt = st.chat_input("Digite a sua mensagem")
    abrir_chat(prompt, modelo, mensagens)


meu_app()