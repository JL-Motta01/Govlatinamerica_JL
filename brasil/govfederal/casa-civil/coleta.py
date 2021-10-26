from urllib.request import urlopen
# ativa a biblioteca nativa do python
from bs4 import BeautifulSoup
# ativa a biblioteca de terceiros que percorre a página, extraindo infos que queremos


def acessar_pagina(url):
    html = urlopen(url)  # irá retornar a página da função links_cards
    # chama a página
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    # percorre os elementos que queremos
    return bsoup


def links_cards(bs):
    cards = bs.find("div", class_="wrapper").find_all("div", class_="card")  # passa em lista
    lista_cards = []  # cria uma lista vazia
    for card in cards:
        lista_cards.append(card.a["href"])  # coloca dentro da lista vazia
    return lista_cards


def noticias(bs):
    noticias = links_cards(bs)[0]


def notas_oficiais():
    url = links_cards(bs)[1]
    cc_pagina = acessar_pagina(url)


def comunicados_interministeriais():
    url = links_cards(bs)[2]
    cc_pagina = acessar_pagina(url)
    # título
    titulo_comunicados = cc_pagina.find("h1", class_="documentFirstHeading").text
    # datas
    data_post_comunicados = cc_pagina.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
    data_update_comunicados = cc_pagina.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    # links
    contador = 0 
    lista_links_comunicados = []
    while contador < 271:
        dominio = "https://www.gov.br/casacivil/pt-br/assuntos/comunicados-interministeriais?b_start:int="
        dominio += str(contador) # montando a url / str, transformando numero em string
        contador += 30
        lista_links_comunicados.append(dominio)
    for links_comunicados in lista_links_comunicados:
        # links comunicados 
        conteudo_links_comunicados = cc_pagina.find("div", id="content-core").find_all("article")
        for article_comunicados in conteudo_links_comunicados:
            links_article_comunicados = acessar_pagina(article_comunicados.h2.a["href"])
            # entrando nos comunicados
            titulo_article_comunicados = links_article_comunicados.find("h1").text
            data_article_comunicados = links_article_comunicados.find("span", class_="documentModified").find("span", class_="value").text
            conteudo_article_comunicados = links_article_comunicados.find("div", id="content-core").text
            lista_link_conteudo_article_comunicados = []
            link_conteudo_article_comunicados = links_article_comunicados.find("div", id="content-core").find_all("a")
            for a_conteudo_article_comunicados in link_conteudo_article_comunicados:
                lista_link_conteudo_article_comunicados.append(a_conteudo_article_comunicados["href"])


def boletins_cc(): # in progress - almost check
    url = links_cards(bs)[3]
    cc_pagina = acessar_pagina(url)
    # título
    titulo_boletins = cc_pagina.find("h1", class_="documentFirstHeading").text
    # datas
    data_post_boletins = cc_pagina.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
    data_update_boletins = cc_pagina.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    # links
    contador = 0 
    lista_links_boletins = []
    while contador < 91:
        dominio = "https://www.gov.br/casacivil/pt-br/assuntos/audios-boletins-casa-civil?b_start:int="
        dominio += str(contador) # montando a url / str, transformando numero em string
        contador += 30
        lista_links_boletins.append(dominio)
    for links_boletins in lista_links_boletins:
        # links boletins 
        conteudo_links_boletins = cc_pagina.find("div", id="content-core").find_all("article")
        for article_boletins in conteudo_links_boletins:
            links_article_boletins = acessar_pagina(article_boletins.h2.a["href"])
            # entrando no boletim
            titulo_article_boletins = links_article_boletins.find("h1").text
            data_article_boletins = links_article_boletins.find("span", class_="documentPublished").find("span", class_="value").text
            conteudo_article_boletins = links_article_boletins.find("div", id="content-core").text
            # coletando áudios
            # site externo: https://anchor.fm/casacivilbr/episodes
            # tag audio
        

def periodicos_mensais(): # check
    url = links_cards(bs)[4]
    cc_pagina = acessar_pagina(url)
    # título
    titulo_periodicos = cc_pagina.find("h1", class_="documentFirstHeading").text
    # datas
    data_post_periodicos = cc_pagina.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
    data_update_periodicos = cc_pagina.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    conteudo_periodicos = cc_pagina.find("div", id="content-core").text
    # links
    lista_links_periodicos = []
    links_periodicos = cc_pagina.find("div", id="content-core").find_all("a")
    for a in links_periodicos:
        lista_links_periodicos.append(a["href"])


def relacionamento_externo(): # in progress - almost check
    url = links_cards(bs)[5]
    cc_pagina = acessar_pagina(url)
    # imagens da página
    lista_imagens_rexterno = []
    imagens_rexterno = cc_pagina.find("div", id="content").find_all("img")
    for img in imagens_rexterno:
        lista_imagens_rexterno.append(img["src"])
    # links 
    lista_links_rexterno = []
    links_rexterno = cc_pagina.find("div", id="content").find_all("a")
    for a in links_rexterno:
        lista_links_rexterno.append(a["href"])
    if lista_links_rexterno[0]: # in progress - almost done
        sobre_rexterno = acessar_pagina(lista_links_rexterno[0])
        # título
        titulo_sobre_rexterno = sobre_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_sobre_rexterno = sobre_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_sobre_rexterno = sobre_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        lista_conteudo_sobre_rexterno = []
        conteudo_sobre_rexterno = sobre_rexterno.find("div", id="content-core").find_all("p")
        for p in conteudo_sobre_rexterno:
            lista_conteudo_sobre_rexterno.append(p)
        # links
        lista_links_sobre_rexterno = []
        links_sobre_rexterno = sobre_rexterno.find("div", id="content-core").find("span", class_="discreet").find_all("a")
        for a in links_sobre_rexterno:
            lista_links_sobre_rexterno.append(a["href"])
    if lista_links_rexterno[1]: # in progress
        brasil_rexterno = acessar_pagina(lista_links_rexterno[1])
        # título
        titulo_brasil_rexterno = brasil_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_brasil_rexterno = brasil_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_brasil_rexterno = brasil_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        lista_conteudo_brasil_rexterno = []
        conteudo_brasil_rexterno = brasil_rexterno.find("div", id="content-core").find_all("p")
        for p in conteudo_brasil_rexterno:
            lista_conteudo_brasil_rexterno.append(p)
        # links
        lista_links_brasil_rexterno = []
        links_brasil_rexterno = brasil_rexterno.find("div", id="content-core").find_all("a")
        for a in links_brasil_rexterno:
            lista_links_brasil_rexterno.append(a["href"])
    if lista_links_rexterno[2]: # in progress
        conselho_rexterno = acessar_pagina(lista_links_rexterno[2])
        # título
        titulo_conselho_rexterno = conselho_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_conselho_rexterno = conselho_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_conselho_rexterno = conselho_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_conselho_rexterno = conselho_rexterno.find("div", id="content-core").text
        # links
        lista_links_conselho_rexterno = []
        links_conselho_rexterno = conselho_rexterno.find("div", id="content-core").find_all("a")
        for a in links_conselho_rexterno:
            lista_links_conselho_rexterno.append(a["href"])
        # imagens
        lista_imagens_conselho_rexterno = []
        imagens_conselho_rexterno = conselho_rexterno.find("div", id="content-core").find_all("img")
        for img in imagens_conselho_rexterno:
            lista_imagens_conselho_rexterno.append(img["src"])
    # link/card 3 não precisa ser coletado
    if lista_links_rexterno[4]: # in progress
        membros_rexterno = acessar_pagina(lista_links_rexterno[4])
        # título
        titulo_membros_rexterno = membros_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_membros_rexterno = membros_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_membros_rexterno = membros_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_membros_rexterno = membros_rexterno.find("div", id="content-core").text
        # links
        lista_links_membros_rexterno = []
        links_membros_rexterno = membros_rexterno.find("div", id="content-core").find_all("a")
        for a in links_membros_rexterno:
            lista_links_membros_rexterno.append(a["href"])
        # imagens
        lista_imagens_membros_rexterno = []
        imagens_membros_rexterno = membros_rexterno.find("div", id="content-core").find_all("img")
        for img in imagens_membros_rexterno:
            lista_imagens_membros_rexterno.append(img["src"])
    if lista_links_rexterno[5]: # check
        caminho_rexterno = acessar_pagina(lista_links_rexterno[5])
        # título
        titulo_caminho_rexterno = caminho_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_caminho_rexterno = caminho_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_caminho_rexterno = caminho_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_caminho_rexterno = caminho_rexterno.find("div", id="content-core").text
        # imagens
        lista_imagens_caminho_rexterno = []
        imagens_caminho_rexterno = caminho_rexterno.find("div", id="content-core").find_all("img")
        for img in imagens_caminho_rexterno:
            lista_imagens_caminho_rexterno.append(img["src"])
    if lista_links_rexterno[6]: # check
        try :
            comite_rexterno = acessar_pagina(lista_links_rexterno[6])
            # título
            titulo_comite_rexterno = comite_rexterno.find("h1", class_="documentFirstHeading").text
            # datas
            data_post_comite_rexterno = comite_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
            data_update_comite_rexterno = comite_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
            # conteúdo
            conteudo_comite_rexterno = comite_rexterno.find("div", id="content-core").text
            # imagens
            lista_imagens_comite_rexterno = []
            imagens_comite_rexterno = comite_rexterno.find("div", id="content-core").find_all("img")
            for img in imagens_comite_rexterno:
                lista_imagens_comite_rexterno.append(img["src"])
        except :
            pass 
    if lista_links_rexterno[7]: # check
        noticias_rexterno = acessar_pagina(lista_links_rexterno[7])
        # título
        titulo_noticias_rexterno = noticias_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_noticias_rexterno = noticias_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_noticias_rexterno = noticias_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        contador = 0 
        lista_url_noticias_rexterno = []
        while contador < 151:
            dominio = "https://www.gov.br/casacivil/pt-br/assuntos/ocde/noticias/noticias-ocde-1?b_start:int="
            dominio += str(contador) # montando a url / str, transformando numero em string
            contador += 10
            lista_url_noticias_rexterno.append(dominio)
        for url_noticias_rexterno in lista_url_noticias_rexterno:
            # conteudo 
            conteudo_noticias_rexterno = noticias_rexterno.find("div", id="content-core").find_all("article")
            for link_noticias in conteudo_noticias_rexterno:
                link_noticias_rexterno = acessar_pagina(link_noticias.h2.a["href"])
                # entrando na notícia
                titulo_noticias_rexterno = link_noticias_rexterno.find("h1").text
                data_noticias_rexterno = link_noticias_rexterno.find("span", class_="documentPublished").find("span", class_="value").text
                conteudo_noticias_rexterno = link_noticias_rexterno.find("div", id="content-core").text
                # tags notícias
                lista_tags_noticias_rexterno = []
                tags_noticias_rexterno = link_noticias_rexterno.find("div", id="category").find_all("span")
                for a_noticias in tags_noticias_rexterno:
                    lista_tags_noticias_rexterno.append(a_noticias.text)
                del(lista_tags_noticias_rexterno[0])
    if lista_links_rexterno[8]: # check
        estrutura_rexterno = acessar_pagina(lista_links_rexterno[8])
        # título
        titulo_estrutura_rexterno = estrutura_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_estrutura_rexterno = estrutura_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_estrutura_rexterno = estrutura_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_estrutura_rexterno = estrutura_rexterno.find("div", id="content-core").text
        # imagens
        lista_imagens_estrutura_rexterno = []
        imagens_estrutura_rexterno = estrutura_rexterno.find("div", id="content-core").find_all("img")
        for img in imagens_estrutura_rexterno:
            lista_imagens_estrutura_rexterno.append(img["src"])
        # links
        lista_links_estrutura_rexterno = []
        links_estrutura_rexterno = estrutura_rexterno.find("div", id="content-core").find("span", class_="discreet").find_all("a")
        for a in links_estrutura_rexterno:
            lista_links_estrutura_rexterno.append(a["href"])
    if lista_links_rexterno[9]: # check
        onde_rexterno = acessar_pagina(lista_links_rexterno[9])
        # título
        titulo_onde_rexterno = onde_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_onde_rexterno = onde_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_onde_rexterno = onde_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_onde_rexterno = onde_rexterno.find("div", id="content-core").text
        # imagens
        lista_imagens_onde_rexterno = []
        imagens_onde_rexterno = onde_rexterno.find("div", id="content-core").find_all("img")
        for img in imagens_onde_rexterno:
            lista_imagens_onde_rexterno.append(img["src"])
    if lista_links_rexterno[10]: # check
        try:
            secretaria_rexterno = acessar_pagina(lista_links_rexterno[10])
            # título
            titulo_secretaria_rexterno = secretaria_rexterno.find("h1", class_="documentFirstHeading").text
            # datas
            data_post_secretaria_rexterno = secretaria_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
            data_update_secretaria_rexterno = secretaria_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
            # conteúdo
            conteudo_secretaria_rexterno = secretaria_rexterno.find("div", id="content-core").text
        except:
            pass
    if lista_links_rexterno[11]: # check
        try: 
            reunioes_rexterno = acessar_pagina(lista_links_rexterno[11])
            # título
            titulo_reunioes_rexterno = reunioes_rexterno.find("h1").text
            # datas
            data_post_reunioes_rexterno = reunioes_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
            data_update_reunioes_rexterno = reunioes_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
            # conteúdo
            conteudo_reunioes_rexterno = reunioes_rexterno.find("div", id="content-core").text
            # links
            lista_links_reunioes_rexterno = []
            links_reunioes_rexterno = reunioes_rexterno.find("div", id="content-core").find_all("a")
            for a in links_reunioes_rexterno:
                lista_links_reunioes_rexterno.append(a["href"]) 
        except:
            pass   
    if lista_links_rexterno[12]: # check
        ### coletando item 12 da lista de links como INFOS LEGAIS pois há uma troca de conteúdo na página coletada
        infoslegais_rexterno = acessar_pagina(lista_links_rexterno[12])
        # título
        titulo_infoslegais_rexterno = infoslegais_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_infoslegais_rexterno = infoslegais_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_infoslegais_rexterno = infoslegais_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo
        conteudo_infoslegais_rexterno = infoslegais_rexterno.find("div", id="content-core").text
        # links
        lista_links_infoslegais_rexterno = []
        links_infoslegais_rexterno = infoslegais_rexterno.find("div", id="content-core").find_all("a")
        for a in links_infoslegais_rexterno:
            lista_links_infoslegais_rexterno.append(a["href"])
    if lista_links_rexterno[13]: # check
        documentos_rexterno = acessar_pagina(lista_links_rexterno[13])
        # título
        titulo_documentos_rexterno = documentos_rexterno.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_documentos_rexterno = documentos_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        # conteúdo
        conteudo_documentos_rexterno = documentos_rexterno.find("div", id="content-core").text
        # links
        lista_links_documentos_rexterno = []
        links_documentos_rexterno = documentos_rexterno.find("div", id="content-core").find_all("a")
        for a in links_documentos_rexterno:
            lista_links_documentos_rexterno.append(a["href"])
    if lista_links_rexterno[14]: # in progress
        try:
            legislacao_rexterno = acessar_pagina(lista_links_rexterno[14])
            # título
            titulo_legislacao_rexterno = legislacao_rexterno.find("h1", class_="documentFirstHeading").text
            # datas
            data_post_legislacao_rexterno = legislacao_rexterno.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
            data_update_legislacao_rexterno = legislacao_rexterno.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
            # conteúdo
            conteudo_legislacao_rexterno = legislacao_rexterno.find("div", id="content-core").text
            # links
            lista_links_legislacao_rexterno = []
            links_legislacao_rexterno = legislacao_rexterno.find("div", id="content-core").find_all("a")
            for a in links_legislacao_rexterno:
                lista_links_legislacao_rexterno.append(a["href"])
        except:
            pass        


def agenda_mais_brasil(): # página em manutenção
    url = links_cards(bs)[6]
    cc_pagina = acessar_pagina(url)


def governanca(): # in progress
    url = links_cards(bs)[7]
    cc_pagina = acessar_pagina(url)
    # pegando título da página 
    titulo_governanca = cc_pagina.find("h1", class_="documentFirstHeading").text
    # coletando subpáginas em lista
    cards_governanca = cc_pagina.find("div", class_="wrapper").find_all("div", class_="card")
    lista_cards_governanca = []
    for card in cards_governanca:
        lista_cards_governanca.append(card.a["href"])
    # não é necessário coletar o primeiro card
    if lista_cards_governanca[1]: # in progress
        ci_governanca = acessar_pagina(lista_cards_governanca[1])
        # título da página 
        titulo_ci_governanca = ci_governanca.find("h1", class_="documentFirstHeading").text
        # conteúdo da página - in progress (coletar subpáginas)
        lista_a_ci_governanca = []
        a_ci_governanca = ci_governanca.find("div", {"id":"parent-fieldname-text"}).find_all("td")
        for td_ci_governanca in a_ci_governanca:
            try:
                lista_a_ci_governanca.append(td_ci_governanca.a["href"])
            except:
                pass
        if lista_a_ci_governanca[0]: # check
            comite_ci_governanca = acessar_pagina(lista_a_ci_governanca[0])
            # título da página 
            titulo_comite_ci_governanca = comite_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_comite_ci_governanca = comite_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_comite_ci_governanca = comite_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_comite_ci_governanca = comite_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
        if lista_a_ci_governanca[1]: # check
            composicao_ci_governanca = acessar_pagina(lista_a_ci_governanca[1])
            # título da página 
            titulo_composicao_ci_governanca = composicao_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_composicao_ci_governanca = composicao_ci_governanca.find("div", {"id": "content-core"})
            # links
            lista_links_composicao_ci_governanca = []
            links_composicao_ci_governanca = composicao_ci_governanca.find("div", {"id": "content-core"}).find_all("p")
            for p_composicao_ci_governanca in links_composicao_ci_governanca:
                try:
                    lista_links_composicao_ci_governanca.append(p_composicao_ci_governanca.a["href"])
                except:
                    pass
            # datas da página
            data_post_composicao_ci_governanca = composicao_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_composicao_ci_governanca = composicao_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
        if lista_a_ci_governanca[2]: # check
            legislacao_ci_governanca = acessar_pagina(lista_a_ci_governanca[2])
            # título da página 
            titulo_legislacao_ci_governanca = legislacao_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_legislacao_ci_governanca = legislacao_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_legislacao_ci_governanca = legislacao_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_legislacao_ci_governanca = legislacao_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
            # links da página
            lista_links_legislacao_ci_governanca = []
            links_legislacao_ci_governanca = legislacao_ci_governanca.find("div", {"id": "content-core"}).find_all("li")
            for li_legislacao_ci_governanca in links_legislacao_ci_governanca: 
                try:
                    lista_links_legislacao_ci_governanca.append(li_legislacao_ci_governanca.a["href"])
                except:
                    pass
        if lista_a_ci_governanca[3]: # check
            agenda_ci_governanca = acessar_pagina(lista_a_ci_governanca[3])
            # título da página 
            titulo_agenda_ci_governanca = agenda_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_agenda_ci_governanca = agenda_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_agenda_ci_governanca = agenda_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_agenda_ci_governanca = agenda_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
        if lista_a_ci_governanca[4]: # check
            atas_ci_governanca = acessar_pagina(lista_a_ci_governanca[4])
            # título da página 
            titulo_atas_ci_governanca = atas_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_atas_ci_governanca = atas_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_atas_ci_governanca = atas_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_atas_ci_governanca = atas_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
            # links da página
            lista_links_atas_ci_governanca = []
            links_atas_ci_governanca = atas_ci_governanca.find("div", {"id": "content-core"}).find_all("li")
            for li_atas_ci_governanca in links_atas_ci_governanca: 
                try:
                    lista_links_atas_ci_governanca.append(li_atas_ci_governanca.a["href"])
                except:
                    pass
        if lista_a_ci_governanca[5]: # check
            recomendacoes_ci_governanca = acessar_pagina(lista_a_ci_governanca[5])
            # título da página 
            titulo_recomendacoes_ci_governanca = recomendacoes_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_recomendacoes_ci_governanca = recomendacoes_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_recomendacoes_ci_governanca = recomendacoes_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_recomendacoes_ci_governanca = recomendacoes_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
        if lista_a_ci_governanca[6]: # check
            guias_ci_governanca = acessar_pagina(lista_a_ci_governanca[6])
            # título da página 
            titulo_guias_ci_governanca = guias_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_guias_ci_governanca = guias_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_guias_ci_governanca = guias_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_guias_ci_governanca = guias_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
            # links da página
            lista_links_guias_ci_governanca = []
            links_guias_ci_governanca = guias_ci_governanca.find("div", {"id": "content-core"}).find_all("p")
            for p_guias_ci_governanca in links_guias_ci_governanca: 
                try:
                    lista_links_guias_ci_governanca.append(p_guias_ci_governanca.a["href"])
                except:
                    pass
        if lista_a_ci_governanca[7]: # check
            grupos_ci_governanca = acessar_pagina(lista_a_ci_governanca[7])  
            # título da página 
            titulo_grupos_ci_governanca = grupos_ci_governanca.find("h1", class_="documentFirstHeading").text
            # conteúdo da página
            conteudo_grupos_ci_governanca = grupos_ci_governanca.find("div", {"id": "content-core"}).text
            # datas da página
            data_post_grupos_ci_governanca = grupos_ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_grupos_ci_governanca = grupos_ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
            # links da página
            lista_links_grupos_ci_governanca = []
            links_grupos_ci_governanca = grupos_ci_governanca.find("div", {"id": "content-core"}).find_all("li")
            for li_grupos_ci_governanca in links_grupos_ci_governanca: 
                try:
                    lista_links_grupos_ci_governanca.append(li_grupos_ci_governanca.a["href"])
                except:
                    pass 
        # datas da página
        data_post_ci_governanca = ci_governanca.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_ci_governanca = ci_governanca.find("span", class_="documentModified").find("span", class_="value").text
    if lista_cards_governanca[2]: # in progress
        politica_governanca = acessar_pagina(lista_cards_governanca[2])
        # título da página 
        titulo_politica_governanca = politica_governanca.find("h1", class_="documentFirstHeading").text
        # conteúdo da página - in progress (coletar vídeos - a href)
        conteudo_politica_governanca = politica_governanca.find("div", id="content-core").text # texto
        # datas da página
        data_post_politica_governanca = politica_governanca.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_politica_governanca = politica_governanca.find("span", class_="documentModified").find("span", class_="value").text
    if lista_cards_governanca[3]: # check
        biblioteca_governanca = acessar_pagina(lista_cards_governanca[3])
        # título da página 
        titulo_biblioteca_governanca = biblioteca_governanca.find("h1", class_="documentFirstHeading").text
        # conteúdo da página 
        conteudo_biblioteca_governanca = biblioteca_governanca.find("div", id="content-core").text # texto
        # links da página
        lista_links_biblioteca = []
        links_biblioteca = biblioteca_governanca.find("div", id="content-core").find_all("a")
        for a in links_biblioteca:
            a_biblioteca = a["href"]
            lista_links_biblioteca.append(a_biblioteca)
        # datas da página
        data_post_biblioteca_governanca = biblioteca_governanca.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_biblioteca_governanca = biblioteca_governanca.find("span", class_="documentModified").find("span", class_="value").text
    if lista_cards_governanca[4]: # in progress
        regulacao_governanca = acessar_pagina(lista_cards_governanca[4])
        # há 3 blocos de conteúdo
        # conteúdo 1 
        conteudo1_regulacao_governanca = regulacao_governanca.find("div", id="cff0d1b2bca4404ea3551ec20813f6bf")
        # links 1
        # conteúdo 2
        conteudo2_regulacao_governanca = regulacao_governanca.find("div", id="c265f16cd95b48d5b694188908adf602")
        # links 2
        # conteúdo 3 
        conteudo3_regulacao_governanca = regulacao_governanca.find("div", id="e7c9a747e5294faba7ef776eb3686e94")
        # links 3
    if lista_cards_governanca[5]: # in progress
        avaliacao_governanca = acessar_pagina(lista_cards_governanca[5])
        # título da página 
        titulo_avaliacao_governanca = avaliacao_governanca.find("h1", class_="documentFirstHeading").text
        # datas da página
        data_post_avaliacao_governanca = avaliacao_governanca.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_avaliacao_governanca = avaliacao_governanca.find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo da página 
        conteudo_avaliacao_governanca = avaliacao_governanca.find("div", id="content-core")
        # links
        lista_links_avaliacao_governanca = []
        links_avaliacao_governanca = conteudo_avaliacao_governanca.find_all("a")
        for a in links_avaliacao_governanca:
            lista_links_avaliacao_governanca.append(a["href"])
    # cards 6(legislacao), 7(recomendacoes), 8(boas práticas), 9(guias e cartilhas) estão com a página vazia/em branco
    if lista_cards_governanca[-1]: # in progress
        planejamento_governanca = acessar_pagina(lista_cards_governanca[-1])
        # título da página 
        titulo_planejamento_governanca = planejamento_governanca.find("h1", class_="documentFirstHeading").text
        # datas da página
        data_post_planejamento_governanca = planejamento_governanca.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_planejamento_governanca = planejamento_governanca.find("span", class_="documentModified").find("span", class_="value").text
        # conteúdo da página 
        lista_tabs_planejamento_governanca = []
        tabs_planejamento_governanca = planejamento_governanca.find_all("div", class_="tab-content")
        for tab in tabs_planejamento_governanca:
            lista_tabs_planejamento_governanca.append(tab["data-url"])
        if lista_tabs_planejamento_governanca[0]:  # in progress
            mapa_governanca = acessar_pagina(lista_tabs_planejamento_governanca[0])
            # título da página 
            titulo_mapa_governanca = mapa_governanca.find("h1", class_="documentFirstHeading").text
            # datas da página
            data_post_mapa_governanca = mapa_governanca.find("span", class_="documentPublished").find("span", class_="value").text
            data_update_mapa_governanca = mapa_governanca.find("span", class_="documentModified").find("span", class_="value").text
            # conteúdo da página
            conteudo_mapa_governanca = mapa_governanca.find("div", id="content-core")
            # imagens da página
            lista_imagens_mapa_governanca = []
            imagens_mapa_governanca = mapa_governanca.find_all("img")
            for img in imagens_mapa_governanca:
                lista_imagens_mapa_governanca.append(img["src"])
            # links 
            lista_links_mapa_governanca = []
            links_mapa_governanca = conteudo_mapa_governanca.find_all("a")
            for a in links_mapa_governanca:
                lista_links_mapa_governanca.append(a["href"])


def conselho_superior_cinema(): # in progress
    url = links_cards(bs)[8]
    cc_pagina = acessar_pagina(url)
    # pegando título da página 
    titulo_cinema = cc_pagina.find("h1", class_="documentFirstHeading").text
    # datas da página
    data_post_cinema = cc_pagina.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_cinema = cc_pagina.find("span", class_="documentModified").find("span", class_="value").text
    # coletando subáginas em lista
    lista_tabs_cinema = []
    tabs_cinema = cc_pagina.find_all("div", class_="tab-content")
    for tab in tabs_cinema:
        lista_tabs_cinema.append(tab["data-url"])
    if lista_tabs_cinema[0]: # check
        informes_cinema = acessar_pagina(lista_tabs_cinema[0])
        # título
        titulo_informes_cinema = informes_cinema.find("h1", class_="documentFirstHeading").text
        # conteúdo
        conteudo_informes_cinema = informes_cinema.find("div", id="content-core")
        # datas
        data_post_informes_cinema = informes_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_informes_cinema = informes_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    if lista_tabs_cinema[1]: # in progress - coletar links
        competencias_cinema = acessar_pagina(lista_tabs_cinema[1])
        # título
        titulo_competencias_cinema = competencias_cinema.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_competencias_cinema = competencias_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_competencias_cinema = competencias_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text   
        # conteúdo e links
        lista_links_competencias_cinema = []
        conteudo_competencias_cinema = competencias_cinema.find("div", id="content-core")
        links_competencias_cinema = conteudo_competencias_cinema.find_all("a")
        for a in links_competencias_cinema:
            lista_links_competencias_cinema.append(a["href"])
        """
        if lista_links_competencias_cinema[0]: # PERGUNTAR PARA RAFAEL: como percorrer dois(todos) links juntos
            link0_competencias = acessar_pagina(lista_links_competencias_cinema[0])
            # coletar conteúdo
        """
    if lista_tabs_cinema[2]: # in progress - coletar links de decretos (possui PDF)
        composicao_cinema = acessar_pagina(lista_tabs_cinema[2])
        # título
        titulo_composicao_cinema = composicao_cinema.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_composicao_cinema = composicao_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_composicao_cinema = composicao_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text   
        # conteúdo e links
        lista_links_composicao_cinema = []
        conteudo_composicao_cinema = composicao_cinema.find("div", id="content-core")
        links_composicao_cinema = conteudo_composicao_cinema.find_all("a")
        for a in links_composicao_cinema:
            lista_links_composicao_cinema.append(a["href"])
        """ 
        if lista_links_composicao_cinema[0]: 
            link0_composicao = acessar_pagina(lista_links_composicao_cinema[0])
            conteudo_link1_composicao = link0_composicao.find()
        if lista_links_composicao_cinema[1]: 
            link1_composicao = acessar_pagina(lista_links_composicao_cinema[1])
            conteudo_link1_composicao = link1_composicao.find()
        if lista_links_composicao_cinema[2]: 
            link2_composicao = acessar_pagina(lista_links_composicao_cinema[2])
            conteudo_link2_composicao = link1_composicao.find()
        if lista_links_composicao_cinema[3]: 
            link3_composicao = acessar_pagina(lista_links_composicao_cinema[3])
            conteudo_link3_composicao = link3_composicao.find()
        if lista_links_composicao_cinema[4]: 
            link4_composicao = acessar_pagina(lista_links_composicao_cinema[4])
            conteudo_link4_composicao = link4_composicao.find()
        """
    if lista_tabs_cinema[3]: # in progress
        regimento_cinema = acessar_pagina(lista_tabs_cinema[3])
        # título
        titulo_regimento_cinema = regimento_cinema.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_regimento_cinema = regimento_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_regimento_cinema = regimento_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text   
        # conteúdo e links
        lista_links_regimento_cinema = []
        conteudo_regimento_cinema = regimento_cinema.find("div", id="content-core")
        links_regimento_cinema = conteudo_regimento_cinema.find_all("a")
        for a in links_regimento_cinema:
            lista_links_regimento_cinema.append(a["href"])
        """
        if lista_links_regimento_cinema[0]: 
            link0_regimento = acessar_pagina(lista_links_regimento_cinema[0])
            # PDF
        """
    if lista_tabs_cinema[4]: # in progress
        reunioes_cinema = acessar_pagina(lista_tabs_cinema[4])
        # título
        titulo_reunioes_cinema = reunioes_cinema.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_reunioes_cinema = reunioes_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_reunioes_cinema = reunioes_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text   
        # conteúdo e links
        lista_links_reunioes_cinema = []
        conteudo_reunioes_cinema = reunioes_cinema.find("div", id="content-core")
        links_reunioes_cinema = conteudo_reunioes_cinema.find_all("a")
        for a in links_reunioes_cinema:
            lista_links_reunioes_cinema.append(a["href"])
        """
        if lista_links_reunioes_cinema[0]: 
            link0_regimento = acessar_pagina(lista_links_reunioes_cinema[0])
        if lista_links_reunioes_cinema[1]: 
            link1_regimento = acessar_pagina(lista_links_reunioes_cinema[1])
        if lista_links_reunioes_cinema[2]: 
            link2_regimento = acessar_pagina(lista_links_reunioes_cinema[2])
        if lista_links_reunioes_cinema[3]: 
            link3_regimento = acessar_pagina(lista_links_reunioes_cinema[3])
        if lista_links_reunioes_cinema[4]: 
            link4_regimento = acessar_pagina(lista_links_reunioes_cinema[4])
        if lista_links_reunioes_cinema[5]: 
            link5_regimento = acessar_pagina(lista_links_reunioes_cinema[5])
        if lista_links_reunioes_cinema[6]: 
            link6_regimento = acessar_pagina(lista_links_reunioes_cinema[6])
        if lista_links_reunioes_cinema[7]: 
            link7_regimento = acessar_pagina(lista_links_reunioes_cinema[7])
        if lista_links_reunioes_cinema[8]: 
            link8_regimento = acessar_pagina(lista_links_reunioes_cinema[8])
        if lista_links_reunioes_cinema[9]: 
            link9_regimento = acessar_pagina(lista_links_reunioes_cinema[9])
        if lista_links_reunioes_cinema[10]: 
            link10_regimento = acessar_pagina(lista_links_reunioes_cinema[10])
        if lista_links_reunioes_cinema[11]: 
            link11_regimento = acessar_pagina(lista_links_reunioes_cinema[11])
        if lista_links_reunioes_cinema[12]: 
            link12_regimento = acessar_pagina(lista_links_reunioes_cinema[12])
        if lista_links_reunioes_cinema[13]: 
            link13_regimento = acessar_pagina(lista_links_reunioes_cinema[13])
        if lista_links_reunioes_cinema[14]: 
            link14_regimento = acessar_pagina(lista_links_reunioes_cinema[14])
        if lista_links_reunioes_cinema[15]: 
            link15_regimento = acessar_pagina(lista_links_reunioes_cinema[15])
        if lista_links_reunioes_cinema[16]: 
            link16_regimento = acessar_pagina(lista_links_reunioes_cinema[16])
        if lista_links_reunioes_cinema[17]: 
            link17_regimento = acessar_pagina(lista_links_reunioes_cinema[17])
        if lista_links_reunioes_cinema[18]: 
            link18_regimento = acessar_pagina(lista_links_reunioes_cinema[18])
        if lista_links_reunioes_cinema[19]: 
            link19_regimento = acessar_pagina(lista_links_reunioes_cinema[19])
        if lista_links_reunioes_cinema[20]: 
            link20_regimento = acessar_pagina(lista_links_reunioes_cinema[20])
        if lista_links_reunioes_cinema[21]: 
            link21_regimento = acessar_pagina(lista_links_reunioes_cinema[21])
        if lista_links_reunioes_cinema[22]: 
            link22_regimento = acessar_pagina(lista_links_reunioes_cinema[22])
        if lista_links_reunioes_cinema[23]: 
            link23_regimento = acessar_pagina(lista_links_reunioes_cinema[23])
        if lista_links_reunioes_cinema[24]: 
            link24_regimento = acessar_pagina(lista_links_reunioes_cinema[24])
        if lista_links_reunioes_cinema[25]: 
            link25_regimento = acessar_pagina(lista_links_reunioes_cinema[25])
        if lista_links_reunioes_cinema[26]: 
            link26_regimento = acessar_pagina(lista_links_reunioes_cinema[26])
        if lista_links_reunioes_cinema[27]: 
            link27_regimento = acessar_pagina(lista_links_reunioes_cinema[27])
        if lista_links_reunioes_cinema[28]: 
            link28_regimento = acessar_pagina(lista_links_reunioes_cinema[28])
        if lista_links_reunioes_cinema[29]: 
            link29_regimento = acessar_pagina(lista_links_reunioes_cinema[29])
        if lista_links_reunioes_cinema[30]: 
            link30_regimento = acessar_pagina(lista_links_reunioes_cinema[30])
        if lista_links_reunioes_cinema[31]: 
            link31_regimento = acessar_pagina(lista_links_reunioes_cinema[31])
        if lista_links_reunioes_cinema[32]: 
            link32_regimento = acessar_pagina(lista_links_reunioes_cinema[32])
        if lista_links_reunioes_cinema[33]: 
            link33_regimento = acessar_pagina(lista_links_reunioes_cinema[33])
        """
    if lista_tabs_cinema[5]: # in progress
        legislacao_cinema = acessar_pagina(lista_tabs_cinema[5])
        # título
        titulo_legislacao_cinema = legislacao_cinema.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_legislacao_cinema = legislacao_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_legislacao_cinema = legislacao_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text   
        # conteúdo e links
        lista_links_legislacao_cinema = []
        conteudo_legislacao_cinema = legislacao_cinema.find("div", id="content-core")
        links_legislacao_cinema = conteudo_legislacao_cinema.find_all("a")
        for a in links_legislacao_cinema:
            lista_links_legislacao_cinema.append(a["href"])
        """
        if lista_links_legislacao_cinema[0]: 
            link0_legislacao = acessar_pagina(lista_links_legislacao_cinema[0])
        if lista_linkslegislacao_cinema[1]: 
            link1_legislacao = acessar_pagina(lista_links_legislacao_cinema[1])
        if lista_links_legislacao_cinema[2]: 
            link2_legislacao = acessar_pagina(lista_links_legislacao_cinema[2])
        if lista_links_legislacao_cinema[3]: 
            link3_legislacao = acessar_pagina(lista_links_legislacao_cinema[3])
        if lista_links_legislacao_cinema[4]: 
            link4_legislacao = acessar_pagina(lista_links_legislacao_cinema[4])
        if lista_links_legislacao_cinema[5]: 
            link5_legislacao = acessar_pagina(lista_links_legislacao_cinema[5])
        if lista_links_legislacao_cinema[6]: 
            link6_legislacao = acessar_pagina(lista_links_legislacao_cinema[6])
        if lista_links_legislacao_cinema[7]: 
            link7_legislacao = acessar_pagina(lista_links_legislacao_cinema[7])
        if lista_links_legislacao_cinema[8]: 
            link8_legislacao = acessar_pagina(lista_links_legislacao_cinema[8])
        if lista_links_legislacao_cinema[9]: 
            link9_legislacao = acessar_pagina(lista_links_legislacao_cinema[9])
        """
    if lista_tabs_cinema[6]: # in progress
        contato_cinema = acessar_pagina(lista_tabs_cinema[6])
        # título
        titulo_contato_cinema = contato_cinema.find("h1", class_="documentFirstHeading").text
        # datas
        data_post_contato_cinema = contato_cinema.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_contato_cinema = contato_cinema.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text   
        # conteúdo e links
        lista_links_contato_cinema = []
        conteudo_contato_cinema = contato_cinema.find("div", id="content-core")
        links_contato_cinema = conteudo_contato_cinema.find_all("a")
        for a in links_contato_cinema:
            lista_links_contato_cinema.append(a["href"])


def ci_mudanca_clima(): # check
    url = links_cards(bs)[9]
    cc_pagina = acessar_pagina(url)
    # pegando título da página 
    titulo_clima = cc_pagina.find("h1", class_="documentFirstHeading").text
    # acessando subpáginas
    cards_clima = cc_pagina.find("div", class_="wrapper").find_all("div", class_="card")
    lista_cards_clima = []
    for card in cards_clima:
        lista_cards_clima.append(card.a["href"])
    if lista_cards_clima[0]: # check
        sobre_cim = acessar_pagina(lista_cards_clima[0])
        lista_conteudo_sobre = sobre_cim.find("div", id="content-core") # conteúdo
        data_post_sobre = sobre_cim.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
    if lista_cards_clima[1]: # check
        atas_cim = acessar_pagina(lista_cards_clima[1])
        lista_links_atas = []
        lista_conteudo_atas = atas_cim.find("div", id="content-core").find_all("p")
        for tag_p in lista_conteudo_atas:
            lista_tag_a = tag_p.find_all("a")
            for a in lista_tag_a:
                tag_a = a["href"]
                lista_links_atas.append(tag_a)
        # datas
        data_post_atas = atas_cim.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_atas = atas_cim.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    if lista_cards_clima[3]: # check 
        regime_cim = acessar_pagina(lista_cards_clima[3])
        lista_links_regime = []
        lista_conteudo_regime = regime_cim.find("div", id="content-core").find_all("p")
        for tag_p in lista_conteudo_regime:
            lista_tag_a = tag_p.find_all("a")
            for a in lista_tag_a:
                tag_a = a["href"]
                lista_links_regime.append(tag_a)
        # datas
        data_post_regime = regime_cim.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_regime = regime_cim.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    if lista_cards_clima[4]: # check
        arquivos_cim = acessar_pagina(lista_cards_clima[-1])
        # conteúdo da página 
        lista_conteudo_arquivos = [] 
        lista_links_arquivos = []
        conteudo_arquivos = arquivos_cim.find("div", id="content-core").find_all("article")
        for tag_article in conteudo_arquivos: 
            lista_tag_article_arquivos = tag_article.find("span", class_="documentByLine")
            lista_conteudo_arquivos.append(lista_tag_article_arquivos)
            # links da página
            links_arquivos = tag_article.find("span", class_="summary").find_all("a")
            for a in links_arquivos:
                    tag_a = a["href"]
                    lista_links_arquivos.append(tag_a)
        # datas 
        data_post_arquivos_cim = arquivos_cim.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_arquivos_cim = arquivos_cim.find("span", class_="documentModified").find("span", class_="value").text


def ci_planejamento_infraestrutura(): # check
    url = links_cards(bs)[10]
    cc_pagina = acessar_pagina(url)
    # pegando título da página 
    titulo_planejamento = cc_pagina.find("h1", class_="documentFirstHeading").text
    # coletando conteudo
    lista_links_planejamento = []
    lista_conteudo_planejamento = cc_pagina.find("div", id="content-core").find_all("p")
    for tag_p in lista_conteudo_planejamento: 
        lista_tag_a = tag_p.find_all("a")
        for a in lista_tag_a:
            tag_a = a["href"]
            lista_links_planejamento.append(tag_a) 
    lista_data_planejamento = cc_pagina.find("div", class_="documentByLine")
    data_post_planejamento = lista_data_planejamento.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_planejamento = lista_data_planejamento.find("span", class_="documentModified").find("span", class_="value").text


def cf_assistencia_emergencial(): # check
    url = links_cards(bs)[11]
    cc_pagina = acessar_pagina(url)
    # pegando título da página 
    titulo_assistencia = cc_pagina.find("h1", class_="documentFirstHeading").text
    # pegando todo conteúdo da página
    lista_conteudo_assistencia = cc_pagina.find("div", id="content-core").find("p", class_="Paragrafo_Numerado_Nivel1").text
    # pegando os links da página
    lista_links_assistencia = []
    lista_tag_ul_assistencia = cc_pagina.find("div", id="content-core").find("ul").find_all("a", class_="internal-link")
    for a in lista_tag_ul_assistencia:
        tag_a = a["href"]
        lista_links_assistencia.append(tag_a) 
    # pegando datas da página
    data_post_assistencia = cc_pagina.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_assistencia = cc_pagina.find("span", class_="documentModified").find("span", class_="value").text


def orgaos_vinculados(): # check
    url = links_cards(bs)[12]
    cc_pagina = acessar_pagina(url)
    # pegando título da página 
    titulo_orgaos = cc_pagina.find("h1", class_="documentFirstHeading").text
    # pegando todo conteúdo da página 
    lista_conteudo_orgaos = cc_pagina.find("div", class_="entries").find("article", class_="entry")
    # pegando os links da página
    lista_links_orgaos = []
    lista_tag_ul_orgaos = lista_conteudo_orgaos.find("span", class_="summary").find_all("a")
    for a in lista_tag_ul_orgaos:
            tag_a = a["href"]
            lista_links_orgaos.append(tag_a)
    # pegando datas da página 
    data_post_orgaos = cc_pagina.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_orgaos = cc_pagina.find("span", class_="documentModified").find("span", class_="value").text


def conselho_solidariedade(): # in progress - pegar títulos
    url = links_cards(bs)[13]
    cc_pagina = acessar_pagina(url) # passando o link para pagina url, parciando as noticias
    # pegando título da página 
    titulo_solidariedade = cc_pagina.find("h1", class_="documentFirstHeading").text
    # pegando datas da página 
    data_post_solidariedade = cc_pagina.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_solidariedade = cc_pagina.find("span", class_="documentModified").find("span", class_="value").text
    # acessando subpáginas por lista
    lista_links_solidariedade = []
    lista_td_solidariedade = cc_pagina.find("div", id="content-core").find_all("td")
    for td_solidariedade in lista_td_solidariedade:
        lista_a_solidariedade = td_solidariedade.find_all("a")
        for a_solidariedade in lista_a_solidariedade:
            tag_a_solidariedade = a_solidariedade["href"]
            lista_links_solidariedade.append(tag_a_solidariedade)
    # acessando subpágina conselho
    if lista_links_solidariedade[0]: # in progress
        td_conselho = acessar_pagina(lista_links_solidariedade[0])
        # pegando conteúdo
        conteudo_conselho = td_conselho.find("div", id="content-core")
        # colocando links e tags da página em lista 
        lista_links_conselho = []
        lista_a_conselho = td_conselho.find("div", class_="visualClear").find_all("a")
        for a in lista_a_conselho:
            links_conselho = a["href"]
            lista_links_conselho.append(links_conselho)
        lista_tag_conselho = td_conselho.find("div", id="category").find_all("a")
        for a in lista_tag_conselho:
            tag_conselho = a["href"]
            lista_links_conselho.append(tag_conselho)
       
        # # acessando links da lista
        # if lista_links_conselho[0]:
        #     a_conselho = acessar_pagina(lista_links_conselho[0])
        #     # pegando conteudo dos links
        #     conteudo_a_conselho = []
        #     conteudo_decreto = a_conselho.find("font", face="Arial").find_all("p")
        #     for p in conteudo_decreto:
        #         conteudo_a_conselho.append(p)
        #     print(conteudo_a_conselho)
        # if lista_links_conselho[1]:
        #     a_conselho = acessar_pagina(lista_links_conselho[1])

        # pegando datas da página 
        data_post_conselho = td_conselho.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_conselho = td_conselho.find("span", class_="documentModified").find("span", class_="value").text
    # acessando subpágina composição 
    if lista_links_solidariedade[1]: # check
        td_composicao = acessar_pagina(lista_links_solidariedade[1])
        # pegando conteúdo 
        lista_conteudo_composicao = td_composicao.find("div", id="content-core").text
        # pegando datas da página 
        data_post_composicao = td_composicao.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_composicao = td_composicao.find("span", class_="documentModified").find("span", class_="value").text


def main():
    global bs
    url = "https://www.gov.br/casacivil/pt-br/assuntos"
    bs = acessar_pagina(url)  # chamando a funcao responsavel por chamar a pag
    cards = links_cards(bs)
    # cc_cf_assistencia_emergencial = cf_assistencia_emergencial()
    # cc_orgaos_vinculados = orgaos_vinculados()
    # cc_conselho_solidariedade = conselho_solidariedade()
    # cc_ci_planejamento_infraestrutura = ci_planejamento_infraestrutura()
    # cc_ci_mudanca_clima = ci_mudanca_clima()
    # cc_conselho_superior_cinema = conselho_superior_cinema()
    # cc_governanca = governanca()
    # cc_relacionamento_externo = relacionamento_externo()
    # cc_agenda_mais_brasil = agenda_mais_brasil()
    # cc_noticias = noticias()
    # cc_notas_oficiais = notas_oficiais()
    cc_comunicados_interministeriais = comunicados_interministeriais()
    # cc_boletins_cc = boletins_cc()
    # cc_periodicos_mensais = periodicos_mensais()


if __name__ == "__main__":
    main()
