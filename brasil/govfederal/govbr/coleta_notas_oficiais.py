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
    """Analisa os notas do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_notas ():
    """Percorre as páginas onde fical os links"""
    lista_url_notas = []
    contador = 0
    while contador<150:
        dominio = "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/notas-oficiais?b_start:int="
        dominio += str(contador)
        contador += 30
        lista_url_notas.append(dominio)
    return lista_url_notas

def coleta_link():
    """Coleta os links de cada página que contém notas"""
    lista_links=[]
    for url in paginas_com_url_notas():
        html = acessar_pagina(url)
        notas = html.find_all("article", class_=["tileItem visualIEFloatFix tile-document","tileItem visualIEFloatFix tile-collective-nitf-content"] )
        for articles in notas:
            links = articles.a["href"]
            lista_links.append(links)
    return lista_links

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos notas"""
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_notas.json", ensure_ascii=False)
    User = Query()
    for link in coleta_link():
        notas = acessar_pagina(link)
        url = link
        publicado_em = notas.find("span", class_="documentPublished").find("span", class_="value").text.split(" ")
        try:
            atualizado_em = notas.find("span", class_="documentModified").find("span", class_="value").text
        except:
           atualizado_em = "NA"
        try:
            lista_tags=[]
            spans=notas.find("div", {"id" : "category"}).find_all("span") 
            for span in spans:
                tag = span.text
                lista_tags.append(tag)
        except:
            lista_tags= "NA"
        titulo = notas.find("h1", class_="documentFirstHeading").text
        try:
            lista_conteudo=[]
            paragrafos = notas.find('div', {'id' : 'content-core'}).find_all(['p','h3','h2','h1'])
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
            subtitulo = notas.find("a", class_="nitfSubtitle").text
        except:
            subtitulo="NA"
        db_planalto = db.contains((User.titulo==titulo)&(User.data==publicado_em))
        if not db_planalto:
            print("não está na base")
            db.insert({
                "origem": "Planalto",
                "classificado": "Notas Oficiais",
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


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()