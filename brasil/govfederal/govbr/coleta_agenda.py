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
from tinydb.operations import add


DIR_LOCAL= "/home/labri_joaomotta/codigo"

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"

def acessar_pagina(url):
    """Analisa os boletim do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def agenda():
    """Percorre as datas da agenda"""
    lista_data = ["2021-11-11","2021-11-10"]
    url_base = "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/"
    lista_url_data = []
    for data in lista_data:
        url= url_base+data
        lista_url_data.append(url)
    return lista_url_data

def coleta_compromissos():
    """coleta os compromissos de cada dia"""
    for dia in agenda():
        db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_agenda.json")
        User = Query()
        try:
            pagina_dia = acessar_pagina(dia)
            url=dia
            data=pagina_dia.find("span", {"id":"breadcrumbs-current"}).text
            db_planalto = db.contains(User.data==data)
            try:
                lista_conteudo=[]
                compromissos = pagina_dia.find("ul", class_="list-compromissos").find_all("div", class_="item-compromisso")
                for conteudo in compromissos:
                    detalhes=[]
                    titulo=conteudo.find("h4", class_="compromisso-titulo").text
                    detalhes.append(titulo)
                    horario=conteudo.find("div", class_="horario").text
                    detalhes.append(horario)
                    local=conteudo.find("div", class_="compromisso-local").text
                    detalhes.append(local)
                    lista_conteudo.append(detalhes)
            except:
                lista_conteudo= "data sem cmpromissos"
            if not db_planalto:
                print("não está na base")
                db.insert({
                    "link":url,
                    "data":data,
                    "compromisso": ""
                })
                for item in lista_conteudo:
                    db.update(add("compromisso",item[0]),User.data==data)
            else:
                print("está na base")
        except:
            pass
        

def main ():
    """Função principal"""
    coleta_compromissos()

if __name__ == "__main__":
    main()