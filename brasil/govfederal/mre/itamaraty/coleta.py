from urllib.request import build_opener, urlopen  # biblioteca nativa
from bs4 import BeautifulSoup  # biblioteca de terceiros


def acesso_pagina(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    return bs


def pags_notas_imprensa():
    """
    - Percorre as páginas que reunem os links para as notas de imprensa
    - Retorna uma  lista com os links das paginas
    """
    lista_url_notas_imprensa = []
    contador = 0
    while contador < 30:  # 4050
        dominio = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
        dominio += str(contador)
        contador += 30
        lista_url_notas_imprensa.append(dominio)

    return lista_url_notas_imprensa


def links_notas_imprensa():
    lista_pags_notas_imprensa = pags_notas_imprensa()
    for pagina_notas_imprensa in lista_pags_notas_imprensa:
        acessar_pagina = acesso_pagina(pagina_notas_imprensa).find(
            "div", {"id": "content-core"}).find_all("article")
        # div_content_core = acessar_pagina.find(
        #     "div", {"id": "content-core"}).find_all("article")
        for article in acessar_pagina:
            conteudo = conteudo_notas_imprensa(article.h2.a["href"])


def conteudo_notas_imprensa(pagina):
    acessar_pagina = acesso_pagina(pagina)
    print(acessar_pagina.find("p", class_="nitfSubtitle").text)
    print(acessar_pagina.h1.text)
    print(acessar_pagina.find("span", class_="documentPublished").find(
        "span", class_="value").text)
    print(acessar_pagina.find(
        "div", {"id": "content-core"}).find_all("p"))
    paragrafos = [x.get_text() for x in acessar_pagina.find(
        "div", {"id": "content-core"}).find_all("p")]
    print(paragrafos)


def inserir_banco_dados():
    pass


def main():
    links = links_notas_imprensa()


if __name__ == "__main__":
    main()
