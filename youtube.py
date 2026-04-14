from langchain_community.document_loaders.parsers import language
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('api_key')
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

url = 'https://www.youtube.com/watch?v=tArMc9-s7Fw'
loader = YoutubeLoader.from_youtube_url(url)

lista_documentos = loader.load()
documento = ''

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado MateusBotque possui as seguintes informações para formular uma resposta: {informacoes}'),
    ('user', '{input}')
])

chain_youtube = template | chat
resposta = chain_youtube.invoke({'informacoes': documento, 'input': 'Sobre o que esse vídeo fala?'})
print(resposta.content)