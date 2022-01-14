from dotenv import load_dotenv
import os

def diretorios(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        DIR_ATUAL = os.environ["PWD"] 
        DIR_TMP = DIR_ATUAL.split("govlatinamerica")
        DIR_ROOT = DIR_TMP[0]+"govlatinamerica"
        env_dir = load_dotenv(f'{DIR_ROOT}/template_html/.env_var') 
        LOCAL = os.getenv("LOCAL")
        DIR_BD_FINAL = os.getenv("DIR_BD_FINAL")
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        MINISTERIO = os.getenv(str(nome))
        print(f'MINISTERIO: {MINISTERIO}')
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        cria_dir_banco = os.makedirs(f'{DIR_CONFIG}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        cria_dir_html = os.makedirs(f'{DIR_CONFIG}/{MINISTERIO}/html', exist_ok = True)
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_CONFIG}/{MINISTERIO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_CONFIG}/{MINISTERIO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_CONFIG}/{MINISTERIO}/banco')
        print(f'{DIR_CONFIG}/{MINISTERIO}/html')
        return (f'{DIR_CONFIG}/{MINISTERIO}/banco', f'{DIR_CONFIG}/{MINISTERIO}/html', dir_html_ano, REFERENCIAS, ESTILO)

def diretorios_template(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        NOME_PROJETO = "govlatinamerica"
        DIR_ATUAL = os.environ["PWD"] 
        DIR_TMP = DIR_ATUAL.split("govlatinamerica")
        DIR_ROOT = DIR_TMP[0]+"govlatinamerica"
        env_dir = load_dotenv(f'{DIR_ROOT}/template_html/.env_var') 
        LOCAL = os.getenv("LOCAL")
        DIR_BD_FINAL = os.getenv("DIR_BD_FINAL")
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        MINISTERIO = os.getenv(str(nome))
        print(f'MINISTERIO: {MINISTERIO}')
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
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

