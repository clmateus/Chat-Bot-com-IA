from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('api_key')
os.environ['GROQ_API_KEY'] = api_key

caminho = './pdfs/a_republica.pdf'

loader = PyPDFLoader(caminho)
chat = ChatGroq(model='llama-3.3-70b-versatile')

lista_documentos = loader.load()
documento = ''

for doc in lista_documentos:
    documento += doc.page_content

template = ChatPromptTemplate.from_messages({
    ('system', 'Você é um assistente amigável chamado MateusBot e tem as seguintes informações para formular respostas: {informacoes}'),
    ('user', '{input}')
})

chain_pdf = template | chat

resposta = chain_pdf.invoke({'informacoes': documento, 'input': 'Faça um breve resumo do PDF apresentado.'})

print(resposta.content)