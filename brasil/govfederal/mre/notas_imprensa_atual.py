import requests
from bs4 import BeautifulSoup

def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text, "html.parser")
    # print(bs)
    return bs

def extrair_info():
    bs = acessar_pagina("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/")
    tag_h1 = bs.find("h1").text
    print(tag_h1)
    notas = bs.find_all("article")
    #print(notas)
    for nota in notas:
        titulo = nota.find("h2").text.strip()
        data = nota.find_all("span", class_="summary-view-icon")[0].text.strip()
        horario = nota.find_all("span", class_="summary-view-icon")[1].text.strip()
        num_nota = nota.find("span", class_="subtitle").text.strip()
        link = nota.a["href"]
        print(titulo)
        print(data)
        print (horario)
        print(num_nota)
        print(link)
#//*[@id="content-core"]/article[1]/div/h2/a
#informações importantes: n° da nota, título, data, horário e link para conteúdo

def main():
    extrair_info()


if __name__ == "__main__":
    main()