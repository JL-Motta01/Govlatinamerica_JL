from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



"""
- coletar noticias de todos os ministérios
- inserir no banco json
- gerar html para cada noticia

"""

class NoticiasGovBr:
    def __init__(self, url):
        self.url = url


    def acessar_pagina(self,link):
        html = urlopen(link)
        global bsoup
        bsoup = BeautifulSoup(html, "html.parser")
        return bsoup

    def noticias(self): # check
        link = self.url
        print(self.url)
        md_page = self.acessar_pagina(link)
        title_pag_noticias = md_page.find("h1", class_="documentFirstHeading").text
        data_post_pag_noticias = md_page.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            data_update_pag_noticias = md_page.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass # >> sem data de atualização
        counter = 0 
        list_url_noticias = [] # lista com paginas com links de noticias
        # 5941
        while counter <= 30: 
            domain = f"{self.url}?b_size=30&b_start:int="
            domain += str(counter) 
            counter += 30
            list_url_noticias.append(domain) 
        for url_noticias in list_url_noticias:
            acessar_pag_com_links_noticias = self.acessar_pagina(url_noticias)
            if ("mj" in self.url) or ("mec" in self.url) or ("secretariadegoverno" in self.url) or ("institucional-cidadania" in self.url) or ("mdr" in self.url) or ("turismo" in self.url) or ("mcom" in self.url) or ("mcti" in self.url) or ("saude" in self.url) or ("agricultura" in self.url) or ("mme" in self.url) or ("economia" in self.url) or ("casacivil" in self.url) or ("defesa" in self.url): 
                noticias = acessar_pag_com_links_noticias.find("ul", class_="noticias listagem-noticias-com-foto").find_all("li")
            elif ("gsi" in self.url) or ("esporte" in self.url) or ("desenvolvimento-social" in self.url) or ("agu" in self.url) or ("cgu" in self.url) or ("secretariageral" in self.url) or ("planalto" in self.url) or ("mdh" in self.url) or ("infraestrutura" in self.url) or ("mma" in self.url):
                noticias = acessar_pag_com_links_noticias.find("div", {"id":"content-core"}).find_all("article")
            for index, noticia in enumerate(noticias, start=1):
                link_noticia = noticia.div.h2.a["href"]
                acessar_noticia = self.acessar_pagina(link_noticia)
                # entrando
                titulo = acessar_noticia.find("h1", class_="documentFirstHeading").text
                print(self.url)
                print(f'{index} - TITULO: {titulo}')
                try:
                    data_post = acessar_noticia.find("span", class_="documentPublished").find("span", class_="value").text
                    # print(f'DATA DE POSTAGEM: {data_post}')
                except:
                    pass
                try:
                    data_update = acessar_noticia.find("span", class_="documentModified").find("span", class_="value").text
                    # print(f'DATA DE ATUALIZAÇÃO: {data_update}')
                except:
                    pass
                conteudo_paragrafos = acessar_noticia.find("div", {"id":"parent-fieldname-text"}).text
                # print(f'CONTEÚDO: {conteudo_paragrafos}')
                # tags das notícias
                lista_tags_noticia = []
                try: 
                    tags_noticia = acessar_noticia.find("div", {"id":"category"}).find_all("span")
                    for tag_noticia in tags_noticia:
                        lista_tags_noticia.append(tag_noticia.text)
                except:
                    lista_tags_noticia.append("notícia sem tag")
                if lista_tags_noticia[0] != 'notícia sem tag' :
                    del lista_tags_noticia[0]
                # print(f'TAGS: {lista_tags_noticia}')
    
def main():
    urls = ["https://www.gov.br/gsi/pt-br/assuntos/noticias", "https://www.gov.br/mj/pt-br/assuntos/noticias", "https://www.gov.br/mec/pt-br/assuntos/noticias", "https://www.gov.br/secretariadegoverno/pt-br/assuntos/noticias", "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/esporte/noticias_esporte", "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/desenvolvimento-social/noticias-desenvolvimento-social", "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/institucional-cidadania", "https://www.gov.br/agu/pt-br/comunicacao/noticias", "https://www.gov.br/cgu/pt-br/assuntos/noticias", "https://www.gov.br/secretariageral/pt-br/assuntos/noticias", "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias", "https://www.gov.br/mdr/pt-br/noticias", "https://www.gov.br/turismo/pt-br/assuntos/noticias", "https://www.gov.br/mcom/pt-br/noticias", "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias", "https://www.gov.br/saude/pt-br/assuntos/noticias", "https://www.gov.br/agricultura/pt-br/assuntos/noticias", "https://www.gov.br/mdh/pt-br/assuntos/noticias", "https://www.gov.br/mme/pt-br/assuntos/noticias", "https://www.gov.br/economia/pt-br/assuntos/noticias", "https://www.gov.br/casacivil/pt-br/assuntos/noticias", "https://www.gov.br/infraestrutura/pt-br/assuntos/noticias", "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias", "https://www.gov.br/mma/pt-br/assuntos/noticias"]
    for url in urls:
        govbr = NoticiasGovBr(url)
        coleta = govbr.noticias() 

if __name__=="__main__":
    main()