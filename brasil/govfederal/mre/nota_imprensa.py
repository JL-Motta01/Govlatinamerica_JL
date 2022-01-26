from urllib.request import urlopen
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tinydb import TinyDB, Query
import lxml
import os
import sys 
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
from templates.diretorios.diretorio import diretorios
# from templates.template_html.html_template import html_consultar
from templates.acesso_bd.inserir_bd import inserir_bd


def acessar_pagina_local(url):
    html = open(url).read().encode("utf-8")
    bs = BeautifulSoup(html, "lxml")
    # print(bs)
    return bs 


def notas_imprensa():
    env_dir = load_dotenv(f'{DIR_PROJETO}/.env_dir')
    DIR_BD = os.getenv("DIR_BD_FINAL") # getenv só aceita str
    MRE = os.getenv("MRE")
    MRE_NOTAS_IMPRENSA = "/001/mre-notas-imprensa/"
    DIR_FINAL = DIR_BD + "/" + MRE + MRE_NOTAS_IMPRENSA
    # print(DIR_FINAL)
    anos = [sorted(os.listdir(DIR_FINAL))[-2]]
    print(anos)
    for ano in anos:
        DIR_HTML = DIR_FINAL + ano
        listar_html = os.listdir(DIR_HTML)
        for html in listar_html:
            DIR_COMPLETO = os.path.join(DIR_HTML, html)
            # print(DIR_COMPLETO)
            extrair_infos = extrai_info(DIR_COMPLETO)


def extrai_info(html):
    bs = acessar_pagina_local(html)
    titulo = bs.find("title").text
    print(titulo)
    data = bs.find("dd", class_="published").text
    print(data)


def main():
    notas = notas_imprensa()


if __name__ == "__main__":
    main()