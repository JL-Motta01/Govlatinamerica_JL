from dotenv import load_dotenv
import os

def diretorio(nome, ano="NA"):
        """ para rodar o template html no computador local, substituir a variável DIR_BD_FINAL por DIR_CONFIG """
        print(f'NOME: {nome}')
        env_dir = load_dotenv("/home/labri_cintiaiorio/codigo/govlatinamerica/template-html/.env_var") 
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

