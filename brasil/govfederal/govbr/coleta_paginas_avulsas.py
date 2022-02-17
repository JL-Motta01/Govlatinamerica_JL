from io import DEFAULT_BUFFER_SIZE
from urllib import parse
from urllib.request import urlopen
import urllib
import urllib.request #realizar requisição da página html
import os #para especificar o caminho do download
import requests
import csv
from tinydb import TinyDB,Query
from urllib.parse import urlparse #realizar parseamento do html
from bs4 import BeautifulSoup #importa o beautifulsoup para extrair as infos das tags
from pprint import pprint #organizar estéticamente os prints


DIR_LOCAL= "/home/labri_joaomotta/codigo"

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"

def acessar_pagina (url):
    """Analisa os discursos do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_avulsas ():
    """cria uma lista de urls"""
    lista_url= [
        "https://www.gov.br/planalto/pt-br/conheca-a-presidencia/biografia-do-presidente",
        "https://www.gov.br/planalto/pt-br/conheca-a-vice-presidencia/biografia-1",
        "https://www.gov.br/planalto/pt-br/mensagempresidencial/mensagem-do-presidente.pdf/view",
        "https://www.gov.br/planalto/pt-br/mensagempresidencial/2021/mensagem-presidencial-2021.pdf/view"
    ]
    return lista_url

def coleta_avulsa ():
    """Coleta os links de cada página que contém discursos"""
    lista_links= paginas_avulsas()
    count = 0
    for url in lista_links:
        html = acessar_pagina(url)
        if count < 2:
            coleta_conteudo(html,url)
            count = count + 1
        else:
            print(url)
            coleta_pdf(html,url)
            count = count + 1

def coleta_conteudo(pg,numero):
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos discursos"""
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_avulso.json", ensure_ascii=False)
    User = Query()
    pagina = pg
    url = numero
    try:
        publicado_em = pagina.find("span", class_="documentPublished").find("span", class_="value").text.split(" ")
    except:
        publicado_em = ["NA","NA"]
    try:
        atualizado_em = pagina.find("span", class_="documentModified").find("span", class_="value").text
    except:
        atualizado_em = "NA"
    try:
        lista_tags=[]
        spans=pagina.find("div", {"id" : "category"}).find_all("span") 
        for span in spans:
            tag = span.text
            lista_tags.append(tag)
    except:
        lista_tags="não possui tags"
    try:
        titulo = pagina.find("h1", class_="documentFirstHeading").text
    except:
        titulo = pagina.find("span", {"id":"breadcrumbs-current"}).text
    try:
        lista_conteudo=[]
        paragrafos = pagina.find('div', {'id' : 'content'}).find_all(['p','h3','h2','h1'])
        for conteudo in paragrafos:
            if conteudo.name == 'h3' or conteudo.name == 'h2' or conteudo.name == 'h1':
                texto = conteudo.text
                texto = texto.upper()
            else:
                texto = conteudo.text 
            lista_conteudo.append(texto)
    except:
        lista_conteudo= "NA"
    try:
        subtitulo = pagina.find("a", class_="nitfSubtitle").text
    except:
        subtitulo="NA"
    db_planalto = db.contains(User.titulo==titulo)
    if not db_planalto:
        print("não está na base")
        db.insert({
            "origem": "Planalto",
            "classificado": "Páginas avulsas",
            "data":publicado_em[0],
            "horario":publicado_em[1],
            "atualizado em":atualizado_em,
            "titulo":titulo,
            "subtitulo":subtitulo,
            "link":url,           
            "tags":lista_tags,
            "conteudo":lista_conteudo,
        })
    else:
        print("está na base")

def coleta_pdf(link,numero):
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_avulso.json")
    User = Query()
    pdf = link
    url = numero
    try:
        publicado_em = pdf.find("span", class_="documentPublished").find("span", class_="value").text.split(" ")
    except:
        publicado_em = "sem data de publicação"
    try:
        atualizado_em = pdf.find("span", class_="documentModified").find("span", class_="value").text
    except:
        atualizado_em = "pdf não modificado"
    titulo = pdf.find("h1", class_="documentFirstHeading").text
    try:
        subtitulo = pdf.find("a", class_="nitfSubtitle").text
    except:
        subtitulo="NA"
    db_planalto = db.contains((User.titulo==titulo)&(User.data==publicado_em))
    if not db_planalto:
        print("não está na base")
        #wget.download(url[:-5], f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_avulso/")
        link_pdf = requests.get(url[:-5])
        local = f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_avulso/"
        with open(f'{local}/{titulo}', "wb") as arq_pdf:
            arq_pdf.write(link_pdf.content)
        # db.insert({
        #     "origem": "Planalto",
        #     "classificado": "PDFs avulsos",
        #     "data":publicado_em[0],
        #     "horario":publicado_em[1],
        #     "atualizado em":atualizado_em,  
        #     "titulo":titulo,
        #     "subtitulo":subtitulo,
        #     "link":url[:-5]
        # })
    else:
        print("está na base")


def main ():
    """Função principal"""
    coleta_avulsa()

if __name__ == "__main__":
    main()