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
from requests.models import DecodeError 

def download_sitemap_xml():
    url = "https://www.gov.br/sitemap.xml"
    wget.download(url)

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
    mypath = "/home/labri_joaomotta/codigo/govlatinamerica/brasil/govfederal/govbr/arquivos/html_noticia"
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
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/db.json")
    User = Query()
    lista_geral = parse_mapa(xml)
    for sublista in lista_geral:
        db_planalto = db.contains(User.titulo==sublista[0])
        if not db_planalto:
            print("não está na base")
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
            print("está na base")
            if db.search(User.conteudo == "NA"):
                db.update({"conteudo":lista_update[1]})
        if db_planalto:
            link_news = sublista[0]
            lista_update = extracao_conteudo(link_news)
            print("está na base")
            if db.search(User.conteudo == "NA"):
                db.update({"conteudo":lista_update[1]})

def extracao_conteudo(xml):
    lista_update = []
    link = base_dados(xml)
    response = urllib.request.urlopen(link)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    try:
        lista_att = html.find('span', class_='documentModified').find('span', class_='value').get_text()
    except:
        lista_att = "notícia não modificada"
    lista_conteudo = []
    linhas = html.find('div', {'id' : 'content-core'}).find_all(['p','h3'])
    for conteudo in linhas:
        if conteudo.name == 'h3':
            texto = conteudo.text
            texto = texto.upper()
        else:
            texto = conteudo.text 
        lista_conteudo.append(texto)
    lista_categoria = html.find('span', {'id' : 'form-widgets-categoria'}).find('a').get_text()
    lista_tag = []
    for spt in html.find('div', {'id' : 'category'}).find_all('span'):
        tag = spt.text
        lista_tag.append(tag)
    lista_update = [lista_att,lista_conteudo,lista_categoria,lista_tag]
    return lista_update
    


DIR_LOCAL= "/home/labri_joaomotta/codigo"

def main ():
    #download_sitemap_xml()
    url_site = f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap.xml"
    xml = mapa_do_site_2(url_site)
    extracao_conteudo(xml)

if __name__ == "__main__":
    main()