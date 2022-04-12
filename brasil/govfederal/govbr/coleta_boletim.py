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

def acessar_pagina(url):
    """Analisa os boletim do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_boletim ():
    """Percorre as páginas onde fical os links"""
    lista_url_boletim = []
    contador = 0
    while contador<460:
        dominio = "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/notas-comunicados?b_start:int="
        dominio += str(contador)
        contador += 20
        lista_url_boletim.append(dominio)
    return lista_url_boletim

def coleta_link():
    """Coleta os links de cada página que contém boletim"""
    lista_links=[]
    for url in paginas_com_url_boletim():
        html = acessar_pagina(url)
        boletim = html.find_all("article", class_="tileItem visualIEFloatFix tile-file")
        for articles in boletim:
            links = articles.a["href"]
            lista_links.append(links)
    return lista_links

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos boletim"""
    db = TinyDB(f"{DIR_DADOS}/govlatinamerica/brasil/govfederal/govbr/bd/db_boletim.json", ensure_ascii=False)
    User = Query()
    for link in coleta_link():
        boletim = acessar_pagina(link)
        url = link
        publicado_em = boletim.find("span", class_="documentPublished").find("span", class_="value").text.split(" ")
        try:
            subtitulo = boletim.find("a", class_="nitfSubtitle").text
        except:
            subtitulo = "NA"
        try:
            atualizado_em = boletim.find("span", class_="documentModified").find("span", class_="value").text
        except:
           atualizado_em = "boletim não modificado"
        titulo = boletim.find("h1", class_="documentFirstHeading").text
        db_planalto = db.contains((User.titulo==titulo)&(User.data==publicado_em))
        if not db_planalto:
            print("não está na base")
            #wget.download(url[:-5], f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_boletim/")
            link_pdf = requests.get(url[:-5])
            local = f"{DIR_DADOS}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_boletim/"
            with open(f'{local}/{titulo}', "wb") as arq_pdf:
                arq_pdf.write(link_pdf.content)
            # db.insert({
            #     "origem": "Planalto",
            #     "classificado": "Notas e classificados",
            #     "data":publicado_em[0],
            #     "horario":publicado_em[1],
            #     "atualizado em":atualizado_em,
            #     "link":url[:-5],  
            #     "titulo":titulo,
            #     "subtítulo":subtitulo
            # })
        else:
            print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()