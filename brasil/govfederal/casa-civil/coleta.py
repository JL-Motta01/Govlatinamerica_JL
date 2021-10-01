from urllib.request import urlopen
# ativa a biblioteca nativa do python 
from bs4 import BeautifulSoup
# ativa a biblioteca de terceiros que percorre a página, extraindo infos que queremos 

def pagina(url):
    html = urlopen(url) # irá retornar a página da função links_cards
    ## chama a página
    global bs
    bs = BeautifulSoup(html, "html.parser")
    ## percorre os elementos que queremos
    return bs

def links_cards(bs):
    cards = bs.find("div", class_="wrapper").find_all("div", class_="card") # passa em lista
    lista_cards = [] # cria uma lista vazia
    for card in cards :
        lista_cards.append(card.a["href"]) # coloca dentro da lista vazia
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

def conselho_superior_cinema(bs):
    conselho_superior_cinema = links_cards(bs)[8]

def ci_mudanca_clima(bs):
    ci_mudanca_clima = links_cards(bs)[9]

def ci_planejamento_infraestrutura(bs):
    ci_planejamento_infraestrutura = links_cards(bs)[10]

def cf_assistencia_emergencial(bs):
    cf_assistencia_emergencial = links_cards(bs)[11]

def orgaos_vinculados(bs):
    orgaos_vinculados = links_cards(bs)[12]

def conselho_solidariedade():
    url = links_cards(bs)[13] # pega o link do solidariedade, indicado pelo numero 13
    cc_pagina = pagina(url) # passando o link para pagina url, parciando as noticias
    tag_tr = cc_pagina.find("tr").find_all("td").a
    for tag_td in tag_tr : 
        print(tag_td)

def main():
    url = "https://www.gov.br/casacivil/pt-br/assuntos"
    bs = pagina(url) # chamando a funcao responsavel por chamar a pag
    cards = links_cards(bs) 
    ## bs = pagina(url)
    """
    cc_noticias = noticias(bs)
    cc_comunicados_interministeriais = comunicados_interministeriais(bs)
    cc_boletins_cc = boletins_cc(bs)
    cc_periodicos_mensais= periodicos_mensais(bs)
    cc_relacionamento_externo= relacionamento_externo(bs)
    cc_agenda_mais_brasil= agenda_mais_brasil(bs)
    cc_governanca= governanca(bs)
    cc_conselho_superior_cinema= conselho_superior_cinema(bs)
    cc_ci_mudanca_clima= ci_mudanca_clima(bs)
    cc_ci_planejamento_infraestrutura= ci_planejamento_infraestrutura(bs)
    cc_cf_assistencia_emergencial= cf_assistencia_emergencial(bs)
    cc_orgaos_vinculados= orgaos_vinculados(bs)
    """
    cc_conselho_solidariedade = conselho_solidariedade()
    

if __name__ == "__main__" :
    main ()