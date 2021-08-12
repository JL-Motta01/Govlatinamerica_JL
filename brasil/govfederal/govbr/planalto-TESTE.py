from urllib.request import urlopen
import urllib
import urllib.request #realizar requisição da página html
import os #para especificar o caminho do download
import wget
from urllib.parse import urlparse #realizar parseamento do html
from bs4 import BeautifulSoup #importa o beautifulsoup para extrair as infos das tags
from pprint import pprint #organizar estéticamente os prints
from requests.models import DecodeError 

def download_sitemap_xml():
    url = "https://www.gov.br/sitemap.xml"
    wget.download(url)

def mapa_do_site (url):
    response = urllib.request.urlopen(url)
    xml = BeautifulSoup(response, 'lxml-xml', from_encoding = response.info().get_param("charset"))

    return xml

def download_pagina (url_pg,titulo):
    mypath = "/home/labri_joaomotta/codigo/govlatinamerica/brasil/govfederal/govbr/arquivos/html_noticia"
    filename = ( titulo + ".html")
    fullfilename = os.path.join(mypath, filename)
    urllib.request.urlretrieve(url_pg, fullfilename)

def parse_mapa (xml):
    lista_de_titulos = xml.find_all("news:title")
    lista_de_links = xml.find_all("loc")
    lista_de_datas = xml.find_all("news:publication_date")   
    for titulo,link,data in zip (lista_de_titulos, lista_de_links, lista_de_datas):
        print (titulo.text)
        print (link.text)
        print (data.text)
        #download_pagina(link.text, titulo.text)
    return lista_de_titulos


def main ():
    download_sitemap_xml()
    #url_site = "https://www.gov.br/sitemap.xml"
    #xml = mapa_do_site(url_site)
    #parse_mapa(xml)


if __name__ == "__main__":
    main()