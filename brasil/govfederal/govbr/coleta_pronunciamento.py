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

def acessar_pagina(url):
    """Analisa os pronunciamentos do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_pronunciamentos ():
    """Percorre as páginas onde fical os links"""
    lista_url_pronunciamentos = []
    contador = 0
    while contador<30:
        dominio = "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/pronunciamentos?b_start:int="
        dominio += str(contador)
        contador += 30
        lista_url_pronunciamentos.append(dominio)
    return lista_url_pronunciamentos

def coleta_link():
    """Coleta os links de cada página que contém pronunciamentos"""
    lista_links=[]
    for url in paginas_com_url_pronunciamentos():
        html = acessar_pagina(url)
        pronunciamentos = html.find_all("article", class_=["tileItem visualIEFloatFix tile-document","tileItem visualIEFloatFix tile-collective-nitf-content"] )
        for articles in pronunciamentos:
            links = articles.a["href"]
            lista_links.append(links)
    return lista_links

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos pronunciamentos"""
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_pronunciamento.json")
    User = Query()
    for link in coleta_link():
        pronunciamentos = acessar_pagina(link)
        url = link
        publicado_em = pronunciamentos.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            atualizado_em = pronunciamentos.find("span", class_="documentModified").find("span", class_="value").text
        except:
           atualizado_em = "pronunciamento não modificado"
        try:
            lista_tags=[]
            spans=pronunciamentos.find("div", {"id" : "category"}).find_all("span") 
            for span in spans:
                tag = span.text
                lista_tags.append(tag)
        except:
            lista_tags="não possui tags"
        titulo = pronunciamentos.find("h1", class_="documentFirstHeading").text
        try:
            lista_conteudo=[]
            paragrafos = pronunciamentos.find('div', {'id' : 'content-core'}).find_all(['p','h3','h2','h1'])
            for conteudo in paragrafos:
                if conteudo.name == 'h3' or conteudo.name == 'h2' or conteudo.name == 'h1':
                    texto = conteudo.text
                    texto = texto.upper()
                else:
                    texto = conteudo.text 
                lista_conteudo.append(texto)
        except:
            lista_conteudo= "notícia sem conteúdo"
        db_planalto = db.contains(User.titulo==titulo,User.data==publicado_em)
        if not db_planalto:
            print("não está na base")
            db.insert({
                "link":url,
                "data":publicado_em,
                "atualizado em":atualizado_em,           
                "tags":lista_tags,
                "titulo":titulo,
                "conteudo":lista_conteudo,
            })
        else:
            print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()