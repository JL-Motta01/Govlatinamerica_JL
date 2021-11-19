from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias(): # check
    url = "https://www.gov.br/mma/pt-br/assuntos/noticias" 
    ma_page = page_access(url)
    # título
    title_noticias = ma_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_noticias = ma_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_noticias = ma_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_noticias = []
    while counter < 991:
        domain = "https://www.gov.br/mma/pt-br/assuntos/noticias?b_start:int="
        domain += str(counter) 
        counter += 30
        list_url_noticias.append(domain)
    for url_noticias in list_url_noticias:
        # conteúdo
        content_noticias = ma_page.find("div", {"id":"content-core"}).find_all("article")
        for article_noticias in content_noticias:
            link_noticias = page_access(article_noticias.div.h2.a["href"]) 
            # entrando
            title_link_noticias = link_noticias.find("h1", class_="documentFirstHeading").text
            try:
                post_link_noticias = link_noticias.find("span", class_="documentPublished").find("span", class_="value").text
                update_link_noticias = link_noticias.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            content_link_noticias = link_noticias.find("div", {"id":"parent-fieldname-text"}).text
            # tags notícias
            lista_tags_noticias = []
            try: 
                tags_noticias = link_noticias.find("div", {"id":"category"}).find_all("span")
                for span_noticias in tags_noticias:
                    lista_tags_noticias.append(span_noticias.text)
            except:
                lista_tags_noticias.append("notícia sem tag")
            if lista_tags_noticias[0] != 'notícia sem tag' :
                del lista_tags_noticias[0]


def acoes(): # in progress
    url = "https://www.gov.br/mma/pt-br/acesso-a-informacao/acoes-e-programas" 
    ma_page = page_access(url)
    list_cards = []  
    cards = ma_page.find("div", class_="wrapper").find_all("div", class_="card")  
    for card in cards:
        list_cards.append(card.a["href"]) 
    if list_cards[0]: # check
        acoes_metas = page_access(list_cards[0])
        title_acoes_metas = acoes_metas.find("h1", class_="documentFirstHeading").text
        post_acoes_metas = acoes_metas.find("span", class_="documentPublished").find("span", class_="value").text
        update_acoes_metas = acoes_metas.find("span", class_="documentModified").find("span", class_="value").text
        content_acoes_metas = acoes_metas.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_acoes_metas = []
        links_acoes_metas = acoes_metas.find("div", {"id":"content-core"}).find_all("ul")
        for ul_acoes_metas in links_acoes_metas:
            list_links_acoes_metas.append(ul_acoes_metas.li.a["href"])
    if list_cards[1]: # check
        acoes_ti = page_access(list_cards[1])
        title_acoes_ti = acoes_ti.find("h1", class_="documentFirstHeading").text
        post_acoes_ti = acoes_ti.find("span", class_="documentPublished").find("span", class_="value").text
        update_acoes_ti = acoes_ti.find("span", class_="documentModified").find("span", class_="value").text
        content_acoes_ti = acoes_ti.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_acoes_ti = []
        links_acoes_ti = acoes_ti.find("div", {"id":"content-core"}).find_all("a")
        for a_acoes_ti in links_acoes_ti:
            list_links_acoes_ti.append(a_acoes_ti["href"])  
    if list_cards[2]: # check
        acoes_planejamento = page_access(list_cards[2])
        title_acoes_planejamento = acoes_planejamento.find("h1", class_="documentFirstHeading").text
        post_acoes_planejamento = acoes_planejamento.find("span", class_="documentPublished").find("span", class_="value").text
        update_acoes_planejamento = acoes_planejamento.find("span", class_="documentModified").find("span", class_="value").text
        content_acoes_planejamento = acoes_planejamento.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_acoes_planejamento = []
        links_acoes_planejamento = acoes_planejamento.find("div", {"id":"content-core"}).find_all("li")
        for li_acoes_planejamento in links_acoes_planejamento:
            list_links_acoes_planejamento.append(li_acoes_planejamento.a["href"])
    if list_cards[3]: # check
        acoes_plano = page_access(list_cards[3])
        title_acoes_plano = acoes_plano.find("h1", class_="documentFirstHeading").text
        post_acoes_plano = acoes_plano.find("span", class_="documentPublished").find("span", class_="value").text
        update_acoes_plano = acoes_plano.find("span", class_="documentModified").find("span", class_="value").text
        content_acoes_plano = acoes_plano.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_acoes_plano = []
        links_acoes_plano = acoes_plano.find("div", {"id":"content-core"}).find_all("a")
        for a_acoes_plano in links_acoes_plano:
            list_links_acoes_plano.append(a_acoes_plano["href"])
    if list_cards[4]: # in progress !!!!
        acoes_plano = page_access(list_cards[3])
        title_acoes_plano = acoes_plano.find("h1", class_="documentFirstHeading").text
        post_acoes_plano = acoes_plano.find("span", class_="documentPublished").find("span", class_="value").text
        update_acoes_plano = acoes_plano.find("span", class_="documentModified").find("span", class_="value").text
        content_acoes_plano = acoes_plano.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_acoes_plano = []
        links_acoes_plano = acoes_plano.find("div", {"id":"content-core"}).find_all("a")
        for a_acoes_plano in links_acoes_plano:
            list_links_acoes_plano.append(a_acoes_plano["href"])


def infos(): # check
    url = "https://www.gov.br/mma/pt-br/acesso-a-informacao/informacoes-classificadas" 
    ma_page = page_access(url)
    # título
    title_infos = ma_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_infos = ma_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infos = ma_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_infos = ma_page.find("div", {"id":"parent-fieldname-text"}).text
    list_links_infos = []
    links_infos = ma_page.find("div", {"id":"content-core"}).find_all("a")
    for a_infos in links_infos:
        list_links_infos.append(a_infos["href"])


def dados(): # check
    url = "https://www.gov.br/mma/pt-br/acesso-a-informacao/dados-abertos-integridade" 
    ma_page = page_access(url)
    list_cards = []  
    cards = ma_page.find("div", class_="wrapper").find_all("div", class_="card")  
    for card in cards:
        list_cards.append(card.a["href"]) 
    if list_cards[0]: # check
        dados_abertos = page_access(list_cards[0])
        title_dados_abertos = dados_abertos.find("h1", class_="documentFirstHeading").text
        post_dados_abertos = dados_abertos.find("span", class_="documentPublished").find("span", class_="value").text
        update_dados_abertos = dados_abertos.find("span", class_="documentModified").find("span", class_="value").text
        content_dados_abertos = dados_abertos.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_dados_abertos = []
        links_dados_abertos = dados_abertos.find("div", {"id":"content-core"}).find_all("a")
        for a_dados_abertos in links_dados_abertos:
            list_links_dados_abertos.append(a_dados_abertos["href"])
    if list_cards[1]: # check
        dados_integridade = page_access(list_cards[1])
        title_dados_integridade = dados_integridade.find("h1", class_="documentFirstHeading").text
        post_dados_integridade = dados_integridade.find("span", class_="documentPublished").find("span", class_="value").text
        update_dados_integridade = dados_integridade.find("span", class_="documentModified").find("span", class_="value").text
        content_dados_integridade = dados_integridade.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_dados_integridade = []
        links_dados_integridade = dados_integridade.find("div", {"id":"content-core"}).find_all("ul")
        for ul_dados_integridade in links_dados_integridade:
            list_links_dados_integridade.append(ul_dados_integridade.li.a["href"])


def relatorios(): # almost check
    url = "https://www.gov.br/mma/pt-br/acesso-a-informacao/relatorios" 
    ma_page = page_access(url)
    # título
    title_relatorios = ma_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_relatorios = ma_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_relatorios = ma_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_relatorios = ma_page.find("div", class_="entries").find_all("article")
    for article_relatorios in content_relatorios:
        link_relatorios = page_access(article_relatorios.span.a["href"]) 
        # entrando
        try:
            title_link_relatorios = link_relatorios.find("h1", class_="documentFirstHeading").text
            post_link_relatorios = link_relatorios.find("span", class_="documentPublished").find("span", class_="value").text # ARRUMAR
            update_link_relatorios = link_relatorios.find("span", class_="documentModified").find("span", class_="value").text # ARRUMAR
        except:
            pass
        list_links_relatorios = []
        try:
            links_relatorios = link_relatorios.find("div", {"id":"content-core"}).find_all("a")
            for a_relatorios in links_relatorios:
                list_links_relatorios.append(a_relatorios["href"])
        except:
            pass
        

def main():
    global bs
    url = "https://www.gov.br/mma/pt-br"
    bs = page_access(url) 
    # ma_noticias = noticias()   
    ma_acoes = acoes() 
    # ma_infos = infos() 
    # ma_dados = dados() 
    # ma_relatorios = relatorios() 


if __name__ == "__main__":
    main()
