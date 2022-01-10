from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from dotenv import load_dotenv
import os
from tinydb import TinyDB, Query


"""
- coletar noticias de todos os ministérios
- inserir no banco json
- gerar html para cada noticia

"""

class NoticiasGovBr:
    def __init__(self, url="NA"):
        self.url = url

    def diretorio(self, nome, ano="NA"):
        env_dir = load_dotenv("../../../.env_local") # procurando a pasta de cima (../)
        DIR_FINAL = os.getenv("DIR_FINAL")
        MINISTERIO = os.getenv(nome)
        cria_dir_banco = os.makedirs(f'{DIR_FINAL}/{MINISTERIO}/banco', exist_ok = True) # makedirs cria diretório
        cria_dir_html = os.makedirs(f'{DIR_FINAL}/{MINISTERIO}/html', exist_ok = True)
        if ano != "NA":
            cria_dir_html_ano = os.makedirs(f'{DIR_FINAL}/{MINISTERIO}/html/{ano}', exist_ok = True)
            dir_html_ano = f'{DIR_FINAL}/{MINISTERIO}/html/{ano}'
        else:
            dir_html_ano = "NA"
        print(f'{DIR_FINAL}/{MINISTERIO}/banco')
        print(f'{DIR_FINAL}/{MINISTERIO}/html')
        return (f'{DIR_FINAL}/{MINISTERIO}/banco', f'{DIR_FINAL}/{MINISTERIO}/html', dir_html_ano)
    
    def acessar_pagina(self,link):
        html = urlopen(link)
        global bsoup
        bsoup = BeautifulSoup(html, "html.parser")
        return bsoup

    def noticias(self): 
        url = self.url
        print(self.url)
        counter = 0 
        list_url_noticias = [] # lista com paginas com links de noticias
        # 5941
        while counter <= 30: 
            domain = f"{self.url}?b_size=30&b_start:int="
            domain += str(counter) 
            counter += 30
            list_url_noticias.append(domain) 
        for url_noticias in list_url_noticias:
            try:
                acessar_pag_com_links_noticias = self.acessar_pagina(url_noticias)
            except:
                pass
            if ("institucional-cidadania" in self.url) or ("mj" in self.url) or ("mec" in self.url) or ("secretariadegoverno" in self.url) or ("mdr" in self.url) or ("turismo" in self.url) or ("mcom" in self.url) or ("mcti" in self.url) or ("saude" in self.url) or ("agricultura" in self.url) or ("mme" in self.url) or ("economia" in self.url) or ("casacivil" in self.url) or ("defesa" in self.url): 
                noticias = acessar_pag_com_links_noticias.find("ul", class_="noticias listagem-noticias-com-foto").find_all("li") # abre a notícia
            elif ("gsi" in self.url) or ("esporte" in self.url) or ("desenvolvimento-social" in self.url) or ("agu" in self.url) or ("cgu" in self.url) or ("secretariageral" in self.url) or ("planalto" in self.url) or ("mdh" in self.url) or ("infraestrutura" in self.url) or ("mma" in self.url):
                noticias = acessar_pag_com_links_noticias.find("div", {"id":"content-core"}).find_all("article") # abre a notícia
            for index, noticia in enumerate(noticias, start=1):
                env_ministerio = url.split("/")[3].upper()
                print(env_ministerio)
                link = noticia.div.h2.a["href"]
                if ("esporte" in link):
                    categoria = "esporte"
                elif ("desenvolvimento-social" in link):
                    categoria = "desenvolvimento-social"
                elif ("institucional-cidadania" in link):
                    categoria = "institucional-cidadania"
                else:
                    categoria = "NA"
                acessar_noticia = self.acessar_pagina(link)
                # entrando
                origem = acessar_noticia.find("meta", property = "og:site_name")["content"]
                print(origem)
                classificado = "notícia"
                titulo = acessar_noticia.find("h1", class_="documentFirstHeading").text
                print(self.url)
                print(f'{index} - TITULO: {titulo}')
                try:
                    publicado = acessar_noticia.find("span", class_="documentPublished").find("span", class_="value").text
                    print(f'DATA DE POSTAGEM: {publicado}')
                except:
                    publicado = "NA"
                try:
                    modificado = acessar_noticia.find("span", class_="documentModified").find("span", class_="value").text
                    print(f'DATA DE ATUALIZAÇÃO: {modificado}')
                except:
                    modificado = "NA"
                try:
                    paragrafos = acessar_noticia.find("div", {"id":"parent-fieldname-text"}).text
                except:
                    paragrafos = "NA"
                # print(f'CONTEÚDO: {paragrafos}')
                # tags das notícias
                tags = []
                try: 
                    tags_noticia = acessar_noticia.find("div", {"id":"category"}).find_all("span")
                    for tag in tags_noticia:
                        tags.append(tag.text)
                except:
                    tags.append("NA")
                if tags[0] != 'NA' :
                    del tags[0]
                print(f'TAGS: {tags}')
                subtitulo = "NA"
                link_archive = "NA"
                # categoria = "NA"
                data = publicado[:10]
                horario = publicado[-5:]
                data_atualizado = modificado[:10]
                horario_atualizado = modificado[-5:]
                local = "NA"
                autoria = "NA"
                dir_local = "NA"
                extra_01 = "NA"
                extra_02 = "NA"
                extra_03 = "NA"
                inserir_banco = self.inserir_bd(env_ministerio, origem, classificado, titulo, subtitulo, link, link_archive, categoria, data, horario, data_atualizado, horario_atualizado, local, autoria, tags, paragrafos, dir_local, extra_01, extra_02, extra_03)
    
    def inserir_bd(self, env_ministerio="NA", origem="NA", classificado="NA", titulo="NA", subtitulo="NA", link="NA", link_archive="NA", categoria="NA", data="NA", horario="NA", data_atualizado="NA", horario_atualizado="NA", local="NA", autoria="NA", tags="NA", paragrafos="NA", dir_local="NA", extra_01="NA", extra_02="NA", extra_03="NA"):
        DIR_FINAL = self.diretorio(env_ministerio)[0]
        nome_bd_json = env_ministerio 
        excluir_json = os.remove(f'{DIR_FINAL}/{nome_bd_json}.json')
        db = TinyDB(f'{DIR_FINAL}/{nome_bd_json}.json', ensure_ascii = False)
        dir_local = f'{DIR_FINAL}/{nome_bd_json}.json'
        User = Query()
        verifica_bd = db.contains((User.titulo == titulo)&(User.data == data)&(User.horario == horario))
        try:
            if not verifica_bd:
                print("Não está na base")
                db.insert({
                    "origem": origem, 
                    "classificado": classificado,
                    "titulo": titulo,
                    "subtitulo": subtitulo,
                    "link": link,
                    "link_archive": link_archive,
                    "categoria": categoria,
                    "data": data,
                    "horario": horario,
                    "data_atualizado": data_atualizado,
                    "horario_atualizado": horario_atualizado,
                    "local": local,
                    "autoria": autoria,
                    "tags": tags,
                    "paragrafos": paragrafos,
                    "dir_local": dir_local,
                    "extra_01": "NA", # categoria_link
                    "extra_02": "NA",
                    "extra_03": "NA"
                })
            else:
                print("Já está na base")
        except:
            pass

def main():
    urls = ["https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/institucional-cidadania", "https://www.gov.br/gsi/pt-br/assuntos/noticias", "https://www.gov.br/mj/pt-br/assuntos/noticias", "https://www.gov.br/mec/pt-br/assuntos/noticias", "https://www.gov.br/secretariadegoverno/pt-br/assuntos/noticias", "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/esporte/noticias_esporte", "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/desenvolvimento-social/noticias-desenvolvimento-social", "https://www.gov.br/agu/pt-br/comunicacao/noticias", "https://www.gov.br/cgu/pt-br/assuntos/noticias", "https://www.gov.br/secretariageral/pt-br/assuntos/noticias", "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias", "https://www.gov.br/mdr/pt-br/noticias", "https://www.gov.br/turismo/pt-br/assuntos/noticias", "https://www.gov.br/mcom/pt-br/noticias", "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias", "https://www.gov.br/saude/pt-br/assuntos/noticias", "https://www.gov.br/agricultura/pt-br/assuntos/noticias", "https://www.gov.br/mdh/pt-br/assuntos/noticias", "https://www.gov.br/mme/pt-br/assuntos/noticias", "https://www.gov.br/economia/pt-br/assuntos/noticias", "https://www.gov.br/casacivil/pt-br/assuntos/noticias", "https://www.gov.br/infraestrutura/pt-br/assuntos/noticias", "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias", "https://www.gov.br/mma/pt-br/assuntos/noticias"]
    # govbr = NoticiasGovBr()
    # diretorios = govbr.diretorio("CIDADANIA")
    for url in urls:
        govbr = NoticiasGovBr(url)
        coleta = govbr.noticias()

if __name__=="__main__":
    main()