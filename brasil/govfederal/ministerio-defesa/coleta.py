from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup

def notas(): # check
    url = "https://www.gov.br/defesa/pt-br/area-de-imprensa/notas-oficiais" 
    md_page = page_access(url)
    # título
    title_notas = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_notas = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_notas = md_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_notas = md_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_notas = []
    links_notas = md_page.find("div", {"id":"content-core"}).find_all("ul")
    for ul_notas in links_notas:
        list_links_notas.append(ul_notas.li.a["href"])


def artigos(): # in progress
    url = "https://www.gov.br/defesa/pt-br/area-de-imprensa/artigos-e-entrevistas-do-ministro" 
    md_page = page_access(url)
    # título
    title_artigos = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_artigos = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_artigos = md_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_artigos = []
    while counter < 21:
        domain = "https://www.gov.br/defesa/pt-br/area-de-imprensa/artigos-e-entrevistas-do-ministro?b_start:int="
        domain += str(counter) 
        counter += 20
        list_url_artigos.append(domain)
    for url_artigos in list_url_artigos:
        # conteúdo
        content_artigos = md_page.find("div", {"id":"entries"}).find_all("article")
        for article_artigos in content_notas:
            link_artigos = page_access(article_notas.span.a["href"]) # ARRUMAR
            # entrandoo
            title_link_artigos = link_artigos.find("h1", class_="documentFirstHeading").text
            post_link_artigos = md_page.find("span", class_="documentPublished").find("span", class_="value").text
            update_link_artigos = md_page.find("span", class_="documentModified").find("span", class_="value").text
            content_link_artigos = md_page.find("div", {"id":"parent-fieldname-text"}).text


def planejamento():
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/auditorias-1/planejamento-estrategico-e-operacional" 
    md_page = page_access(url)

def receitas():
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/despesas-1" 
    md_page = page_access(url)

def infos():
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/informacoes-classificadas-e-desclassificadas" 
    md_page = page_access(url)

def base_dados():
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/dados-abertos/bases-de-dados-do-ministerio-da-defesa" 
    md_page = page_access(url)

def infograficos():
    url = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/publicacoes/infograficos?b_start:int=0" 
    md_page = page_access(url)

def corona():
    url = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/publicacoes/coronavirus" 
    md_page = page_access(url)

def noticias():
    url = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias" 
    md_page = page_access(url)

def main():
    global bs
    url = "https://www.gov.br/economia/pt-br"
    bs = page_access(url)  
    md_notas = notas()
    # md_artigos = artigos()
    # md_planejamento = planejamento()
    # md_receitas = receitas()
    # md_infos = infos()
    # md_base_dados = base_dados()
    # md_infograficos = infograficos()
    # md_corona = corona()
    # md_noticias = noticias()   


if __name__ == "__main__":
    main()
