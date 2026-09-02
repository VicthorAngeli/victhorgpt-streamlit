# VicthorGPT

Chatbot simples construído com Streamlit, LangChain e a API da OpenAI.

## Tecnologias

- Python
- Streamlit
- LangChain
- OpenAI

## Como executar localmente

1. Clone este repositório e entre na pasta do projeto.
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

O chatbot aceita mensagens de até 1.000 caracteres e limita cada sessão a 5 requisições por minuto para reduzir consumo acidental da API.

## Segurança

Nunca publique sua chave da OpenAI, o arquivo `.env` ou a pasta `.venv`. O arquivo `.env.example` é apenas um modelo e não contém credenciais.

Se uma chave for exposta, revogue-a imediatamente no painel da OpenAI e crie outra.