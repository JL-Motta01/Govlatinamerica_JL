from dotenv import load_dotenv
import os

def diretorios(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        LOCAL = os.getenv("LOCAL")
        env_dir = load_dotenv(f'{LOCAL}/codigo/govlatinamerica/template-html/.env_var') 
        DIR_BD_FINAL = os.getenv("DIR_BD_FINAL")
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        MINISTERIO = os.getenv(str(nome))
        print(f'MINISTERIO: {MINISTERIO}')
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        cria_dir_banco = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        cria_dir_html = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/html', exist_ok = True)
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_BD_FINAL}/{MINISTERIO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_BD_FINAL}/{MINISTERIO}/banco')
        print(f'{DIR_BD_FINAL}/{MINISTERIO}/html')
        return (f'{DIR_BD_FINAL}/{MINISTERIO}/banco', f'{DIR_BD_FINAL}/{MINISTERIO}/html', dir_html_ano, REFERENCIAS, ESTILO)

def diretorio_template(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        LOCAL = os.getenv("LOCAL")
        env_dir = load_dotenv(f'{LOCAL}/codigo/govlatinamerica/template-html/.env_var') 
        DIR_BD_FINAL = os.getenv("DIR_BD_FINAL")
        print(f'DIR BD FINAL: {DIR_BD_FINAL}')
        MINISTERIO = os.getenv(str(nome))
        print(f'MINISTERIO: {MINISTERIO}')
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        cria_dir_banco = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        cria_dir_html = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/html', exist_ok = True)
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_BD_FINAL}/{MINISTERIO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_BD_FINAL}/{MINISTERIO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_BD_FINAL}/{MINISTERIO}/banco')
        print(f'{DIR_BD_FINAL}/{MINISTERIO}/html')
        return (f'{DIR_BD_FINAL}/{MINISTERIO}/banco', f'{DIR_BD_FINAL}/{MINISTERIO}/html', dir_html_ano, REFERENCIAS, ESTILO)


