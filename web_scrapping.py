from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('api_key')
os.environ['GROQ_API_KEY'] = api_key

loader = WebBaseLoader('https://www.scrapethissite.com/pages/')
chat = ChatGroq(model='llama-3.3-70b-versatile')

lista_documentos = loader.load()
documento = ''

for doc in lista_documentos:
    documento += doc.page_content

template = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um assistente amigável chamado MateusBot e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}'),
        ('user', '{input}')        
    ]
)

chain = template | chat

resposta = chain.invoke({'documentos_informados': documento, 'input': 'Quais os conteúdos do site?'})

print(resposta.content)