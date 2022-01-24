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
from diretorios.diretorio import diretorios

def inserir_bd(env_ministerio="NA", origem="NA", classificado="NA", titulo="NA", subtitulo="NA", link="NA", link_archive="NA", data_archive="NA", horario_archive="NA", categoria="NA", data="NA", horario="NA", data_atualizado="NA", horario_atualizado="NA", local="NA", autoria="NA", tags="NA", paragrafos="NA", dir_local="NA", extra_01="NA", extra_02="NA", extra_03="NA"):
        print(f'ENV MINISTERIO: {env_ministerio}')
        DIR_FINAL = diretorios(env_ministerio)[0]
        print(DIR_FINAL)
        nome_bd_json = env_ministerio 
        # excluir_json = os.remove(f'{DIR_FINAL}/{nome_bd_json}.json')
        db = TinyDB(f'{DIR_FINAL}/{nome_bd_json}.json', indent=4, ensure_ascii = False)
        dir_local = f'{DIR_FINAL}/{nome_bd_json}.json'
        User = Query()
        verifica_bd = db.contains((User.titulo == titulo)&(User.data == data)&(User.horario == horario))
        print(verifica_bd)
        try:
            if not verifica_bd:
                print("Não está na base")
                db.insert({
                    "origem": origem, 
                    "classificado": classificado,
                    "titulo": titulo,
                    "subtitulo": subtitulo,
                    "link": link,
                    "link_archive": link_archive,
                    "data_archive": data_archive,
                    "horario_archive": horario_archive,
                    "categoria": categoria,
                    "data": data,
                    "horario": horario,
                    "data_atualizado": data_atualizado,
                    "horario_atualizado": horario_atualizado,
                    "local": local,
                    "autoria": autoria,
                    "tags": tags,
                    "paragrafos": paragrafos,
                    "dir_local": dir_local,
                    "extra_01": "NA", # categoria_link
                    "extra_02": "NA",
                    "extra_03": "NA"
                })
            else:
                print("Já está na base")
        except:
            pass

def main():
    inserir_banco = inserir_bd(env_ministerio, origem, classificado, titulo, subtitulo, link, link_archive, categoria, data, horario, data_atualizado, horario_atualizado, local, autoria, tags, paragrafos, dir_local, extra_01, extra_02, extra_03)

if __name__=="__main__":
    main()