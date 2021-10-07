from os import name
from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

# TODO
# Organizar o codigo em funções
# resolver bio com tag p vazias
# gerar html da bio e do discurso de posse

"""
# Realização de requisição de pagina web
# atraves da biblioteca urllib (requests)
"""
url = 'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores'
html = urlopen(url)

"""
# parseamento e extração das imformações da pagina web através do biblioteca BeautifulSoup

"""
bs = BeautifulSoup(html.read(), 'html.parser')
info_ministros = bs.find_all('p')  # ['p1','p2','p3'...]

# pprint(info_ministros)


def main():
    # sublistas com info tag_p ministros
    tag_p_lista_de_ministros = tag_p_ministros()
    # pprint(tag_p_lista_de_ministros)
    # tupla com duas listas: links posse e bio >> ([link_posse1,link_posse2...], [link_bio1, link_bio2..])
    tag_p_discursos_e_bio = link_discurso_e_bio()
    # pprint(tag_p_discursos_e_bio)
    # lista com paragrafos de bio dos ministros. Necessita receber argumento da função link_discurso_e_bio()
    paragrafos_ministros_bio = paragrafo_bio(tag_p_discursos_e_bio[1])
    # pprint(paragrafos_ministros_bio)
    # # sublistas com paragrafos de posse
    paragrafos_discursos_posse = paragrafos_discursos_de_posse()
    pprint(paragrafos_discursos_posse)

    # lista_ministro_normalizada = lista_ministros_normalizada()
    # print(lista_ministro_normalizada)
    # dataframe_discursos = extrair_e_dataframe()
    # print(dataframe_discursos)


def tag_p_ministros():
    """
    Extrai informações das tag p e insere em uma lista
    Exemplo:
    [['31/03/2021', 'Carlos Alberto Franco França', 'Discurso de posse', 
    'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores?layout=edit&id=449', 
    'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores?layout=edit&id=450'], 
    ['02/01/2019', 'Ernesto Araújo', 
    'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores/422']]

    """
    texto = []
    for info_ministro in info_ministros:
        info_ministro = str(info_ministro)
        bsi = BeautifulSoup(info_ministro, "lxml")

        tmp = []
        # extrai textos dos paragrafos
        for string in bsi.stripped_strings:
            palavras = repr(string)
            tmp.append(palavras)

        # extrai links dos paragrafos
        for link in bsi.find_all("a"):
            links = urllib.parse.urljoin(url, link['href'])
            tmp.append(links)
        texto.append(tmp)

    texto2 = texto

    # https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/
    # retira strings de lista de lista
    # https://stackoverflow.com/questions/19220554/python-remove-elements-from-nested-lists
    texto2 = [[i for i in texto if i != "'|'"] for texto in texto2]
    texto2 = [[i for i in texto if i != "'-'"] for texto in texto2]
    # retira caracter de lista de lista
    # https://stackoverflow.com/questions/31794610/removing-a-character-from-a-string-in-a-list-of-lists
    texto2 = [[item.replace("'", "") for item in texto] for texto in texto2]

    lista_ministros = texto2[4:-3]
    return lista_ministros


def link_discurso_e_bio():
    """link de discursos e bio"""
    lista_ministros = tag_p_ministros()

    lista_ministro_bio = []
    lista_ministro_discurso_posse = []
    for ministro in lista_ministros:
        # discursos de posse + link do discurso para posse para bs
        if ministro[2] == 'Discurso de posse':
            lista_ministro_discurso_posse.append(ministro[-1])
        elif ministro[2] != 'Discurso de posse':
            lista_ministro_discurso_posse.append("NA")

        if ministro[2] != 'Discurso de posse':
            lista_ministro_bio.append(ministro[-1])
        elif ministro[2] == 'Discurso de posse':
            lista_ministro_bio.append(ministro[-2])
    return lista_ministro_discurso_posse, lista_ministro_bio


def paragrafo_bio(lista_ministro_bio):
    """Obter paragrafos relativos a biografia dos ministros"""
    ministro_bio_paragrafo = []
    for ministro_bio in lista_ministro_bio:
        # print(type(ministro_bio))
        url = ministro_bio
        html = urlopen(url)
        bsBio = BeautifulSoup(html.read(), 'html.parser')
        # pprint(bsBio)
        bio = bsBio.find('div', attrs={"class": "item-page"})
        for p in bio.find_all('p'):
            if len(p.get_text(strip=True)) == 0:
                p = p.extract()
            else:
                p = p.get_text(strip=True)
                if 'Nascido' in p:
                    p.split('Nascido')[1]
                elif 'Nasceu' in p:
                    p.split('Nasceu')[1]
                ministro_bio_paragrafo.append(p)

    ministro_bio_paragrafo = [el.replace(
        '\xad', '') for el in ministro_bio_paragrafo]

    print(ministro_bio_paragrafo)


def paragrafos_discursos_de_posse():
    """Obter sublistas com paragrafos de discursos de posse"""
    ministro_discurso_posse_paragrafos = []
    lista_ministro_discurso_posse = link_discurso_e_bio()[0]
    print(lista_ministro_discurso_posse)
    for ministro_discurso_posse in lista_ministro_discurso_posse:
        try:
            url = ministro_discurso_posse
            html = urlopen(url)
            bsPosse = BeautifulSoup(html.read(), 'html.parser')
            d_posse = bsPosse.find('div', attrs={"class": "item-page"})

            p_d_posse = []
            for p in d_posse.find_all('p'):

                if p.find('strong'):
                    pass
                else:
                    # https://stackoverflow.com/questions/10993612/
                    p_d_posse.append(p.get_text(strip=True))
            p_d_posse = [el.replace('\xa0', ' ') for el in p_d_posse]
            p_d_posse = [string for string in p_d_posse if string != ""]
            ministro_discurso_posse_paragrafos.append(p_d_posse)

        except:
            ministro_discurso_posse_paragrafos.append(ministro_discurso_posse)
    return ministro_discurso_posse_paragrafos


def lista_ministros_normalizada():
    """
    Exemplo:
    [['31/03/2021', 'Carlos Alberto Franco França', 'Discurso de posse', 
    'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores?layout=edit&id=449', 
    'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores?layout=edit&id=450'], 
    ['02/01/2019', 'Ernesto Araújo', 
    'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores/422']]
    """
    lista_ministros = tag_p_ministros()
    elemento = "Discurso de posse"
    insert_na = "NA"
    # https://stackoverflow.com/questions/66671363/find-an-element-in-a-sub-list-and-when-this-element-is-found-append-all-other
    nova_lista_ministros = []
    for sublista in lista_ministros:
        if elemento in sublista:
            # sublista = [data, nome_ministro, YES, link_bio, link_p_posse]
            sublista[2] = "YES"
            nova_lista_ministros.append(sublista)
        else:
            #sublista = [data, nome_ministro, NA, link_bio, NA]
            sublista[2:2] = ["NA"]
            sublista[4:4] = ["NA"]
            nova_lista_ministros.append(sublista)

    return nova_lista_ministros


def extrair_e_dataframe():
    def Extract(lst, i):
        x = i
        return [item[x] for item in lst]

    data = Extract(nova_lista_ministros, 0)
    ministro = Extract(nova_lista_ministros, 1)
    discurso_posse = Extract(nova_lista_ministros, 2)
    link_bio = Extract(nova_lista_ministros, 3)
    link_discurso = Extract(nova_lista_ministros, 4)

    df = pd.DataFrame({
        'data': data,
        'ministro': ministro,
        'discurso_posse': discurso_posse,
        'ministro_discurso_posse_paragrafos': ministro_discurso_posse_paragrafos,
        'ministro_bio_paragrafo': ministro_bio_paragrafo,
        'link_bio': link_bio,
        'link_discurso': link_discurso,
    })
    df.to_csv('discursos.csv')
    print(df.head())
    # print(df.to_string())


if __name__ == "__main__":
    main()
