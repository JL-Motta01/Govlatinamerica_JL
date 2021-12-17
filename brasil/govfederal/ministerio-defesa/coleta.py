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


def artigos(): # check
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
        page = page_access(url_artigos)
        # conteúdo
        content_artigos = page.find("div", class_="entries").find_all("article")
        for article_artigos in content_artigos:
            link_artigos = page_access(article_artigos.span.a["href"]) 
            # entrando
            title_link_artigos = link_artigos.find("h1", class_="documentFirstHeading").text
            post_link_artigos = link_artigos.find("span", class_="documentPublished").find("span", class_="value").text
            try:
                update_link_artigos = link_artigos.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            content_link_artigos = link_artigos.find("div", {"id":"parent-fieldname-text"}).text
            # tags
            list_tags_artigos = []
            try: 
                tags_artigos = link_artigos.find("div", {"id":"category"}).find_all("span")
                for span_artigos in tags_artigos:
                    list_tags_artigos.append(span_artigos.text)
            except:
                list_tags_artigos.append("Artigo sem tag")
            if list_tags_artigos[0] != 'Artigo sem tag' :
                del list_tags_artigos[0]


def planejamento(): # check
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/auditorias-1/planejamento-estrategico-e-operacional" 
    md_page = page_access(url)
    # título
    title_planejamento = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_planejamento = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_planejamento = md_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_planejamento = md_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_planejamento = []
    links_planejamento = md_page.find("div", {"id":"content-core"}).find_all("ul")
    for ul_planejamento in links_planejamento:
        list_links_planejamento.append(ul_planejamento.li.a["href"])


def receitas(): # check
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/despesas-1" 
    md_page = page_access(url)
    # título
    title_receitas = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_receitas = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_receitas = md_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_receitas = md_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_receitas = []
    links_receitas = md_page.find("div", {"id":"content-core"}).find_all("a")
    for a_receitas in links_receitas:
        list_links_receitas.append(a_receitas["href"])


def infos(): # check
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/informacoes-classificadas-e-desclassificadas" 
    md_page = page_access(url)
    # título
    title_infos = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_infos = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infos = md_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_infos = md_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_infos = []
    links_infos = md_page.find("div", {"id":"content-core"}).find_all("a")
    for a_infos in links_infos:
        list_links_infos.append(a_infos["href"])


def base_dados(): # check
    url = "https://www.gov.br/defesa/pt-br/acesso-a-informacao/dados-abertos/bases-de-dados-do-ministerio-da-defesa" 
    md_page = page_access(url)
    # título
    title_base_dados = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_base_dados = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_base_dados = md_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_base_dados = md_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_base_dados = []
    links_base_dados = md_page.find("div", {"id":"content-core"}).find_all("a")
    for a_base_dados in links_base_dados:
        list_links_base_dados.append(a_base_dados["href"])


def infograficos(): # check
    url = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/publicacoes/infograficos?b_start:int=0" 
    md_page = page_access(url)
    # título
    title_infograficos = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_infograficos = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infograficos = md_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_infograficos = []
    while counter < 21:
        domain = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/publicacoes/infograficos?b_start:int="
        domain += str(counter) 
        counter += 20
        list_url_infograficos.append(domain)
    for url_infograficos in list_url_infograficos:
        page = page_access(url_infograficos)
        # conteúdo
        content_infograficos = page.find("div", class_="entries").find_all("article")
        for article_infograficos in content_infograficos:
            link_infograficos = page_access(article_infograficos.span.a["href"]) 
            # entrando
            title_link_infograficos = link_infograficos.find("h1", class_="documentFirstHeading").text
            post_link_infograficos = link_infograficos.find("span", class_="documentPublished").find("span", class_="value").text
            update_link_infograficos = link_infograficos.find("span", class_="documentModified").find("span", class_="value").text
            content_link_infograficos = link_infograficos.find("div", {"id":"parent-fieldname-text"}).text
            # links
            try: 
                list_links_infograficos = []
                links_infograficos = link_infograficos.find("div", {"id":"content-core"}).find_all("a")
                for a_infograficos in links_infograficos:
                    list_links_infograficos.append(a_infograficos["href"])
            except:
                pass
            

def corona(): # check
    url = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/publicacoes/coronavirus" 
    md_page = page_access(url)
    # título
    title_corona = md_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_corona = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_corona = md_page.find("span", class_="documentModified").find("span", class_="value").text
    # conteúdo
    content_corona = md_page.find("div", class_="entries").find_all("article")
    for article_corona in content_corona:
        link_corona = page_access(article_corona.span.a["href"]) 
        # entrando
        title_link_corona = link_corona.find("h1", class_="documentFirstHeading").text
        post_link_corona = link_corona.find("span", class_="documentPublished").find("span", class_="value").text
        update_link_corona = link_corona.find("span", class_="documentModified").find("span", class_="value").text
        content_link_corona = link_corona.find("div", {"id":"parent-fieldname-text"}).text
        # links
        try: 
            list_links_corona = []
            links_corona = link_corona.find("div", {"id":"content-core"}).find_all("a")
            for a_corona in links_corona:
                list_links_corona.append(a_corona["href"])
        except:
            pass


def noticias(): # check
    url = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias" 
    md_page = page_access(url)
    title_noticias = md_page.find("h1", class_="documentFirstHeading").text
    post_noticias = md_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_noticias = md_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_noticias = []
    while counter < 5941:
        domain = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias?b_size=60&b_start:int="
        domain += str(counter) 
        counter += 60
        list_url_noticias.append(domain)
    for url_noticias in list_url_noticias:
        page = page_access(url_noticias)
        content_noticias = page.find("ul", class_="noticias listagem-noticias-com-foto").find_all("li")
        for li_noticias in content_noticias:
            link_noticias = page_access(li_noticias.div.h2.a["href"]) 
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


def main():
    global bs
    url = "https://www.gov.br/economia/pt-br"
    bs = page_access(url)  
    """
    md_notas = notas()
    md_artigos = artigos()
    md_planejamento = planejamento()
    md_receitas = receitas()
    md_infos = infos()
    md_base_dados = base_dados()
    md_infograficos = infograficos()
    md_corona = corona()
    """
    md_noticias = noticias()   


if __name__ == "__main__":
    main()
