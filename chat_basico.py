from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv
import os

# Chave API
load_dotenv()
api_key = os.environ.get('api_key')
os.environ['GROQ_API_KEY'] = api_key

# Define o modelo de IA
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Lista para armazenar as conversas com a IA
mensagens = []

# Função que recebe a lista com as conversas e retorna a resposta da IA
def resposta_bot(mensagem):
    # Define o comportamento da IA
    mensagens_modelo = [('system', 'Você é um assistente amigável chamado MateusBot')]
    # Junta o comportamento da IA com as entradas do usuário
    mensagens_modelo += mensagens
    # Define o template da IA
    template = ChatPromptTemplate.from_messages(
        mensagens_modelo
    )
    # Define a cadeia de respostas
    chain = template | chat
    # Retorna somente o conteúdo da resposta da IA
    return chain.invoke({}).content

# Loop para registrar X entradas do usuário
while True:
    # Recebe a entrada do usuário
    pergunta = input('Pergunte algo: ')

    # Se o usuário digitar 'x' o programa encerra
    if pergunta.lower() == 'x':
        break

    # Insere a entrada do usuário na lista de mensagens
    mensagens.append(('user', pergunta))

    # Recebe a resposta da IA
    resposta = resposta_bot(mensagens)

    # Insere a resposta da IA na lista de mensagens
    mensagens.append(('assistant', resposta))

    # Imprime no console a resposta da IA
    print(f'MateusBot: {resposta}')

print('Muito obrigado por usar o MateusBot')