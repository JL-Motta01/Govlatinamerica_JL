""" Para utilizar esse script, é necessário incorporá-lo em um dos repositórios de coleta. 
Por exemplo: govlatinamerica. """
from dotenv import load_dotenv
import os

def diretorios(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        DIR_ATUAL = os.environ["PWD"] 
        lista_dir_atual = DIR_ATUAL.split("/")
        NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
        lista_dir_atual_02 = DIR_ATUAL.split(NOME_PROJETO)
        DIR_ROOT = lista_dir_atual_02[0]+NOME_PROJETO
        env_dir = load_dotenv(f'{DIR_ROOT}/diretorios/.env_dir') 
        LOCAL = os.getenv("LOCAL")
        DIR_BD_FINAL = os.getenv("DIR_BD_FINAL")
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        MINISTERIO = os.getenv(str(nome))
        print(f'MINISTERIO: {MINISTERIO}')
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        if NOME_PROJETO != "template_html":
            DIR_TEMPLATE_HTML = DIR_ROOT + "/template_html"
            ESTILO = DIR_TEMPLATE_HTML + "/css/style.css" 
            REFERENCIAS = DIR_TEMPLATE_HTML + "/js/referencia.js"
        env_dir = load_dotenv(f'{DIR_ROOT}/diretorios/.env_dir') 
        cria_dir_banco = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        DIR_BD = f'{DIR_BD_FINAL}/{MINISTERIO}/banco'
        cria_dir_html = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/html', exist_ok = True)
        DIR_HTML = f'{DIR_BD_FINAL}/{MINISTERIO}/html'
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/html/{ano}', exist_ok = True)
            DIR_HTML_ANO = f'{DIR_BD_FINAL}/{MINISTERIO}/html/{ano}'
        else:
            DIR_HTML_ANO = "NA"
        return (DIR_BD, DIR_HTML, DIR_HTML_ANO, REFERENCIAS, ESTILO)

def diretorios_template(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        DIR_ATUAL = os.environ["PWD"] 
        lista_dir_atual = DIR_ATUAL.split("/")
        NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
        lista_dir_atual_02 = DIR_ATUAL.split(NOME_PROJETO)
        DIR_ROOT = lista_dir_atual_02[0]+NOME_PROJETO
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        if NOME_PROJETO != "template_html":
            DIR_ROOT += "/template_html"
            ESTILO = DIR_ROOT + "/css/style.css" 
            REFERENCIAS = DIR_ROOT + "/js/referencia.js"
        env_dir = load_dotenv(f'{DIR_ROOT}/.env_dir') 
        print(f'{DIR_ROOT}/.env_dir')
        # /home/labri_juliasilveira/codigo/template_html/.env_var
        LOCAL = os.getenv("LOCAL")
        DIR_BD_FINAL = os.getenv("DIR_BD_FINAL")
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        MINISTERIO = os.getenv(str(nome))
        print(f'MINISTERIO: {MINISTERIO}')
        cria_dir_banco = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        # /home/labri_cintiaiorio/codigo/govlatinamerica/template_html/exemplos/min-cidadania/banco/CIDADANIA.json
        cria_dir_html = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/html', exist_ok = True)
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/banco')
        print(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/html')
        return (f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/banco', f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{MINISTERIO}/html', dir_html_ano, REFERENCIAS, ESTILO)

