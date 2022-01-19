""" Para utilizar esse script, é necessário incorporá-lo em um dos repositórios de coleta. 
Por exemplo: govlatinamerica. """
from waybackpy import WaybackMachineSaveAPI
from dotenv import load_dotenv
from tinydb import TinyDB, Query
import os
import sys 
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
from diretorios.diretorio import diretorios


def salvar_pagina():
    link = "https://www.gov.br/mj/pt-br/assuntos/noticias/ministerio-da-justica-e-seguranca-publica-realiza-segunda-etapa-dos-ensaios-tecnicos-em-viaturas"
    user_agente = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    save_api = WaybackMachineSaveAPI(link, user_agente)
    link_archive = save_api.save()
    arquivar_data = save_api.timestamp()
    print(link_archive)
    print(arquivar_data)
    return link, link_archive

def link_internet_archive(archive):
    nome = archive[0].split("/")[3].upper()
    dir_banco = diretorios(nome)[0]
    db = TinyDB(f'{dir_banco}/{nome}.json')
    myDBQuery = Query()
    # fazer termo de busca
    bd.update({"link_archive": archive[1]})

def main():
    archive = salvar_pagina()
    internet_archive = link_internet_archive(archive)

if __name__=="__main__":
    main()