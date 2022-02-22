""" Para utilizar esse script, é necessário incorporá-lo em um dos repositórios de coleta. 
Por exemplo: govlatinamerica. """
from dotenv import load_dotenv
import os

def diretorios(nome, ano="NA"):
        """ essa função retorna a pasta do banco, do html, do html-ano, referencia-abnt, estilo-css """
        print(f'NOME: {nome}')
        DIR_ATUAL = os.environ["PWD"] 
        lista_dir_atual = DIR_ATUAL.split("/")
        NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
        lista_dir_atual_02 = DIR_ATUAL.split(NOME_PROJETO)
        DIR_ROOT = lista_dir_atual_02[0]+NOME_PROJETO
        env_dir = load_dotenv(f'{DIR_ROOT}/.env_dir') 
        DIR_BD_FINAL = os.getenv(nome)
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        BASE_DADO = os.getenv(str(nome))
        print(f'BASE_DADO: {BASE_DADO}')
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        if NOME_PROJETO != "templates":
            DIR_TEMPLATE_HTML = DIR_ROOT + "/templates/template_html"
            ESTILO = DIR_TEMPLATE_HTML + "/css/style.css" 
            REFERENCIAS = DIR_TEMPLATE_HTML + "/js/referencia.js" 
        cria_dir_banco = os.makedirs(f'{DIR_BD_FINAL}/json', exist_ok = True) # makedirs cria diretório
        DIR_BD = f'{DIR_BD_FINAL}'
        cria_dir_html = os.makedirs(f'{DIR_BD_FINAL}/html', exist_ok = True)
        DIR_HTML = f'{DIR_BD_FINAL}/html'
<<<<<<< HEAD
        cria_dir_html_img = os.makedirs(f'{DIR_BD_FINAL}/html_img', exist_ok = True)        
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_BD_FINAL}/html/{ano}', exist_ok = True)
            cria_dir_html_img = os.makedirs(f'{DIR_BD_FINAL}/html_img/{ano}', exist_ok = True)
            DIR_HTML_ANO = f'{DIR_BD_FINAL}/html/{ano}'
            DIR_HTML_IMG = f'{DIR_BD_FINAL}/html_img/{ano}'
=======
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_BD_FINAL}/html/{ano}', exist_ok = True)
            DIR_HTML_ANO = f'{DIR_BD_FINAL}/html/{ano}'
>>>>>>> ae4a163ee176e7956175c7bc34db61b45c20e284
        else:
            DIR_HTML_ANO = f'{DIR_BD_FINAL}/html'
            DIR_HTML_IMG = f'{DIR_BD_FINAL}/html_img'
        return (DIR_BD, DIR_HTML, DIR_HTML_ANO, REFERENCIAS, ESTILO, DIR_HTML_IMG)

def diretorios_template(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        DIR_ATUAL = os.environ["PWD"] 
        lista_dir_atual = DIR_ATUAL.split("/")
        NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
        lista_dir_atual_02 = DIR_ATUAL.split(NOME_PROJETO)
        DIR_ROOT = lista_dir_atual_02[0]+NOME_PROJETO
        env_dir = load_dotenv(f'{DIR_ROOT}/.env_dir') 
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        if NOME_PROJETO != "templates":
            DIR_ROOT += "/templates/template_html"
            ESTILO = DIR_ROOT + "/css/style.css" 
            REFERENCIAS = DIR_ROOT + "/js/referencia.js"       
        print(f'{DIR_ROOT}/.env_dir')
        DIR_BD_FINAL = os.getenv(nome)
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        BASE_DADO = os.getenv(str(nome))
        print(f'BASE_DADO: {BASE_DADO}')
        cria_dir_banco = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/json', exist_ok = True)
        cria_dir_html = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html', exist_ok = True)
<<<<<<< HEAD
        cria_dir_html_img = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html_img', exist_ok = True)
=======
>>>>>>> ae4a163ee176e7956175c7bc34db61b45c20e284
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/json')
        print(f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/{BASE_DADO}/json')
<<<<<<< HEAD
        return (f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/json', f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html', dir_html_ano, REFERENCIAS, ESTILO, f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html_img')
=======
        return (f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/json', f'{DIR_ROOT}/exemplos/{NOME_PROJETO}/html', dir_html_ano, REFERENCIAS, ESTILO)
>>>>>>> ae4a163ee176e7956175c7bc34db61b45c20e284

