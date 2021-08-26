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
        lista_tmp.append(data.text)
        lista_tmp.append(titulo.text)
        lista_tmp.append(link.text)
        lista_geral.append(lista_tmp)
    return lista_geral
    

def base_dados(xml,db,User):
    lista_geral = parse_mapa(xml)
    for sublista in lista_geral:
        db_planalto = db.contains(User.titulo==sublista[0])
        if not db_planalto:
            print("não está na base")
            db.insert({
                "data": sublista[0],
                "título":sublista[1],
                "link": sublista[2],
                "atualizado em": [],
                "conteúdo": [],
                "categoria": [],
                "tag": [],
            })
        if db_planalto:
            print("está na base")

#def extração_conteudo():
    #

DIR_LOCAL= "/home/labri_joaomotta/codigo"

def main ():
    #download_sitemap_xml()
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/db.json")
    User = Query()
    url_site = f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/sitemap.xml"
    xml = mapa_do_site_2(url_site)
    base_dados(xml,db,User)

if __name__ == "__main__":
    main()