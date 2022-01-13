from dotenv import load_dotenv
import os

def diretorio(nome, ano="NA"):
        env_dir = load_dotenv(".env_var") 
        DIR_FINAL = os.getenv("DIR_FINAL")
        MINISTERIO = os.getenv(nome)
        REFERENCIAS = os.getenv("REFERENCIAS")
        ESTILO = os.getenv("ESTILO")
        cria_dir_banco = os.makedirs(f'{DIR_FINAL}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        cria_dir_html = os.makedirs(f'{DIR_FINAL}/{MINISTERIO}/html', exist_ok = True)
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_FINAL}/{MINISTERIO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_FINAL}/{MINISTERIO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_FINAL}/{MINISTERIO}/banco')
        print(f'{DIR_FINAL}/{MINISTERIO}/html')
        return (f'{DIR_FINAL}/{MINISTERIO}/banco', f'{DIR_FINAL}/{MINISTERIO}/html', dir_html_ano, REFERENCIAS, ESTILO)

