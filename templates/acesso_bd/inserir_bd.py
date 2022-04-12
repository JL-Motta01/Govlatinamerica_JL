""" Para utilizar esse script, é necessário incorporá-lo em um dos repositórios de coleta. 
Por exemplo: govlatinamerica. """
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
from templates.diretorios.diretorio import diretorios

def inserir_bd(env_dir_bd="NA", origem="NA", sigla="NA", classificado="NA", titulo="NA", subtitulo="NA", link="NA", link_archive="NA", data_archive="NA", horario_archive="NA", categoria="NA", data="NA", horario="NA", data_atualizado="NA", horario_atualizado="NA", local="NA", autoria="NA", tags="NA", paragrafos="NA",  nome_arquivo="NA", imagens="NA", dir_bd="NA", dir_arquivo="NA", codigo_bd="NA", extra_01="NA", extra_02="NA", extra_03="NA"):
        print(f'ENV_DIR_BD: {env_dir_bd}')
        DIR_FINAL = diretorios(env_dir_bd)[0]
        print(DIR_FINAL)
        nome_bd_json = env_dir_bd 
        # excluir_json = os.remove(f'{DIR_FINAL}/{nome_bd_json}.json')
        db = TinyDB(f'{DIR_FINAL}/json/{nome_bd_json}.json', indent=4, ensure_ascii = False)
        dir_bd = f'{DIR_FINAL}/json/{nome_bd_json}.json'
        User = Query()
        verifica_bd = db.contains((User.titulo == titulo)&(User.data == data)&(User.horario == horario))
        print(verifica_bd)
        # try:
        if not verifica_bd:
            print("Não está na base")
            db.insert({
                "origem": origem, 
                "sigla": sigla,
                "classificado": classificado,
                "categoria": categoria,
                "autoria": autoria,
                "titulo": titulo,
                "subtitulo": subtitulo,
                "data": data,
                "horario": horario,
                "data_atualizado": data_atualizado,
                "horario_atualizado": horario_atualizado,
                "link": link,
                "link_archive": link_archive,
                "data_archive": data_archive,
                "horario_archive": horario_archive,
                "local": local,
                "tags": tags,
                "paragrafos": paragrafos,
                "nome_arquivo": nome_arquivo,
                "imagens": imagens,
                "dir_bd": dir_bd,
                "dir_arquivo": dir_arquivo,
                "codigo_bd": codigo_bd,
                "extra_01": extra_01, 
                "extra_02": extra_02,
                "extra_03": extra_03
            })
        else:
            print("Já está na base")
        #except:
            #pass

def main():
    inserir_banco = inserir_bd(env_dir_bd, origem, sigla, classificado, titulo, subtitulo, link, link_archive, categoria, data, horario, data_atualizado, horario_atualizado, local, autoria, tags, paragrafos, nome_arquivo, imagens, dir_bd, dir_arquivo, codigo_bd, extra_01, extra_02, extra_03)

if __name__=="__main__":
    main()