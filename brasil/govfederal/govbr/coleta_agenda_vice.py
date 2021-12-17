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
from datetime import date, timedelta, datetime


DIR_LOCAL= "/home/labri_joaomotta/codigo"

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"

def acessar_pagina(url):
    """Analisa os boletim do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def datas():
    data_inicio = date (2019,1,1)
    data_fim = date.today()
    delta = data_fim - data_inicio
    lista_data = []
    for dia in range(delta.days+1):
        dia_delta = data_inicio + timedelta(days=dia)
        lista_data.append(dia_delta)
    lista_data_final = [datetime.strftime(dt,format="%Y-%m-%d") for dt in lista_data]
    return lista_data_final

def agenda():
    """Percorre as datas da agenda"""
    lista_data = datas()
    #lista_data = ["2021-11-22","2021-11-25"]
    url_base = "https://www.gov.br/planalto/pt-br/nova-vice-presidencia/agenda-vice-presidente/"
    lista_url_data = []
    for data in lista_data:
        url= url_base+data
        lista_url_data.append(url)
    return lista_url_data

def coleta_compromissos():
    """coleta os compromissos de cada dia"""
    for dia in agenda():
        db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_agenda_vice.json", ensure_ascii=False)
        User = Query()
        try:
            pagina_dia = acessar_pagina(dia)
            url=dia
            data=pagina_dia.find("span", {"id":"breadcrumbs-current"}).text
            try:
                lista_conteudo=[]
                compromissos = pagina_dia.find("ul", class_="list-compromissos").find_all("div", class_="item-compromisso")
                
                for conteudo in compromissos:
                    detalhes=[]
                    titulo=conteudo.find("h2", class_="compromisso-titulo").text
                    print(titulo)
                    detalhes.append(titulo)
                    horario=conteudo.find("div", class_="horario").text
                    detalhes.append(horario)
                    local=conteudo.find("div", class_="compromisso-local").text
                    detalhes.append(local)
                    detalhes.append(data)
                    detalhes.append(url)
                    lista_conteudo.append(detalhes)
            except:
                lista_conteudo= "NA"
            print(lista_conteudo,type(lista_conteudo)) 
            for detalhe in lista_conteudo:
                db_planalto = db.contains((User.compromisso==detalhe[0])&(User.data==detalhe[3][-10:])&(User.horario==detalhe[1]))
                if not db_planalto:
                    print("não está na base")
                    db.insert({
                        "link":detalhe[4],
                        "data":detalhe[3][-10:],
                        "compromisso": detalhe[0],
                        "horario": detalhe[1].replace("              ","").replace("\n",""),
                        "local": detalhe[2]
                        })
                else:
                    print("está na base")
        except:
            pass
        

def main ():
    """Função principal"""
    coleta_compromissos()

if __name__ == "__main__":
    main()