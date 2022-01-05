from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/turismo/pt-br/assuntos/noticias"
    pass


def corona(): # check
    url = "https://www.gov.br/turismo/pt-br/assuntos/coronavirus"
    mtur_page = page_access(url)
    title_corona = mtur_page.find("h1", class_="documentFirstHeading").text
    post_corona = mtur_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_corona = mtur_page.find("span", class_="documentModified").find("span", class_="value").text
    content_corona = mtur_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_links_corona = []
    links_corona = mtur_page.find("div", {"id":"content-core"}).find_all("a", rel="noopener noreferrer")
    for a_corona in links_corona:
        list_links_corona.append(a_corona["href"])
    del(list_links_corona[1::])


def acordos(): # check
    url = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/acordos"
    mtur_page = page_access(url)
    title_acordos = mtur_page.find("h1", class_="documentFirstHeading").text
    post_acordos = mtur_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_acordos = mtur_page.find("span", class_="documentModified").find("span", class_="value").text
    content_acordos = mtur_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_link_acordos = []
    link_acordos = mtur_page.find("div", {"id":"content-core"}).find_all("a")
    for a_acordos in link_acordos:
        try:
            acordos_pages = page_access(a_acordos["href"])
            link_acordos_pages = acordos_pages.find("div", {"id" : "content-core"}).find_all("a")
            for a_acordos_pages in link_acordos_pages:
                list_link_acordos.append(a_acordos_pages["href"])
        except:
            list_link_acordos.append(a_acordos["href"])


def cartilha(): # check
    url = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/cartilha-parlamentar"
    mtur_page = page_access(url)
    title_cartilha = mtur_page.find("h1", class_="documentFirstHeading").text
    post_cartilha = mtur_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cartilha = mtur_page.find("span", class_="documentModified").find("span", class_="value").text
    list_link_cartilha = []
    link_cartilha = mtur_page.find("div", {"id":"content-core"}).find_all("a")
    for a_cartilha in link_cartilha:
        list_link_cartilha.append(a_cartilha["href"])


def pesquisas(): # check
    url = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/pesquisas"
    mtur_page = page_access(url)
    title_pesquisas = mtur_page.find("h1", class_="documentFirstHeading").text
    post_pesquisas = mtur_page.find("span", class_="documentPublished").find("span", class_="value").text
    list_link_pesquisas = []
    link_pesquisas = mtur_page.find("div", {"id":"content-core"}).find_all("a")
    for a_pesquisas in link_pesquisas:
        list_link_pesquisas.append(a_pesquisas["href"])


def noticias_secre(): # check
    url = "https://www.gov.br/turismo/pt-br/secretaria-especial-da-cultura/assuntos/noticias"
    mtur_page = page_access(url)
    title_noticias_secre = mtur_page.find("h1", class_="documentFirstHeading").text
    post_noticias_secre = mtur_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_noticias_secre = mtur_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_noticias_secre = []
    while counter < 141:
        domain = "https://www.gov.br/turismo/pt-br/secretaria-especial-da-cultura/assuntos/noticias?b_start:int="
        domain += str(counter) 
        counter += 20
        list_url_noticias_secre.append(domain)
    for url_noticias_secre in list_url_noticias_secre:
        page = page_access(url_noticias_secre)
        # acessando páginas de notícias 
        content_noticias_secre = page.find("div", {"id":"content-core"}).find_all("article")
        for article_noticias_secre in content_noticias_secre:
            link_noticias_secre = page_access(article_noticias_secre.span.a["href"]) 
            # entrando na notícia
            title_link_noticias_secre = link_noticias_secre.find("h1", class_="documentFirstHeading").text
            post_link_noticias_secre = link_noticias_secre.find("span", class_="documentPublished").find("span", class_="value").text
            try:
                update_link_noticias_secre = link_noticias_secre.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            content_link_noticias_secre = link_noticias_secre.find("div", {"id" : "parent-fieldname-text"}).text
            

def cartilha_lit(): # check
    url = "https://www.gov.br/turismo/pt-br/secretaria-especial-da-cultura/centrais-de-conteudo/publicacoes/livro-leitura-literatura-e-bibliotecas/cartilhas-2"
    mtur_page = page_access(url)
    title_cartilha_lit = mtur_page.find("h1", class_="documentFirstHeading").text
    post_cartilha_lit = mtur_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cartilha_lit = mtur_page.find("span", class_="documentModified").find("span", class_="value").text
    content_cartilha_lit = mtur_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_link_cartilha_lit = []
    link_cartilha_lit = mtur_page.find("div", {"id":"content-core"}).find_all("a")
    for a_cartilha_lit in link_cartilha_lit:
        list_link_cartilha_lit.append(a_cartilha_lit["href"])
    del(list_link_cartilha_lit[-1])


def main():
    global bs
    url = "https://www.gov.br/turismo/pt-br/"
    bs = page_access(url) 
    mtur_noticias = noticias()
    mtur_corona = corona()
    mtur_acordos = acordos()
    mtur_cartilha = cartilha()
    mtur_pesquisas = pesquisas()
    mtur_noticias_secre = noticias_secre()
    mtur_cartilha_lit = cartilha_lit()


if __name__ == "__main__":
    main()