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

def acesso_discursos (url):
    """Analisa os discursos do site a partir do link"""
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'html', from_encoding = response.info().get_param("charset"))
    return html

def parse_discursos ():
    html = acesso_discursos("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int=0")
    discursos = html.find('div', {'id' : 'content'}).find('div', {'id' : 'content-core'}).find_all("article", {"class" : "tileItem visualIEFloatFix tile-document"})
    return print(discursos)

def main ():
    parse_discursos()

if __name__ == "__main__":
    main()