import urllib.request #realizar requisição da página html
from urllib.parse import urlparse #realizar pareamento do html
from bs4 import BeautifulSoup
from pprint import pprint 

def mapa_do_site (url):
    response = urllib.request.urlopen(url)
    xml = BeautifulSoup(response, 'lxml-xml', from_encoding = response.info().get_param("charset"))

    return xml

def parse_mapa (xml):
    lista_de_titulos = xml.find_all("news:title")
    lista_de_links = xml.find_all("loc")
    lista_de_datas = xml.find_all("news:publication_date")
    for titulo,link,data in zip (lista_de_titulos, lista_de_links, lista_de_datas):
        print (titulo.text)
        print (link.text)
        print (data.text)
    return lista_de_titulos


def main ():
    url_site = "https://www.gov.br/sitemap.xml"
    xml = mapa_do_site(url_site)
    parse_mapa(xml)

if __name__ == "__main__":
    main()