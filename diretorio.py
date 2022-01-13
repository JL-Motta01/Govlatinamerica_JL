from dotenv import load_dotenv
import os

def diretorio(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_CONFIG por DIR_CONFIG """
        print(f'NOME: {nome}')
        env_dir = load_dotenv(".env_var") 
        DIR_CONFIG = os.getenv("DIR_CONFIG")
        print(f'DIR BD FINAL: {DIR_CONFIG}')
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

