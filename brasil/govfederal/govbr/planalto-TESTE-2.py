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
            })
            lista_geral2 = extracao_conteudo(sublista[2])
            for sublista2 in lista_geral2:
                db.insert({
                    "atualizado em": sublista2[0],
                    "conteúdo": sublista2[1],
                    "categoria": sublista2[2],
                    "tag": sublista2[3],
                })
        if db_planalto:
            print("está na base")

def extracao_conteudo(link):
    response = urllib.request.urlopen(link)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    lista_att = html.find("span", {"class" : "documentmodified"}).getText
    print(lista_att)
    lista_conteudo = html.find("div",{"id" : "content-core"}).getText
    lista_categoria = html.find("div",{"id" : "formfield-form-widgets-categoria"}).getText
    lista_tag = html.find("div",{"id" : "category"}).getText
    lista_geral2 = []
    for atualizado_em, conteudo, categoria, tag in zip (lista_att, lista_conteudo, lista_categoria, lista_tag):
        lista_tmp2 = [] 
        lista_tmp2.append(atualizado_em.text)
        lista_tmp2.append(conteudo.text)
        lista_tmp2.append(categoria.text)
        lista_tmp2.append(tag.text)
        lista_geral2.append(lista_tmp2)
    return lista_geral2


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