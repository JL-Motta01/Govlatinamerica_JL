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

DIR_LOCAL= "/home/labri_joaomotta/codigo"

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"

def acessar_pagina(url):
    """Analisa os Ministro do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_Ministro ():
    """Percorre as páginas onde fical os links"""
    pagina_inicio = acessar_pagina("https://www.gov.br/planalto/pt-br/conheca-a-presidencia/ministros")
    lista_url_Ministro = pagina_inicio.find_all("div", class_="column col-md-4")
    return lista_url_Ministro

def coleta_link():
    """Coleta os links de cada página que contém Ministro"""
    lista_links=[]
    for url in paginas_com_url_Ministro():
        try:
            Ministro = url.a["href"]
            lista_links.append(Ministro)
        except:
            pass
    return lista_links

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos Ministro"""
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_Ministro.json", ensure_ascii=False)
    User = Query()
    for link in coleta_link():
        Ministro = acessar_pagina(link)
        url = link
        publicado_em = Ministro.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            atualizado_em = Ministro.find("span", class_="documentModified").find("span", class_="value").text
        except:
           atualizado_em = "Ministro não modificado"
        titulo = Ministro.find("h1", class_="documentFirstHeading").text
        try:
            nome_ministro = Ministro.find("div",class_="documentDescription description").text
        except:
            nome_ministro = "Nome não inserido, verificar biografia"
        try:
            lista_conteudo=[]
            paragrafos = Ministro.find('div', {'id' : 'content-core'}).find_all(['p','h3','h2','h1'])
            for conteudo in paragrafos:
                if conteudo.name == 'h3' or conteudo.name == 'h2' or conteudo.name == 'h1':
                    texto = conteudo.text
                    texto = texto.upper()
                else:
                    texto = conteudo.text 
                lista_conteudo.append(texto)
        except:
            lista_conteudo= "biografia sem conteúdo"
        db_planalto = db.contains(User.titulo==titulo,User.data==publicado_em)
        if not db_planalto:
            print("não está na base")
            db.insert({
                "link":url,
                "data":publicado_em,
                "atualizado em":atualizado_em,  
                "titulo":titulo,
                "nome": nome_ministro,
                "Conteudo": lista_conteudo
            })
        else:
            print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()