import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tinydb import TinyDB, Query
import lxml
import os
import sys
import unicodedata 
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
if NOME_PROJETO == "templates":
    from diretorios.diretorio import diretorios, diretorios_template 
else:
    from templates.diretorios.diretorio import diretorios, diretorios_template 
print(f'DIR PROJETO: {DIR_PROJETO}')
from templates.acesso_bd.inserir_bd import inserir_bd
from templates.template_html.html_template import html_consultar_json


def acessar_pagina(url):
    """Responsável por acessar as páginas enviadas a ele"""
    html = requests.get(url)
    bs = BeautifulSoup(html.text, "html.parser")
    # print(bs)
    return bs

def paginas_info():
    #https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=90
    paginas_info = []
    contador = 4170
    while contador > 0:
        url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
        url = url + str(contador)
        contador = contador - 30
        paginas_info.append(url)
    return paginas_info

def extrair_info(url):
    """Responsável por extrair as informações solicitadas"""
    sigla = "MRE_NOTAS_IMPRENSA"
    codigo_bd = "bd/003/001/001/001/002/001"
    env_dir_bd = "BD_MRE_NOTAS_IMPRENSA"
    classificado = ["notas de imprensa"]
    origem = "Ministério das Relações Exteriores"
    autoria = ["Ministério das Relações Exteriores"]
    bs = acessar_pagina(url)
    tag_h1 = bs.find("h1").text
    print(tag_h1)
    notas = bs.find_all("article")
    #print(notas)
    for nota in notas:
        titulo = nota.find("h2").text.strip()
        data = nota.find_all("span", class_="summary-view-icon")[0].text.strip()
        horario = nota.find_all("span", class_="summary-view-icon")[1].text.strip()
        try:
            num_nota = nota.find("span", class_="subtitle").text.strip()
            num_nota = num_nota.split()[-1]
        except:
            num_nota = "NA"
        link = nota.a["href"]
        print(titulo)
        print(data)
        print (horario)
        print(num_nota)
        print(link)
        acessar_nota = acessar_pagina(link)
        tag_p = acessar_nota.find_all("p")
        paragrafos = [unicodedata.normalize("NFKD",paragrafo.get_text(strip=True)) for paragrafo in tag_p]
        
        for p in paragrafos.copy():
            if p == "Notícias":
                paragrafos.remove(p)
            if "NOTA À IMPRENSA Nº" in p:
                paragrafos.remove(p)
        paragrafos = filter(None,paragrafos)
           
        print(paragrafos)
        # paragrafos_final = []
        # for paragrafo in paragrafos:
        #     paragrafos_final.append(paragrafo.text)
        # print(paragrafos_final)
        #inserir_banco = inserir_bd(env_dir_bd=env_dir_bd, titulo=titulo, data=data, horario=horario, extra_01=num_nota, origem=origem, autoria=autoria, classificado=classificado, sigla=sigla, codigo_bd=codigo_bd)
#//*[@id="content-core"]/article[1]/div/h2/a
#informações importantes: n° da nota, título, data, horário e link para conteúdo

def main():
    #extrair_info()
    paginas = paginas_info()
    for url in paginas:
        extrair_info(url)


if __name__ == "__main__":
    main()