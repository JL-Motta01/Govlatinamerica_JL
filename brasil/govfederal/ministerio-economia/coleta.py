from urllib.request import urlopen
from bs4 import BeautifulSoup


def acessar_pagina(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


# def links_navigation(bs): # analisar 
#     navigation = bs.find("div", class_="navigation-content").find_all("a", class_="plain") 
#     lista_a = []  # cria uma lista vazia
#     for a_menu in navigation:
#         lista_a.append(a_menu["href"])  
#     return lista_a

"""
def notas_imprensa(): # check
    url = "https://www.gov.br/economia/pt-br/canais_atendimento/imprensa/notas-a-imprensa" 
    me_pagina = acessar_pagina(url)
    # título
    titulo_notas = me_pagina.find("h1", class_="documentFirstHeading").text
    # datas
    data_post_notas = me_pagina.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
    data_update_notas = me_pagina.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    contador = 0 
    lista_url_notas = []
    while contador < 211:
        dominio = "https://www.gov.br/economia/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
        dominio += str(contador) 
        contador += 30
        lista_url_notas.append(dominio)
    for url_notas in lista_url_notas:
        # conteudo das notas
        conteudo_notas = me_pagina.find("div", id="content-core").find_all("article")
        for article_notas in conteudo_notas:
            link_notas = acessar_pagina(article_notas.h2.a["href"])
            # entrando nas notas
            titulo_notas = link_notas.find("h1").text
            data_notas = link_notas.find("span", class_="documentPublished").find("span", class_="value").text
            corpo_notas = link_notas.find("div", id="content-core").text
            # links notas
            lista_href_notas = []
            try: 
                href_notas = link_notas.find("div", {"id":"category"}).find_all("a")
                for a_notas in href_notas:
                    lista_href_notas.append(a_notas.text)
            except:
                lista_href_notas.append("nota sem links")
            # tags notas
            lista_tags_notas = []
            try: 
                tags_notas = link_notas.find("div", {"id":"category"}).find_all("span")
                for span_notas in tags_notas:
                    lista_tags_notas.append(span_notas.text)
            except:
                lista_tags_notas.append("nota sem tag")
            if lista_tags_notas[0] != 'nota sem tag' :
                del lista_tags_notas[0]


def noticias(): # almost check
    url = "https://www.gov.br/economia/pt-br/assuntos/noticias"
    me_pagina = acessar_pagina(url)
    # título
    titulo_noticias = me_pagina.find("h1", class_="documentFirstHeading").text
    # datas
    data_post_noticias = me_pagina.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
    data_update_noticias = me_pagina.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    contador = 0 
    lista_url_noticias = []
    while contador < 5881:
        dominio = "https://www.gov.br/economia/pt-br/assuntos/noticias?b_size=60&b_start:int="
        dominio += str(contador) 
        contador += 60
        lista_url_noticias.append(dominio)
    for url_noticias in lista_url_noticias:
        # conteudo das noticias
        conteudo_noticias = me_pagina.find("ul", class_="noticias listagem-noticias-com-foto").find_all("li")
        for li_noticias in conteudo_noticias:
            link_noticias = acessar_pagina(li_noticias.div.h2.a["href"])
            # entrando nas noticias
            titulo_noticias = link_noticias.find("h1").text
            data_noticias = link_noticias.find("span", class_="documentPublished").find("span", class_="value").text
            corpo_noticias = link_noticias.find("div", id="content-core").text
            # links noticias
            lista_href_noticias = [] # ajustar EXCEPT
            try: 
                href_noticias = link_noticias.find("div", {"id":"content-core"}).find_all("a")
                for a_noticias in href_noticias:
                    lista_href_noticias.append(a_noticias.text)
            except:
                lista_href_noticias.append("notícia sem links")
"""


def boletins(): # in progress
    url = "https://www.gov.br/economia/pt-br/centrais-de-conteudo/publicacoes/boletins"
    me_pagina = acessar_pagina(url)
    # links 
    lista_links_boletins = []
    links_boletins = me_pagina.find("div", class_="wrapper").find_all("div", class_="card")
    for card_boletins in links_boletins:
        lista_links_boletins.append(card_boletins.a["href"])
    if lista_links_boletins[0]: # check
        boletins_admin = acessar_pagina(lista_links_boletins[0])
        # título
        titulo_boletins_admin = boletins_admin.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_boletins_admin = boletins_admin.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_boletins_admin = boletins_admin.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_boletins_admin = boletins_admin.find("div", id="content-core").text
        # links
        lista_links_boletins_admin = []
        links_boletins_admin = boletins_admin.find("div", id="content-core").find_all("article")
        for article_boletins in links_boletins_admin:
            lista_links_boletins_admin.append(article_boletins.h2.a["href"])
    if lista_links_boletins[1]: # check
        boletins_empresas = acessar_pagina(lista_links_boletins[1])
        # título
        titulo_boletins_empresas = boletins_empresas.find("h2", class_="outstanding-title").text
        # conteúdo
        conteudo_boletins_empresas = boletins_empresas.find("div", class_="cover-richtext-tile tile-content").text
        # links
        lista_links_boletins_empresas = []
        links_boletins_empresas = boletins_empresas.find("div", class_="cover-collection-tile tile-content").find_all("h2")
        for h2_boletins in links_boletins_empresas:
            lista_links_boletins_empresas.append(h2_boletins.a["href"])
    if lista_links_boletins[2]: # check
        boletins_empresas_dep = acessar_pagina(lista_links_boletins[2])
        # título
        titulo_boletins_empresas_dep = boletins_empresas_dep.find("h2", class_="outstanding-title").text
        # conteúdo
        conteudo_boletins_empresas_dep = boletins_empresas_dep.find("div", class_="cover-richtext-tile tile-content").text
        # links
        lista_links_boletins_empresas_dep = []
        links_boletins_empresas_dep = boletins_empresas_dep.find("div", class_="cover-collection-tile tile-content").find_all("h2")
        for h2_boletins in links_boletins_empresas_dep:
            lista_links_boletins_empresas_dep.append(h2_boletins.a["href"])
    if lista_links_boletins[3]: # almost check
        boletins_covid = acessar_pagina(lista_links_boletins[3])
        # título
        titulo_boletins_covid = boletins_covid.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_boletins_covid = boletins_covid.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_boletins_covid = boletins_covid.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        contador = 0 
        lista_url_boletins_covid = []
        while contador < 331:
            dominio = "https://www.gov.br/economia/pt-br/centrais-de-conteudo/publicacoes/boletins/covid-19?b_start:int="
            dominio += str(contador) 
            contador += 30
            lista_url_boletins_covid.append(dominio)
        for url_boletins_covid in lista_url_boletins_covid: # SÓ COLETA DA PRIMEIRA PÁGINA 
            # conteúdo
            conteudo_boletins_covid = boletins_covid.find("div", id="content-core").text
            # links
            lista_links_boletins_covid = []
            links_boletins_covid = boletins_covid.find("div", id="content-core").find_all("article")
            for article_boletins in links_boletins_covid:
                lista_links_boletins_covid.append(article_boletins.h2.a["href"])
    if lista_links_boletins[4]: # check
        boletins_loterias = acessar_pagina(lista_links_boletins[4])
        # título
        titulo_boletins_loterias = boletins_loterias.find("h2", class_="outstanding-title").text
        # conteúdo
        conteudo_boletins_loterias = boletins_loterias.find("div", class_="cover-richtext-tile tile-content").text
        # links
        lista_links_boletins_loterias = []
        links_boletins_loterias = boletins_loterias.find("div", class_="cover-collection-tile tile-content").find_all("h2")
        for h2_boletins in links_boletins_loterias:
            lista_links_boletins_loterias.append(h2_boletins.a["href"])
    if lista_links_boletins[5]: # in progress
        boletins_estrangeiros = acessar_pagina(lista_links_boletins[5])
        # título
        titulo_boletins_estrangeiros = boletins_estrangeiros.find("div", class_="cover-richtext-tile tile-content").find("strong").text
        # conteúdo
        lista_conteudo_boletins_estrangeiros = []
        conteudo_boletins_estrangeiros = boletins_estrangeiros.find("div", {"id":"content"}).find_all("div", class_="row")
        for row_boletins in conteudo_boletins_estrangeiros:
            lista_conteudo_boletins_estrangeiros.append(row_boletins.text)
        # TODOS OS ROWS ESTÃO COMO ITEM ÚNICO DA LISTA - SEPARAR
    if lista_links_boletins[6]: # check
        boletins_custeio = acessar_pagina(lista_links_boletins[6])
        # links 
        lista_links_boletins_custeio = []
        links_boletins_custeio = boletins_custeio.find("div", class_="wrapper").find_all("div", class_="card")
        for card_boletins_custeio in links_boletins_custeio:
            lista_links_boletins_custeio.append(card_boletins_custeio.a["href"])
        if lista_links_boletins_custeio[0]: # check
            boletins_custeio_notas = acessar_pagina(lista_links_boletins_custeio[0])
            # título
            titulo_boletins_custeio_notas = boletins_custeio_notas.find("h1", class_="documentFirstHeading").text
            # datas
            data_post_boletins_custeio_notas = boletins_custeio_notas.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
            data_update_boletins_custeio_notas = boletins_custeio_notas.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
            # conteúdo
            conteudo_boletins_custeio_notas = boletins_custeio_notas.find("div", {"id" : "content-core"}).text
            # links
            lista_links_boletins_custeio_notas = []
            links_boletins_custeio_notas = boletins_custeio_notas.find("div", {"id" : "content-core"}).find_all("h2")
            for h2_boletins_custeio_notas in links_boletins_custeio_notas:
                lista_links_boletins_custeio_notas.append(h2_boletins_custeio_notas.a["href"])
        if lista_links_boletins_custeio[1]: # check
            boletins_custeio_tri = acessar_pagina(lista_links_boletins_custeio[1])
            # links 
            lista_links_boletins_custeio_tri = []
            links_boletins_custeio_tri = boletins_custeio_tri.find("div", class_="wrapper").find_all("div", class_="card")
            for card_boletins_custeio_tri in links_boletins_custeio_tri:
                lista_links_boletins_custeio_tri.append(card_boletins_custeio_tri.a["href"])
            if lista_links_boletins_custeio_tri[0]: # check
                boletins_custeio_tri2021 = acessar_pagina(lista_links_boletins_custeio_tri[0])
                # título
                titulo_boletins_custeio_tri2021 = boletins_custeio_tri2021.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_tri2021 = boletins_custeio_tri2021.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_tri2021 = boletins_custeio_tri2021.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_tri2021 = boletins_custeio_tri2021.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_tri2021 = []
                links_boletins_custeio_tri2021 = boletins_custeio_tri2021.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_tri2021 in links_boletins_custeio_tri2021:
                    lista_links_boletins_custeio_tri2021.append(h2_boletins_custeio_tri2021.a["href"])
            if lista_links_boletins_custeio_tri[1]: # check
                boletins_custeio_tri2020 = acessar_pagina(lista_links_boletins_custeio_tri[1])
                # título
                titulo_boletins_custeio_tri2020 = boletins_custeio_tri2020.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_tri2020 = boletins_custeio_tri2020.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_tri2020 = boletins_custeio_tri2020.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_tri2020 = boletins_custeio_tri2020.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_tri2020 = []
                links_boletins_custeio_tri2020 = boletins_custeio_tri2020.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_tri2020 in links_boletins_custeio_tri2020:
                    lista_links_boletins_custeio_tri2020.append(h2_boletins_custeio_tri2020.a["href"])
            if lista_links_boletins_custeio_tri[2]: # check
                boletins_custeio_tri2019 = acessar_pagina(lista_links_boletins_custeio_tri[2])
                # título
                titulo_boletins_custeio_tri2019 = boletins_custeio_tri2019.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_tri2019 = boletins_custeio_tri2019.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_tri2019 = boletins_custeio_tri2019.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_tri2019 = boletins_custeio_tri2019.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_tri2019 = []
                links_boletins_custeio_tri2019 = boletins_custeio_tri2019.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_tri2019 in links_boletins_custeio_tri2019:
                    lista_links_boletins_custeio_tri2019.append(h2_boletins_custeio_tri2019.a["href"])
            if lista_links_boletins_custeio_tri[3]: # check
                boletins_custeio_tri2018 = acessar_pagina(lista_links_boletins_custeio_tri[3])
                # título
                titulo_boletins_custeio_tri2018 = boletins_custeio_tri2018.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_tri2018 = boletins_custeio_tri2018.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_tri2018 = boletins_custeio_tri2018.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_tri2018 = boletins_custeio_tri2018.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_tri2018 = []
                links_boletins_custeio_tri2018 = boletins_custeio_tri2018.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_tri2018 in links_boletins_custeio_tri2018:
                    lista_links_boletins_custeio_tri2018.append(h2_boletins_custeio_tri2018.a["href"])
            if lista_links_boletins_custeio_tri[4]: # check
                boletins_custeio_tri2017 = acessar_pagina(lista_links_boletins_custeio_tri[4])
                # título
                titulo_boletins_custeio_tri2017 = boletins_custeio_tri2017.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_tri2017 = boletins_custeio_tri2017.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_tri2017 = boletins_custeio_tri2017.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_tri2017 = boletins_custeio_tri2017.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_tri2017 = []
                links_boletins_custeio_tri2017 = boletins_custeio_tri2017.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_tri2017 in links_boletins_custeio_tri2017:
                    lista_links_boletins_custeio_tri2017.append(h2_boletins_custeio_tri2017.a["href"])
            if lista_links_boletins_custeio_tri[5]: # check
                boletins_custeio_tri2016 = acessar_pagina(lista_links_boletins_custeio_tri[5])
                # título
                titulo_boletins_custeio_tri2016 = boletins_custeio_tri2016.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_tri2016 = boletins_custeio_tri2016.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_tri2016 = boletins_custeio_tri2016.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_tri2016 = boletins_custeio_tri2016.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_tri2016 = []
                links_boletins_custeio_tri2016 = boletins_custeio_tri2016.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_tri2016 in links_boletins_custeio_tri2016:
                    lista_links_boletins_custeio_tri2016.append(h2_boletins_custeio_tri2016.a["href"])
        if lista_links_boletins_custeio[2]: # check
            boletins_custeio_despesa = acessar_pagina(lista_links_boletins_custeio[2])
            # links 
            lista_links_boletins_custeio_despesa = []
            links_boletins_custeio_despesa = boletins_custeio_despesa.find("div", class_="wrapper").find_all("div", class_="card")
            for card_boletins_custeio_despesa in links_boletins_custeio_despesa:
                lista_links_boletins_custeio_despesa.append(card_boletins_custeio_despesa.a["href"])
            if lista_links_boletins_custeio_despesa[0]: # check
                boletins_custeio_despesa_atualizada = acessar_pagina(lista_links_boletins_custeio_despesa[0])
                # título
                titulo_boletins_custeio_despesa_atualizada = boletins_custeio_despesa_atualizada.find("h1", class_="documentFirstHeading").text
                # datas
                data_post_boletins_custeio_despesa_atualizada = boletins_custeio_despesa_atualizada.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                data_update_boletins_custeio_despesa_atualizada = boletins_custeio_despesa_atualizada.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                # conteúdo
                conteudo_boletins_custeio_despesa_atualizada = boletins_custeio_despesa_atualizada.find("div", {"id" : "content-core"}).text
                # links
                lista_links_boletins_custeio_despesa_atualizada = []
                links_boletins_custeio_despesa_atualizada = boletins_custeio_despesa_atualizada.find("div", {"id" : "content-core"}).find_all("h2")
                for h2_boletins_custeio_despesa_atualizada in links_boletins_custeio_despesa_atualizada:
                    lista_links_boletins_custeio_despesa_atualizada.append(h2_boletins_custeio_despesa_atualizada.a["href"])
            if lista_links_boletins_custeio_despesa[1]: # check
                boletins_custeio_despesa_anterior = acessar_pagina(lista_links_boletins_custeio_despesa[1])
                # links 
                lista_links_boletins_custeio_despesa_anterior = []
                links_boletins_custeio_despesa_anterior = boletins_custeio_despesa_anterior.find("div", class_="wrapper").find_all("div", class_="card")
                for card_boletins_custeio_despesa_anterior in links_boletins_custeio_despesa_anterior:
                    lista_links_boletins_custeio_despesa_anterior.append(card_boletins_custeio_despesa_anterior.a["href"])
                if lista_links_boletins_custeio_despesa_anterior[0]: # check
                    boletins_custeio_despesa_anterior_2021 = acessar_pagina(lista_links_boletins_custeio_despesa_anterior[0])
                    # título
                    titulo_boletins_custeio_despesa_anterior_2021 = boletins_custeio_despesa_anterior_2021.find("h1", class_="documentFirstHeading").text
                    # datas
                    data_post_boletins_custeio_despesa_anterior_2021 = boletins_custeio_despesa_anterior_2021.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                    data_update_boletins_custeio_despesa_anterior_2021 = boletins_custeio_despesa_anterior_2021.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                    # conteúdo
                    conteudo_boletins_custeio_despesa_anterior_2021 = boletins_custeio_despesa_anterior_2021.find("div", {"id" : "content-core"}).text
                    # links
                    lista_links_boletins_custeio_despesa_anterior_2021 = []
                    links_boletins_custeio_despesa_anterior_2021 = boletins_custeio_despesa_anterior_2021.find("div", {"id" : "content-core"}).find_all("h2")
                    for h2_boletins_custeio_despesa_anterior_2021 in links_boletins_custeio_despesa_anterior_2021:
                        lista_links_boletins_custeio_despesa_anterior_2021.append(h2_boletins_custeio_despesa_anterior_2021.a["href"])
                if lista_links_boletins_custeio_despesa_anterior[1]: # check
                    boletins_custeio_despesa_anterior_2020 = acessar_pagina(lista_links_boletins_custeio_despesa_anterior[1])
                    # título
                    titulo_boletins_custeio_despesa_anterior_2020 = boletins_custeio_despesa_anterior_2020.find("h1", class_="documentFirstHeading").text
                    # datas
                    data_post_boletins_custeio_despesa_anterior_2020 = boletins_custeio_despesa_anterior_2020.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                    data_update_boletins_custeio_despesa_anterior_2020 = boletins_custeio_despesa_anterior_2020.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                    # conteúdo
                    conteudo_boletins_custeio_despesa_anterior_2020 = boletins_custeio_despesa_anterior_2020.find("div", {"id" : "content-core"}).text
                    # links
                    lista_links_boletins_custeio_despesa_anterior_2020 = []
                    links_boletins_custeio_despesa_anterior_2020 = boletins_custeio_despesa_anterior_2020.find("div", {"id" : "content-core"}).find_all("h2")
                    for h2_boletins_custeio_despesa_anterior_2020 in links_boletins_custeio_despesa_anterior_2020:
                        lista_links_boletins_custeio_despesa_anterior_2020.append(h2_boletins_custeio_despesa_anterior_2020.a["href"])
                if lista_links_boletins_custeio_despesa_anterior[2]: # check
                    boletins_custeio_despesa_anterior_2019 = acessar_pagina(lista_links_boletins_custeio_despesa_anterior[2])
                    # título
                    titulo_boletins_custeio_despesa_anterior_2019 = boletins_custeio_despesa_anterior_2019.find("h1", class_="documentFirstHeading").text
                    # datas
                    data_post_boletins_custeio_despesa_anterior_2019 = boletins_custeio_despesa_anterior_2019.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                    data_update_boletins_custeio_despesa_anterior_2019 = boletins_custeio_despesa_anterior_2019.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                    # conteúdo
                    conteudo_boletins_custeio_despesa_anterior_2019 = boletins_custeio_despesa_anterior_2019.find("div", {"id" : "content-core"}).text
                    # links
                    lista_links_boletins_custeio_despesa_anterior_2019 = []
                    links_boletins_custeio_despesa_anterior_2019 = boletins_custeio_despesa_anterior_2019.find("div", {"id" : "content-core"}).find_all("h2")
                    for h2_boletins_custeio_despesa_anterior_2019 in links_boletins_custeio_despesa_anterior_2019:
                        lista_links_boletins_custeio_despesa_anterior_2019.append(h2_boletins_custeio_despesa_anterior_2019.a["href"])
                if lista_links_boletins_custeio_despesa_anterior[3]: # check
                    boletins_custeio_despesa_anterior_2018 = acessar_pagina(lista_links_boletins_custeio_despesa_anterior[3])
                    # título
                    titulo_boletins_custeio_despesa_anterior_2018 = boletins_custeio_despesa_anterior_2018.find("h1", class_="documentFirstHeading").text
                    # datas
                    data_post_boletins_custeio_despesa_anterior_2018 = boletins_custeio_despesa_anterior_2018.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                    data_update_boletins_custeio_despesa_anterior_2018 = boletins_custeio_despesa_anterior_2018.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                    # conteúdo
                    conteudo_boletins_custeio_despesa_anterior_2018 = boletins_custeio_despesa_anterior_2018.find("div", {"id" : "content-core"}).text
                    # links
                    lista_links_boletins_custeio_despesa_anterior_2018 = []
                    links_boletins_custeio_despesa_anterior_2018 = boletins_custeio_despesa_anterior_2018.find("div", {"id" : "content-core"}).find_all("h2")
                    for h2_boletins_custeio_despesa_anterior_2018 in links_boletins_custeio_despesa_anterior_2018:
                        lista_links_boletins_custeio_despesa_anterior_2018.append(h2_boletins_custeio_despesa_anterior_2018.a["href"])
                if lista_links_boletins_custeio_despesa_anterior[4]: # check
                    boletins_custeio_despesa_anterior_2017 = acessar_pagina(lista_links_boletins_custeio_despesa_anterior[4])
                    # título
                    titulo_boletins_custeio_despesa_anterior_2017 = boletins_custeio_despesa_anterior_2017.find("h1", class_="documentFirstHeading").text
                    # datas
                    data_post_boletins_custeio_despesa_anterior_2017 = boletins_custeio_despesa_anterior_2017.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                    data_update_boletins_custeio_despesa_anterior_2017 = boletins_custeio_despesa_anterior_2017.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                    # conteúdo
                    conteudo_boletins_custeio_despesa_anterior_2017 = boletins_custeio_despesa_anterior_2017.find("div", {"id" : "content-core"}).text
                    # links
                    lista_links_boletins_custeio_despesa_anterior_2017 = []
                    links_boletins_custeio_despesa_anterior_2017 = boletins_custeio_despesa_anterior_2017.find("div", {"id" : "content-core"}).find_all("h2")
                    for h2_boletins_custeio_despesa_anterior_2017 in links_boletins_custeio_despesa_anterior_2017:
                        lista_links_boletins_custeio_despesa_anterior_2017.append(h2_boletins_custeio_despesa_anterior_2017.a["href"])
                if lista_links_boletins_custeio_despesa_anterior[5]: # check
                    boletins_custeio_despesa_anterior_2016 = acessar_pagina(lista_links_boletins_custeio_despesa_anterior[5])
                    # título
                    titulo_boletins_custeio_despesa_anterior_2016 = boletins_custeio_despesa_anterior_2016.find("h1", class_="documentFirstHeading").text
                    # datas
                    data_post_boletins_custeio_despesa_anterior_2016 = boletins_custeio_despesa_anterior_2016.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
                    data_update_boletins_custeio_despesa_anterior_2016 = boletins_custeio_despesa_anterior_2016.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
                    # conteúdo
                    conteudo_boletins_custeio_despesa_anterior_2016 = boletins_custeio_despesa_anterior_2016.find("div", {"id" : "content-core"}).text
                    # links
                    lista_links_boletins_custeio_despesa_anterior_2016 = []
                    links_boletins_custeio_despesa_anterior_2016 = boletins_custeio_despesa_anterior_2016.find("div", {"id" : "content-core"}).find_all("h2")
                    for h2_boletins_custeio_despesa_anterior_2016 in links_boletins_custeio_despesa_anterior_2016:
                        lista_links_boletins_custeio_despesa_anterior_2016.append(h2_boletins_custeio_despesa_anterior_2016.a["href"])
    if lista_links_boletins[7]: # in progress
        boletins_incentivado = acessar_pagina(lista_links_boletins[7])


"""
def cartilhas():
    url = links_navigation(bs)[6]
    me_pagina = acessar_pagina(url)


def estudos_notas():
    url = links_navigation(bs)[6]
    me_pagina = acessar_pagina(url)


def planilhas():
    url = links_navigation(bs)[6]
    me_pagina = acessar_pagina(url)


def relatorios():
    url = links_navigation(bs)[6]
    me_pagina = acessar_pagina(url)


def auditorias():
    url = links_navigation(bs)[4]
    me_pagina = acessar_pagina(url)
"""


def main():
    global bs
    url = "https://www.gov.br/economia/pt-br"
    bs = acessar_pagina(url)  
    # navigation = links_navigation(bs)
    # me_notas_imprensa = notas_imprensa()
    # me_noticias = noticias()
    me_boletins = boletins()


if __name__ == "__main__":
    main()
