from urllib.request import urlopen
from bs4 import BeautifulSoup



"""
- coletar noticias de todos os ministérios
- inserir no banco json
- gerar html para cada noticia

"""

class NoticiasGovBr:
    def __init__(self, url):
        self.url = url


    def acessar_pagina(self,link):
        html = urlopen(link)  # retorna a página da função links_navigation
        global bsoup
        bsoup = BeautifulSoup(html, "html.parser")
        return bsoup

    def noticias(self): # check
        link = self.url
        md_page = self.acessar_pagina(link)
        title_noticias = md_page.find("h1", class_="documentFirstHeading").text
        post_noticias = md_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_noticias = md_page.find("span", class_="documentModified").find("span", class_="value").text
        counter = 0 
        list_url_noticias = [] # lista com paginas com links de noticias
        while counter < 5941:
            domain = "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias?b_size=60&b_start:int="
            domain += str(counter) 
            counter += 60
            list_url_noticias.append(domain) 
        for url_noticias in list_url_noticias:
            acessar_pag_com_links_noticias = self.acessar_pagina(url_noticias)
            noticias = acessar_pag_com_links_noticias.find("ul", class_="noticias listagem-noticias-com-foto").find_all("li")
            for noticia in noticias:
                link_noticia = noticia.div.h2.a["href"]
                acessar_noticia = self.acessar_pagina(link_noticia)
                # entrando
                titulo = acessar_noticia.find("h1", class_="documentFirstHeading").text
                print(f'TITULO: {titulo}')
                try:
                    post_link_noticias = acessar_noticia.find("span", class_="documentPublished").find("span", class_="value").text
                    update_link_noticias = acessar_noticia.find("span", class_="documentModified").find("span", class_="value").text
                    print(post_link_noticias)
                except:
                    pass
                content_link_noticias = acessar_noticia.find("div", {"id":"parent-fieldname-text"})
                # tags notícias
                lista_tags_noticias = []
                try: 
                    tags_noticias = acessar_noticia.find("div", {"id":"category"}).find_all("span")
                    for span_noticias in tags_noticias:
                        lista_tags_noticias.append(span_noticias.text)
                except:
                    lista_tags_noticias.append("notícia sem tag")
                if lista_tags_noticias[0] != 'notícia sem tag' :
                    del lista_tags_noticias[0]
    
def main():
    url= "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias"
    govbr = NoticiasGovBr(url)
    coleta = govbr.noticias() 

if __name__=="__main__":
    main()