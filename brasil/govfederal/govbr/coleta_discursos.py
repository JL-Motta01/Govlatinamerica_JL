from io import DEFAULT_BUFFER_SIZE
from urllib import parse
from urllib.request import urlopen
import urllib
import urllib.request #realizar requisição da página html
import os #para especificar o caminho do download
import wget
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

def paginas_com_url_discursos ():
    """Percorre as páginas onde fical os links"""
    lista_url_discursos = []
    contador = 0
    while contador<421:
        dominio = "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int="
        dominio += str(contador)
        contador += 30
        lista_url_discursos.append(dominio)
    return lista_url_discursos

def coleta_link_discursos ():
    """Coleta os links de cada página que contém discursos"""
    lista_links=[]
    for url in paginas_com_url_discursos():
        html = acessar_pagina(url)
        discursos = html.find_all("article", class_= "tileItem visualIEFloatFix tile-document")
        for articles in discursos:
            links = articles.a["href"]
            lista_links.append(links)
    return lista_links

def coleta_conteudo_discursos ():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos discursos"""
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_discursos.json", ensure_ascii=False)
    User = Query()
    for link in coleta_link_discursos():
        discursos = acessar_pagina(link)
        url = link
        publicado_em = discursos.find("span", class_="documentPublished").find("span", class_="value").text.split(" ")
        try:
            atualizado_em = discursos.find("span", class_="documentModified").find("span", class_="value").text
        except:
           atualizado_em = "NA"
        try:
            lista_tags=[]
            spans=discursos.find("div", {"id" : "category"}).find_all("span") 
            for span in spans:
                tag = span.text
                lista_tags.append(tag)
        except:
            lista_tags="NA"
        titulo = discursos.find("h1", class_="documentFirstHeading").text
        try:
            lista_conteudo=[]
            paragrafos = discursos.find('div', {'id' : 'content-core'}).find_all(['p','h3','h2','h1'])
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
            subtitulo = discursos.find("a", class_="nitfSubtitle").text
        except:
            subtitulo="NA"
        db_planalto = db.contains(User.titulo==titulo)
        if not db_planalto:
            print("não está na base")
            db.insert({
                "origem": "Presidência da República",
                "classificado": "discurso",
                "data":publicado_em[0],
                "horario":publicado_em[1],
                "atualizado em":atualizado_em,
                "titulo":titulo,
                "subtitulo":subtitulo,
                "autor": "Jair Messias Bolsonaro",
                "link":url,           
                "tags":lista_tags,
                "conteudo":lista_conteudo,
            })
        else:
            print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo_discursos()

if __name__ == "__main__":
    main()