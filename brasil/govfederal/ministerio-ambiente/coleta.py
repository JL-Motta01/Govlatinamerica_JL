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


def acoes():
    url = "https://www.gov.br/mma/pt-br/acesso-a-informacao/acoes-e-programas" 
    ma_page = page_access(url)


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
