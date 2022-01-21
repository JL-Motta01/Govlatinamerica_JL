""" Para utilizar esse script, é necessário incorporá-lo em um dos repositórios de coleta. 
Por exemplo: govlatinamerica. """
from waybackpy import WaybackMachineSaveAPI
from dotenv import load_dotenv
from tinydb import TinyDB, Query, where
import os
import sys 
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
from diretorios.diretorio import diretorios


def salvar_internet_archive(link):
    """ passa a url para o internet archive e devolve a url enviada pelo link gerado pelo internet archive """
    url = "https://www.gov.br/mj/pt-br/assuntos/noticias/ministerio-da-justica-e-seguranca-publica-realiza-segunda-etapa-dos-ensaios-tecnicos-em-viaturas"
    user_agente = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    save_api = WaybackMachineSaveAPI(url, user_agente)
    link_archive = save_api.save()
    arquivar_data = save_api.timestamp()
    return url, link_archive

def salvar_internet_archive_exemplo(link):
    """ função de teste para verificação do consulta_json sem ter que fazer chamada para internet archive """
    url = link  
    link_archive = "https://web.archive.org/web/20220119125447/"+url
    return url, link_archive

def consulta_json():
    # lista = ["BIBLIOTECA-PRESIDENCIA", "PLANALTO", "MRE", "MMA", "INFRAESTRUTURA", "MME", "ECONOMIA", "DEFESA", "SAUDE", "MCTI", "MDH", "MCOM", "TURISMO", "MDR", "SECRETARIAGERAL", "CGU", "AGU", "CIDADANIA", "SECRETARIADEGOVERNO", "MEC", "MJ", "GSI", "CASACIVIL", "AGRICULTURA"]
    ministerios = ["CIDADANIA", "MJ"]
    for nome in ministerios:
        dir_banco = diretorios(nome)[0]
        db = TinyDB(f'{dir_banco}/{nome}.json', indent=4, ensure_ascii=False)
        for link in iter(db): # iter >> iteracao 
            url_link = link["link"]
            url_link_archive = link["link_archive"]
            if url_link_archive == "NA":
                internet_archive = salvar_internet_archive(url_link)
                atualizar = atualiza_json(internet_archive)

def atualiza_json(archive):
    print(archive)
    nome = archive[0].split("/")[3].upper()
    dir_banco = diretorios(nome)[0]
    db = TinyDB(f'{dir_banco}/{nome}.json', ensure_ascii=False)
    db.update({"link_archive": archive[1]}, where("link")==archive[0])

def main():
    consulta = consulta_json()

if __name__=="__main__":
    main()