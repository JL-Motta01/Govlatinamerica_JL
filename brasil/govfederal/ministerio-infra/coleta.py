from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "" 
    mi_page = page_access(url)


def arq_rel():
    url = "" 
    mi_page = page_access(url)


def ri():
    url = "" 
    mi_page = page_access(url)


def planos():
    url = "" 
    mi_page = page_access(url)


def rel_orc():
    url = "" 
    mi_page = page_access(url)


def ppa():
    url = "" 
    mi_page = page_access(url)


def arq_ppa():
    url = "" 
    mi_page = page_access(url)


def pdtic():
    url = "" 
    mi_page = page_access(url)


def cgd():
    url = "" 
    mi_page = page_access(url)


def auditorias():
    url = "" 
    mi_page = page_access(url)


def dados():
    url = "" 
    mi_page = page_access(url)


def demonstracoes():
    url = "" 
    mi_page = page_access(url)


def rel_gestao():
    url = "" 
    mi_page = page_access(url)


def responsaveis():
    url = "" 
    mi_page = page_access(url)


def cronologia():
    url = "" 
    mi_page = page_access(url)


def convenios():
    url = "" 
    mi_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/infraestrutura/pt-br"
    bs = page_access(url) 
    mi_noticias = noticias() 
    mi_arq_rel = arq_rel() 
    mi_ri = ri() 
    mi_planos = planos() 
    mi_rel_orc = rel_orc() 
    mi_ppa = ppa() 
    mi_arq_ppa = arq_ppa() 
    mi_pdtic = pdtic() 
    mi_cgd = cgd() 
    mi_auditorias = auditorias() 
    mi_dados = dados() 
    mi_demonstracoes = demonstracoes() 
    mi_rel_gestao = rel_gestao() 
    mi_responsaveis = responsaveis() 
    mi_cronologia = cronologia() 
    mi_convenios = convenios() 


if __name__ == "__main__":
    main()