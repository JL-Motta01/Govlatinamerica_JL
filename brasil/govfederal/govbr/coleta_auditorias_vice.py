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
    """Analisa os auditoria_vice do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_auditoria_vice ():
    """Percorre as páginas onde fical os links"""
    lista_url_auditoria_vice = ["https://www.gov.br/secretariageral/pt-br/estrutura/secretaria_de_controle_interno/resultados","https://www.gov.br/planalto/pt-br/nova-vice-presidencia/acesso-a-informacao/auditorias/relatorio-de-gestao_vpr_2018.pdf/view","https://www.gov.br/planalto/pt-br/nova-vice-presidencia/acesso-a-informacao/auditorias/relatorio-de-gestao_pr_2019.pdf/view"]
    return lista_url_auditoria_vice

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos auditoria_vice"""
    db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_auditoria_vice.json", ensure_ascii=False)
    User = Query()
    for link in paginas_com_url_auditoria_vice():
        auditoria_vice = acessar_pagina(link)
        try:
            links_pdf = auditoria_vice.find_all("a", class_="internal-link")
        except:
            links_pdf = auditoria_vice.find("div", {id:"content-core"}).find_all("a")
        print(links_pdf)
        for pdf in links_pdf:
            url = pdf["href"]
            titulo = pdf.text
            db_planalto = db.contains(User.titulo==titulo)
            if not db_planalto:
                print("não está na base")
                wget.download(url, f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_auditoria_vice/")
                db.insert({
                    "origem": "vice presidência",
                    "classificado": "Auditorias",
                    "link":url, 
                    "titulo":titulo,
                })
            else:
                print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()