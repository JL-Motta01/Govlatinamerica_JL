import os
import sys
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
print(f'DIR PROJETO: {DIR_PROJETO}')
# from templates.diretorios.diretorio import diretorios, diretorios_template 
from brasil.govfederal.coleta.coleta_noticias import NoticiasGovBr
from templates.template_html.html_template import html_consultar_json
from templates.internet_archive.internet_archive import archive_consultar_json


def url_base():
    urls = [
        "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/institucional-cidadania", 
        "https://www.gov.br/gsi/pt-br/assuntos/noticias", 
        "https://www.gov.br/mj/pt-br/assuntos/noticias", 
        "https://www.gov.br/mec/pt-br/assuntos/noticias", 
        "https://www.gov.br/secretariadegoverno/pt-br/assuntos/noticias", 
        "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/esporte/noticias_esporte", 
        "https://www.gov.br/cidadania/pt-br/noticias-e-conteudos/desenvolvimento-social/noticias-desenvolvimento-social", 
        "https://www.gov.br/agu/pt-br/comunicacao/noticias", 
        # "https://www.gov.br/cgu/pt-br/assuntos/noticias", 
        # "https://www.gov.br/secretariageral/pt-br/assuntos/noticias", 
        # "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias", 
        # "https://www.gov.br/mdr/pt-br/noticias", 
        # "https://www.gov.br/turismo/pt-br/assuntos/noticias", 
        # "https://www.gov.br/mcom/pt-br/noticias", 
        # "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias", 
        # "https://www.gov.br/saude/pt-br/assuntos/noticias", 
        # "https://www.gov.br/agricultura/pt-br/assuntos/noticias", 
        # "https://www.gov.br/mdh/pt-br/assuntos/noticias", 
        # "https://www.gov.br/mme/pt-br/assuntos/noticias", 
        # "https://www.gov.br/economia/pt-br/assuntos/noticias", 
        # "https://www.gov.br/casacivil/pt-br/assuntos/noticias", 
        # "https://www.gov.br/infraestrutura/pt-br/assuntos/noticias", 
        # "https://www.gov.br/defesa/pt-br/centrais-de-conteudo/noticias", 
        # "https://www.gov.br/mma/pt-br/assuntos/noticias"
        ]
    return urls


def main():
    urls = url_base()
    nomes = []
    # coleta informações 
    for url in urls:
        nomes.append(url.split("/")[3].upper())
        govbr = NoticiasGovBr(url)
        coleta = govbr.noticias()
    salvar_internet_archive = archive_consultar_json(nomes)
    gerar_html = html_consultar_json(nomes)

if __name__=="__main__":
    main()