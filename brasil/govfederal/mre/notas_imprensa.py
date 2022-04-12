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
from templates.template_html.html_template import html_consultar_json
from templates.acesso_bd.inserir_bd import inserir_bd
from notas_imprensa_quebrados import links_quebrados

def acessar_pagina_local(url):
    """responsavel por acessar as paginas html"""
    html = open(url).read().encode("utf-8")
    bs = BeautifulSoup(html, "lxml")
    # print(bs)
    return bs 


def notas_imprensa():
    """responsavel por encontrar a localização dos htmls 
    e chamar a função que extrai as infos do html"""
    env_dir = load_dotenv(f'{DIR_PROJETO}/.env_dir')
    DIR_BD = os.getenv("DIR_BD_FINAL") # getenv só aceita str
    MRE = os.getenv("MRE")
    MRE_NOTAS_IMPRENSA = "/001/mre-notas-imprensa/"
    DIR_FINAL = DIR_BD + "/" + MRE + MRE_NOTAS_IMPRENSA
    # print(DIR_FINAL)
    anos = sorted(os.listdir(DIR_FINAL))
    print(anos)
    for ano in anos:
        # print(ano)
        DIR_HTML = DIR_FINAL + ano
        listar_html = sorted(os.listdir(DIR_HTML))
        quebrados = links_quebrados()
        print(quebrados)
        for html in listar_html:
            print(f'NOME HTML:{html}')
            buscar = [quebrado for quebrado in quebrados if quebrado in html]
            print(buscar)
            if not buscar: 
                DIR_COMPLETO = os.path.join(DIR_HTML, html)
                print(f'DIR_COMPLETO:{DIR_COMPLETO}')
                extrair_infos = extrai_info(DIR_COMPLETO, ano[-4:])


def extrai_info(html, ano):
    """
    extrai e insere no banco as seguintes informações: 
    origem, classificado, autoria, título, data, link, parágrafos, extra_01 (número da nota),
    a função internet_archive atualiza o banco com as seguintes informações:
    link_archive, data_archive, horario_archive, 
    a função template_html atualiza o banco com as seguintes informações:
    nome_arquivo, dir_bd, dir_arquivo,
    """
    bs = acessar_pagina_local(html)
    origem = "Ministério das Relações Exteriores"
    classificado = ["notas de imprensa"]
    autoria = ["Ministério das Relações Exteriores"]
    link = "NA"
    try:
        tag_titulo = bs.find("h1", {"class" : "documentFirstHeading"})
        titulo = tag_titulo.span.text.strip()
    except:
        titulo = "NA"
   
    if ano == "2012":
        print(f'TITULO: {titulo}')
        data = bs.find("dd", class_="published").text
        print(f'DATA {ano}: {data}')
        div_pf = bs.find("div", class_="item-page artigo-padrao").find_all("p")
        lista_paragrafos = []
        for pf in div_pf: 
            lista_paragrafos.append(pf.text)
    anos = ["2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997"]
    if ano in anos:
        print(f'TITULO: {titulo}')
        print(f'HTML: {html}') 
        try:
            nota_numero = bs.find("div", {"id":"content"}).span.em.text
            extra_01 = nota_numero
            print(f'NUMERO: {nota_numero}')
        except:
            nota_numero = "NA"
            extra_01 = nota_numero
            print(f'NUMERO: {nota_numero}')
        try:   
            tag_data = bs.find("div",{"id":"parent-fieldname-text"})
            data = tag_data.span.text.strip(" -")
            print(f'DATA {ano}: {data}')
        except:
            data = "NA"
            print(f'DATA:{data}')
        try:
            div_pf = bs.find("div",{"id":"parent-fieldname-text"}).find_all("p")
            paragrafos = []
            for pf in div_pf: 
                paragrafo = pf.text.replace("\n", "").strip()
                paragrafos.append(paragrafo)
            print(paragrafos)
        except:
            paragrafos = ["NA"]
            print(f'PARAGRAFOS:{paragrafos}')
    print("#####")
    sigla = "MRE_NOTAS_IMPRENSA"
    codigo_bd = "bd/003/001/001/001/002/001"
    env_dir_bd = "BD_MRE_NOTAS_IMPRENSA"
    inserir_banco = inserir_bd(env_dir_bd = env_dir_bd, titulo = titulo, data=data, paragrafos=paragrafos, extra_01=extra_01, origem=origem, autoria=autoria, classificado=classificado, sigla=sigla, codigo_bd=codigo_bd)
    gerar_html = html_consultar_json(env_dir_bd)
        
   
def main():
    notas = notas_imprensa()
    #notas_impensa = extrai_info("/home/labri_treyceannunciado/codigo/govlatinamerica/brasil/govfederal/mre/notas_imprensa/MRE-Notas-Imprensa-2011/ataque-as-nacoes-unidas-no-afeganistao.html", "2011")

if __name__ == "__main__":
    main()