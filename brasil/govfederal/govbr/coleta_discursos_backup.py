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

DIR_LOCAL= "/home/labri_joaomotta/codigo"

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"

def acesso_discursos (url):
    """Analisa os discursos do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_discursos ():
    """Percorre as páginas onde fical os links"""
    lista_url_discursos = []
    contador = 0
    while contador<421:
        dominio = "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int="
        dominio += str(contador)
        contador += 30
        lista_url_discursos.append(dominio)
    return lista_url_discursos

def coleta_link_discursos ():
    """Coleta os links de cada página que contém discursos"""
    lista_links=[]
    for url in paginas_com_url_discursos():
        html = acesso_discursos(url)
        discursos = html.find_all("article", class_= "tileItem visualIEFloatFix tile-document")
        for articles in discursos:
            links = articles.a["href"]
            lista_links.append(links)
    return lista_links

def base_dados():
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_discursos.json")
    User = Query()
    lista_geral = coleta_conteudo_discursos()
    for sublista in lista_geral:
        db_planalto = db.contains(User.titulo==sublista[0])
        if not db_planalto:
            print("não está na base")
            db.insert({
                "link": sublista[0],
                "data":sublista[1],
                "atualizado em": sublista[2],           
                "tags": sublista[3],
                "titulo": sublista[4],
                "conteudo": sublista[5],
            })
        else:
            print("está na base")


def coleta_conteudo_discursos ():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos discursos"""
    lista_geral=[]
    for link in coleta_link_discursos():
        discursos = acesso_discursos(link)
        lista_temp=[]
        url = link
        publicado_em = discursos.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            atualizado_em = discursos.find("span", class_="documentModified").find("span", class_="value").text
        except:
           atualizado_em = "discurso não modificado"
        try:
            lista_tags=[]
            spans=discursos.find("div", {"id" : "category"}).find_all("span") 
            for span in spans:
                tag = span.text
                lista_tags.append(tag)
        except:
            lista_tags="não possui tags"
        titulo = discursos.find("h1", class_="documentFirstHeading").text
        try:
            lista_conteudo=[]
            paragrafos = discursos.find('div', {'id' : 'content-core'}).find_all(['p','h3','h2','h1'])
            for conteudo in paragrafos:
                if conteudo.name == 'h3' or conteudo.name == 'h2' or conteudo.name == 'h1':
                    texto = conteudo.text
                    texto = texto.upper()
                else:
                    texto = conteudo.text 
                lista_conteudo.append(texto)
        except:
            lista_conteudo= "notícia sem conteúdo"
        lista_temp.append(url)
        lista_temp.append(publicado_em)
        lista_temp.append(atualizado_em)
        lista_temp.append(lista_tags)
        lista_temp.append(titulo)
        lista_temp.append(lista_conteudo)
        lista_geral.append(lista_temp)
        
    return lista_geral

def main ():
    """Função principal"""
    base_dados()

if __name__ == "__main__":
    main()