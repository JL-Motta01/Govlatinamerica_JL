
from tinydb import TinyDB, Query
from pprint import pprint
from pagina_html import get_html


def consultar():
    db = TinyDB('/home/lantri_rafael/codigo/govlatinamerica/template/db_artigo.json')
    myDBQuery = Query()
    for dado in iter(db):
        print(dado['link'])
        print("#################")
        file = dado['titulo']
        file += ".html"
        with open(f"/home/lantri_rafael/codigo/govlatinamerica/template/html/{file}", "w") as f:
            f.write(get_html(dado))



def main():
    consulta = consultar()


if __name__ == '__main__':
    main()