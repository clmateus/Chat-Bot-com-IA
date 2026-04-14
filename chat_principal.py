from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, YoutubeLoader
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('api_key')
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

mensagens = []

def resposta_bot(mensagem, documento):
    mensagens_modelo = [('system', 'Você é um assistente amigável chamado MateusBot e tem as seguintes informações para formular respostas: {informacoes}')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(
        mensagens_modelo
    )
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content

def carrega_site():
    url_site = input('Digite a URL do site: ')
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()

    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_pdf():
    path_pdf = 'pdfs/a_republica.pdf'
    loader = PyPDFLoader.load(path_pdf)
    lista_documentos = loader.load()

    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_video_youtube():
    url_video = input('Digite a URL do vídeo do youtube: ')
    loader = YoutubeLoader.from_youtube_url(url_video, language=['pt'])
    lista_documentos = loader.load()
    
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

while True:
    selecao = input('''
    Digite 1 para conversar com um site
    Digite 2 para conversar com um PDF
    Digite 3 para conversar com um vídeo do YouTube
''')

    if selecao == '1':
        documento = carrega_site()
        break
    if selecao == '2':
        documento = carrega_pdf()
        break
    if selecao == '3':
        documento = carrega_video_youtube()
        break
    
    print('Opção inválida, digite um valor entre 1 e 3.')

while True:
    pergunta = input('Pergunte algo: ')

    if pergunta.lower() == 'x':
        break

    mensagens.append(('user', pergunta))

    resposta = resposta_bot(mensagens, documento)

    mensagens.append(('assistant', resposta))

    print(f'MateusBot: {resposta}')

print('Muito obrigado por usar o MateusBot')