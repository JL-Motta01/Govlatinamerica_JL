from io import DEFAULT_BUFFER_SIZE
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

def download_sitemap_xml():
    url1 = "https://www.gov.br/sitemap.xml"
    url2 = "https://www.gov.br/planalto/sitemap.xml"
    wget.download(url1, f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap/map_noticias.xml")
    wget.download(url2, f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap/map_planalto.xml")

def mapa_do_site (url):
    """Analisa o mapa do site a partir do link"""
    response = urllib.request.urlopen(url)
    xml = BeautifulSoup(response, 'lxml-xml', from_encoding = response.info().get_param("charset"))
    return xml

def mapa_do_site_2 (url):
    """Analisa o mapa do site a partir do arquivo xml baixado"""
    conteudo = BeautifulSoup(open(url, 'r'), 'lxml')
    return conteudo

def download_pagina (url_pg,titulo):
    mypath = f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/arquivos/html_noticia"
    filename = ( titulo + ".html")
    fullfilename = os.path.join(mypath, filename)
    urllib.request.urlretrieve(url_pg, fullfilename)



def parse_mapa (xml):
    lista_de_titulos = xml.find_all("news:title")
    lista_de_links = xml.find_all("loc")
    lista_de_datas = xml.find_all("news:publication_date") 
    lista_geral = []
    for titulo,link,data in zip (lista_de_titulos, lista_de_links, lista_de_datas):
        lista_tmp = [] 
        lista_tmp.append(link.text)
        lista_tmp.append(data.text)
        lista_tmp.append("NA")
        lista_tmp.append("NA")
        lista_tmp.append("NA")
        lista_tmp.append(titulo.text)
        lista_tmp.append("NA")
        lista_geral.append(lista_tmp)
    return lista_geral
    

def base_dados(xml):
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db.json", ensure_ascii=False)
    User = Query()
    lista_geral = parse_mapa(xml)
    for sublista in lista_geral:
        db_planalto = db.contains(User.titulo==sublista[5])
        if not db_planalto:
            print(f"não está na base:{sublista[5]}")
            db.insert({
                "link": sublista[0],
                "data":sublista[1],
                "atualizado em": sublista[2],
                "categoria": sublista[3],
                "tags": sublista[4],
                "titulo": sublista[5],
                "conteudo": sublista[6],
            })
            link_news = sublista[0]
            lista_update = extracao_conteudo(link_news)
            if db.search(User.conteudo == "NA"):
                db.update({"atualizado em":lista_update[0]})
                db.update({"conteudo":lista_update[1]})
                db.update({"categoria":lista_update[2]})
                db.update({"tags":lista_update[3]})
        if db_planalto:
            link_news = sublista[0]
            lista_update = extracao_conteudo(link_news)
            print(f"está na base:{sublista[5]}")
            if db.search(User.conteudo == "NA"):
                db.update({"atualizado em":lista_update[0]})
                db.update({"conteudo":lista_update[1]})
                db.update({"categoria":lista_update[2]})
                db.update({"tags":lista_update[3]})

def extracao_conteudo(link):
    lista_update = []
    response = urllib.request.urlopen(link)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))

    try:
        lista_att = html.find('span', class_='documentModified').find('span', class_='value').get_text()
    except:
        lista_att = "notícia não modificada"

    try:
        lista_conteudo = []
        linhas = html.find('div', {'id' : 'content-core'}).find_all(['p','h3'])
        for conteudo in linhas:
            if conteudo.name == 'h3':
                texto = conteudo.text
                texto = texto.upper()
            else:
                texto = conteudo.text 
            lista_conteudo.append(texto)
    except:
        lista_conteudo= "notícia sem conteúdo"

    try:
        lista_categoria = html.find('span', {'id' : 'form-widgets-categoria'}).find('a').get_text()
    except:
        lista_categoria= "notícia sem categoria"

    try:
        lista_tag = []
        for spt in html.find('div', {'id' : 'category'}).find_all('span'):
            tag = spt.text
            lista_tag.append(tag)
    except:
        lista_tag= "notícia sem tags"

    lista_update = [lista_att,lista_conteudo,lista_categoria,lista_tag]
    return lista_update

def main ():
    if not os.path.exists(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap/map_noticias.xml"):
        download_sitemap_xml()
    url_site = [f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap/map_noticias.xml",f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap/map_planalto.xml"]
    for url in url_site:
        xml = mapa_do_site_2(url)
        base_dados(xml)

if __name__ == "__main__":
    main()