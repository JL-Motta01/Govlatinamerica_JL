from io import DEFAULT_BUFFER_SIZE
from urllib import parse
from urllib.request import urlopen
import urllib
import urllib.request #realizar requisição da página html
import os #para especificar o caminho do download
import wget
import csv
from tinydb import TinyDB,Query
from urllib.parse import urlparse #realizar parseamento do html
from bs4 import BeautifulSoup #importa o beautifulsoup para extrair as infos das tags
from pprint import pprint #organizar estéticamente os prints
from tinydb.operations import add
from datetime import date, timedelta, datetime


DIR_LOCAL= "/home/labri_joaomotta/codigo"

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"


def acessar_pagina(url):
    """Analisa os boletim do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def datas():
    data_inicio = date (2019,1,1)
    data_fim = date.today()
    delta = data_fim - data_inicio
    lista_data = []
    for dia in range(delta.days+1):
        dia_delta = data_inicio + timedelta(days=dia)
        lista_data.append(dia_delta)
    lista_data_final = [datetime.strftime(dt,format="%Y-%m-%d") for dt in lista_data]
    return lista_data_final

def agenda(urlbase):
    """Percorre as datas da agenda"""
    #lista_data = datas()
    lista_data = ["2021-11-10","2021-11-11"]
    url_base = urlbase
    lista_url_data = []
    for data in lista_data:
        url= url_base+data
        lista_url_data.append(url)
    return lista_url_data

def coleta_compromissos(ag, origem):
    """coleta os compromissos de cada dia"""
    print("Entrando na função coleta compromisso. agenda: ",ag)
    for dia in agenda(ag):
        db = TinyDB(f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/db_agenda_ministerios.json", ensure_ascii=False)
        User = Query()
        try:
            pagina_dia = acessar_pagina(dia)
            url=dia
            data=pagina_dia.find("span", {"id":"breadcrumbs-current"}).text
            try:
                lista_conteudo=[]
                compromissos = pagina_dia.find("ul", class_="list-compromissos").find_all("div", class_="item-compromisso")
                for conteudo in compromissos:
                    detalhes=[]
                    titulo=conteudo.find("h2", class_="compromisso-titulo").text
                    print(titulo)
                    detalhes.append(titulo)
                    horario=conteudo.find("div", class_="horario").text
                    detalhes.append(horario)
                    local=conteudo.find("div", class_="compromisso-local").text
                    detalhes.append(local)
                    detalhes.append(data)
                    detalhes.append(url)
                    lista_conteudo.append(detalhes)
            except:
                lista_conteudo= "NA" 
            for detalhe in lista_conteudo:
                print(detalhe)
                db_planalto = db.contains((User.compromisso==detalhe[0])&(User.data==detalhe[3][-10:])&(User.horario==detalhe[1]))
                if not db_planalto:
                    print("não está na base")
                    db.insert({
                        "origem" : origem,
                        "classificado_como" : "compromiso de agenda",
                        "titulo" : detalhe[0],
                        "subtitulo" : "NA",
                        "link" : detalhe[4],
                        "link_archive" : "NA",
                        "data" : detalhe[3][-10:],
                        "horario" : detalhe[1].replace("              ","").replace("\n",""), 
                        "data_atualizado_em" : "NA", 
                        "horario_atualizado_em" : "NA",
                        "local_do_compromisso" : detalhe[2],
                        "autoria" : detalhe[3][:10],
                        "tags" : "NA",
                        "conteudo" : "NA",
                        "dir_local" : "/media/hdvm10/bd/003/001/001/001/001-b/govlatinamerica/brasil/govfederal/govbr/bd"
                        })
                else:
                    print("está na base")
        except:
            pass
        
def acesso_ministerios ():
    lista_ministerios = [
        "https://www.gov.br/casacivil/pt-br/acesso-a-informacao/agendas-da-casa-civil",
        "https://www.gov.br/mre/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/mma/pt-br/acesso-a-informacao/agenda-de-autoridades-1",
        "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/agendas-de-autoridades",
        "https://www.gov.br/mme/pt-br/acesso-a-informacao/agendas-de-autoridades",
        "https://www.gov.br/defesa/pt-br/acesso-a-informacao/agenda-de-autoridades"
        ##"https://www.gov.br/economia/pt-br/acesso-a-informacao/agendas-de-autoridades"
        ]
    lista_agenda = []
    for ministerio in lista_ministerios:
        lista_link = []
        lista_link.append(ministerio)
        acesso_ministerio = acessar_pagina(ministerio)
        """Teste para ministerios difereines"""
        #ministérios que direcionam para as agendas a partir de card contents (MRE)
        agendas = acesso_ministerio.find_all("a", class_="govbr-card-content")
        if agendas:
            try:
                #ministérios que direcionam para as secretarias a partir de card contents (MMA)
                #Nesse caso, acessa cada secretaria e lista as agendas de seus membros, também em card contents
                for link in agendas:
                    acesso_agenda_reduzida = acessar_pagina(link)
                    corrige = acesso_agenda_reduzida.find_all("a", class_="govbr-card-content")
                    for item in corrige:
                        agendas.remove(link)                  
                        agendas.append(item["href"])
            except:
                pass           
            try:
                #Verifica se o link  da agenda direciona para uma versão simplificada da mesma (Comum no MMA)
                #Neste caso, busca o link da agenda completa
                for link in agendas:
                    corrige_agenda = []
                    acesso_agenda_reduzida = acessar_pagina(link)
                    link_agenda_completa = acesso_agenda_reduzida.find("div", class_="agenda-tile-footer").find("a")
                    agenda_completa =link_agenda_completa["href"]
                    corrige_agenda.append(agenda_completa)
                agendas = corrige_agenda
            except:
                pass
        if not agendas:
            #Ministérios com uso de drop-down-lists que contém os links para as agendas (Casa civil, MME e Ministério da defesa)
            agendas = acesso_ministerio.find_all("a", class_="calendario")
        if not agendas:
            #Ministérios que usam listas simples de links para as agendas (Ministério da infraestrutura)
            agendas = acesso_ministerio.find_all("a", class_="internal-link")
        if not agendas:
            #Caso não se enquadre, solicita revisão do ministério (Ministério da economia, atualmente fora do ar)
            print("rever ministério: ", ministerio)
        for agenda in agendas:
            link = agenda["href"]
            lista_link.append(link)
        lista_agenda.append(lista_link)
    return lista_agenda

def coleta_agendas ():
    for ministerio in acesso_ministerios():
        pagina_inicial = acessar_pagina(ministerio[1])
        origem = pagina_inicial.find("div", class_="site-name").find("a").text
        print(origem)
        for agenda in ministerio[1:]:
            coleta_compromissos(agenda,origem)


def main ():
    """Função principal"""
    coleta_agendas()

if __name__ == "__main__":
    main()