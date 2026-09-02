# VicthorGPT

Este é um projeto que desenvolvi para transformar o uso da inteligência artificial em uma solução prática: um chatbot simples, funcional e acessível pelo navegador.

Com ele, explorei como integrar a API da OpenAI a uma interface feita com Streamlit e como organizar o histórico de uma conversa usando LangChain. Também incluí cuidados básicos para evitar o uso acidental ou excessivo da API.

## O que este projeto demonstra

- Interface de chat criada com Streamlit
- Integração com um modelo da OpenAI por meio do LangChain
- Configuração de credenciais por variável de ambiente
- Limite de tamanho das mensagens e de requisições por minuto

Este repositório contém o código-fonte para estudo e reprodução local. A chave da OpenAI não está incluída.

## Tecnologias

- Python
- Streamlit
- LangChain
- OpenAI

## Como executar localmente

1. Clone este repositório e entre na pasta do projeto:

   ```powershell
   git clone https://github.com/VicthorAngeli/victhorgpt-streamlit.git
   cd victhorgpt-streamlit
   ```

2. Crie um ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```powershell
   pip install -r requirements.txt
   ```

4. Crie o arquivo `.env` a partir do exemplo:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Abra `.env` e informe sua chave da OpenAI:

   ```text
   OPENAI_API_KEY=sua_chave_aqui
   ```

6. Inicie o chatbot:

   ```powershell
   streamlit run chat.py
   ```

O chatbot aceita mensagens de até 1.000 caracteres e limita cada sessão a 5 requisições por minuto para reduzir o consumo acidental da API.
