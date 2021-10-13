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


def notas_oficiais(bs):
    notas_oficiais = links_cards(bs)[1]


def comunicados_interministeriais(bs):
    comunicados_interministeriais = links_cards(bs)[2]


def boletins_cc(bs):
    boletins_cc = links_cards(bs)[3]


def periodicos_mensais(bs):
    periodicos_mensais = links_cards(bs)[4]


def relacionamento_externo(bs):
    relacionamento_externo = links_cards(bs)[5]


def agenda_mais_brasil(bs):
    agenda_mais_brasil = links_cards(bs)[6]


def governanca(bs):
    governanca = links_cards(bs)[7]


def conselho_superior_cinema(): # in progress
    url = links_cards(bs)[8]
    cc_pagina = acessar_pagina(url)
    # conteúdo da página
    lista_conteudo_cinema = cc_pagina.find("div", id="content-core")
    # datas da página
    lista_data_cinema = cc_pagina.find("div", class_="documentByLine")
    data_post_cinema = lista_data_cinema.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_cinema = lista_data_cinema.find("span", class_="documentModified").find("span", class_="value").text


def ci_mudanca_clima(): # check
    url = links_cards(bs)[9]
    cc_pagina = acessar_pagina(url)
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
        lista_data_atas = atas_cim.find("div", class_="documentByLine")
        data_post_atas = atas_cim.find("div", class_="documentByLine").find("span", class_="documentPublished").find("span", class_="value").text
        data_update_atas = atas_cim.find("div", class_="documentByLine").find("span", class_="documentModified").find("span", class_="value").text
    if lista_cards_clima[3]: # check / conferir o retorno de várias vezes os mesmos links
        regime_cim = acessar_pagina(lista_cards_clima[3])
        lista_links_regime = []
        lista_conteudo_regime = regime_cim.find("div", id="content-core").find_all("p")
        for tag_p in lista_conteudo_regime:
            lista_tag_a = tag_p.find_all("a")
            for a in lista_tag_a:
                tag_a = a["href"]
                lista_links_regime.append(tag_a)
        # datas
        lista_data_regime = regime_cim.find("div", class_="documentByLine")
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
        lista_data_arquivos = arquivos_cim.find("div", class_="documentByLine")
        data_post_arquivos = lista_data_arquivos.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_arquivos = lista_data_arquivos.find("span", class_="documentModified").find("span", class_="value").text


def ci_planejamento_infraestrutura(): # check
    url = links_cards(bs)[10]
    cc_pagina = acessar_pagina(url)
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
    # pegando toodo conteúdo da página
    lista_conteudo_assistencia = cc_pagina.find("div", id="content-core").find("p", class_="Paragrafo_Numerado_Nivel1").text
    # pegando os links da página
    lista_links_assistencia = []
    lista_tag_ul_assistencia = cc_pagina.find("div", id="content-core").find("ul").find_all("a", class_="internal-link")
    for a in lista_tag_ul_assistencia:
        tag_a = a["href"]
        lista_links_assistencia.append(tag_a) 
    # pegando datas da página
    lista_data_assistencia = cc_pagina.find("div", class_="documentByLine")
    data_post_assistencia = lista_data_assistencia.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_assistencia = lista_data_assistencia.find("span", class_="documentModified").find("span", class_="value").text


def orgaos_vinculados(): # check
    url = links_cards(bs)[12]
    cc_pagina = acessar_pagina(url)
    # pegando todo conteúdo da página 
    lista_conteudo_orgaos = cc_pagina.find("div", class_="entries").find("article", class_="entry")
    # pegando os links da página
    lista_links_orgaos = []
    lista_tag_ul_orgaos = lista_conteudo_orgaos.find("span", class_="summary").find_all("a")
    for a in lista_tag_ul_orgaos:
            tag_a = a["href"]
            lista_links_orgaos.append(tag_a)
    # pegando datas da página 
    lista_data_orgaos = cc_pagina.find("div", class_="documentByLine")
    data_post_orgaos = lista_data_orgaos.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_orgaos = lista_data_orgaos.find("span", class_="documentModified").find("span", class_="value").text


def conselho_solidariedade(): # in progress - pegar títulos
    url = links_cards(bs)[13]
    cc_pagina = acessar_pagina(url) # passando o link para pagina url, parciando as noticias
    # pegando datas da página 
    lista_data_solidariedade = cc_pagina.find("div", class_="documentByLine")
    data_post_solidariedade = lista_data_solidariedade.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_solidariedade = lista_data_solidariedade.find("span", class_="documentModified").find("span", class_="value").text
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
       
        """
        # acessando links da lista
        if lista_links_conselho[0]:
            a_conselho = acessar_pagina(lista_links_conselho[0])
            # pegando conteudo dos links
            conteudo_a_conselho = []
            conteudo_decreto = a_conselho.find("font", face="Arial").find_all("p")
            for p in conteudo_decreto:
                conteudo_a_conselho.append(p)
            print(conteudo_a_conselho)
        if lista_links_conselho[1]:
            a_conselho = acessar_pagina(lista_links_conselho[1])
        """

        # pegando datas da página 
        lista_data_conselho = td_conselho.find("div", class_="documentByLine")
        data_post_conselho = lista_data_conselho.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_conselho = lista_data_conselho.find("span", class_="documentModified").find("span", class_="value").text
    # acessando subpágina composição 
    if lista_links_solidariedade[1]: # check
        td_composicao = acessar_pagina(lista_links_solidariedade[1])
        # pegando conteúdo 
        lista_conteudo_composicao = td_composicao.find("div", id="content-core").text
        # pegando datas da página 
        lista_data_composicao = td_composicao.find("div", class_="documentByLine")
        data_post_composicao = lista_data_composicao.find("span", class_="documentPublished").find("span", class_="value").text
        data_update_composicao = lista_data_composicao.find("span", class_="documentModified").find("span", class_="value").text


def main():
    global bs
    url = "https://www.gov.br/casacivil/pt-br/assuntos"
    bs = acessar_pagina(url)  # chamando a funcao responsavel por chamar a pag
    cards = links_cards(bs)
    cc_cf_assistencia_emergencial = cf_assistencia_emergencial()
    cc_orgaos_vinculados = orgaos_vinculados()
    cc_conselho_solidariedade = conselho_solidariedade()
    cc_ci_planejamento_infraestrutura = ci_planejamento_infraestrutura()
    cc_ci_mudanca_clima = ci_mudanca_clima()
    cc_conselho_superior_cinema = conselho_superior_cinema()

    """
    cc_noticias = noticias(bs)
    cc_notas_oficiais = notas_oficiais(bs)
    cc_comunicados_interministeriais = comunicados_interministeriais(bs)
    cc_boletins_cc = boletins_cc(bs)
    cc_periodicos_mensais= periodicos_mensais(bs)
    cc_relacionamento_externo= relacionamento_externo(bs)
    cc_agenda_mais_brasil= agenda_mais_brasil(bs)
    cc_governanca= governanca(bs)
    """  

if __name__ == "__main__":
    main()
