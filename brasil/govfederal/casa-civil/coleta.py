from urllib.request import urlopen
# ativa a biblioteca nativa do python
from bs4 import BeautifulSoup
# ativa a biblioteca de terceiros que percorre a página, extraindo infos que queremos


def pagina(url):
    html = urlopen(url)  # irá retornar a página da função links_cards
    # chama a página
    bs = BeautifulSoup(html, "html.parser")
    # percorre os elementos que queremos
    return bs


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


def conselho_superior_cinema(): # em andamento
    url = links_cards(bs)[8]
    cc_pagina = pagina(url)
    # conteúdo da página
    lista_conteudo_cinema = cc_pagina.find("div", id="content-core")
    # datas da página
    lista_data_cinema = cc_pagina.find("div", class_="documentByLine")
    data_post_cinema = lista_data_cinema.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_cinema = lista_data_cinema.find("span", class_="documentModified").find("span", class_="value").text


def ci_mudanca_clima(): # em andamento
    url = links_cards(bs)[9]
    cc_pagina = pagina(url)
    cards_clima = cc_pagina.find("div", class_="wrapper").find_all("div", class_="card")
    lista_cards_clima = []
    for card in cards_clima:
        lista_cards_clima.append(card.a["href"])
    return lista_cards_clima


def ci_planejamento_infraestrutura(): # check
    url = links_cards(bs)[10]
    cc_pagina = pagina(url)
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
    cc_pagina = pagina(url)
    # pegando toodo conteúdo da página
    lista_conteudo_assistencia = cc_pagina.find("div", id="content-core").find("p", class_="Paragrafo_Numerado_Nivel1").text
<<<<<<< HEAD
    lista_links_assistencia = []
    lista_tag_ul = cc_pagina.find("div", id="content-core").find("ul").find_all("a")
    for a in lista_tag_ul:
        tag_a = a["href"]
        lista_links_assistencia.append(tag_a)
        print(paginas_links_assistencia)
=======
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

>>>>>>> f84dc05fd68307f04994a3cf98152e3d5a737d2d

def orgaos_vinculados(): # check
    url = links_cards(bs)[12]
    cc_pagina = pagina(url)
    # pegando todo conteúdo da página 
<<<<<<< HEAD
    lista_conteudo_orgaos = cc_pagina.find("div", class_="entries").find("article", class_="entry") 
=======
    lista_conteudo_orgaos = cc_pagina.find("div", class_="entries").find("article", class_="entry")
    # pegando os links da página
    lista_links_orgaos = []
    lista_tag_ul_orgaos = lista_conteudo_orgaos.find("span", class_="summary").find_all("a")
    for a in lista_tag_ul_orgaos:
            tag_a = a["href"]
            lista_links_orgaos.append(tag_a)
>>>>>>> f84dc05fd68307f04994a3cf98152e3d5a737d2d
    # pegando datas da página 
    lista_data_orgaos = cc_pagina.find("div", class_="documentByLine")
    data_post_orgaos = lista_data_orgaos.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_orgaos = lista_data_orgaos.find("span", class_="documentModified").find("span", class_="value").text


def conselho_solidariedade(): # em andamento
    # pega o link do solidariedade, indicado pelo numero 13
    url = links_cards(bs)[13]
    # passando o link para pagina url, parciando as noticias
    cc_pagina = pagina(url)
    lista_links_solidariedade = [] # cria uma lista vazia
    # chamando os links das subpáginas
    lista_tag_td = cc_pagina.find("tr").find_all("td") # a lista td percorrida foi atribuída a tag
    for tag_td in lista_tag_td:
        lista_tag_a = tag_td.find_all("a") 
        for a in lista_tag_a:
            tag_a = a["href"]
            lista_links_solidariedade.append(tag_a) # coloca dentro da lista vazia
    for link in lista_links_solidariedade:
        paginas_links = pagina(link) # chamou a variável link criada 
        pags_solidariedade = paginas_links
    # pegando datas da página 
    lista_data_solidariedade = cc_pagina.find("div", class_="documentByLine")
    data_post_solidariedade = lista_data_solidariedade.find("span", class_="documentPublished").find("span", class_="value").text
    data_update_solidariedade = lista_data_solidariedade.find("span", class_="documentModified").find("span", class_="value").text
    # clicando nas subpáginas

def main():
    global bs
    url = "https://www.gov.br/casacivil/pt-br/assuntos"
    bs = pagina(url)  # chamando a funcao responsavel por chamar a pag
    cards = links_cards(bs)
    cc_cf_assistencia_emergencial = cf_assistencia_emergencial()
    cc_orgaos_vinculados = orgaos_vinculados()
    cc_conselho_solidariedade = conselho_solidariedade()
    cc_ci_planejamento_infraestrutura = ci_planejamento_infraestrutura()
    cc_ci_mudanca_clima = ci_mudanca_clima()
    cc_conselho_superior_cinema= conselho_superior_cinema()

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
