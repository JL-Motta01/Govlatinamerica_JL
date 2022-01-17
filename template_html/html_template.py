from yattag import Doc, indent
from tinydb import TinyDB, Query
from dotenv import load_dotenv
import os
from diretorio import diretorios, diretorios_template 


def consultar(template = "NA"):
    ministerios = ["CIDADANIA", "MMA", "PLANALTO"]
    for ministerio in ministerios:
        if template == "ok":
            print("ok")
            diretorio = diretorios_template(ministerio)
        else:
            diretorio = diretorios(ministerio)
        dir_json = diretorio[0]
        dir_html = diretorio[1]
        dir_referencias = diretorio[3]
        dir_estilo = diretorio[4]
        db = TinyDB(f'{dir_json}/{ministerio}.json')
        myDBQuery = Query()
        for dado in iter(db):
            origem = dado['origem']
            classificado = dado['classificado']
            titulo = dado['titulo']
            subtitulo = dado['subtitulo']
            link = dado['link']
            link_archive = dado['link_archive']
            categoria = dado['categoria']
            data = dado['data']
            horario = dado['horario']
            data_atualizado = dado['data_atualizado']
            horario_atualizado = dado['horario_atualizado']
            local = dado['local']
            autoria = dado['autoria']
            tags = dado['tags']
            paragrafos = dado['paragrafos']
            dir_local = dado['dir_local']
            extra_01 = dado['extra_01']
            extra_02 = dado['extra_02']
            extra_03 = dado['extra_03']
            print(data)
            if template == "ok":
                dir_html_ano = diretorios_template(ministerio, data[-4:])[2]
            else:
                dir_html_ano = diretorios(ministerio, data[-4:])[2]
            template_html(dir_html_ano, dir_referencias, dir_estilo, dir_html, origem, classificado, titulo, subtitulo, link, link_archive, categoria, data, horario, data_atualizado, horario_atualizado, local, autoria, tags, paragrafos, dir_local, extra_01, extra_02, extra_03)
            
            print("#################")
            print("#################")

def template_html(dir_html_ano="NA", dir_referencias="NA", dir_estilo="NA", dir_html="NA", origem="NA", classificado="NA", titulo="NA", subtitulo="NA", link="NA", link_archive="NA", categoria="NA", data="NA", horario="NA", data_atualizado="NA", horario_atualizado="NA", local="NA", autoria="NA", tags="NA", paragrafos="NA", dir_local="NA", extra_01="NA", extra_02="NA", extra_03="NA"):
    doc, tag, text = Doc().tagtext()
    paragrafos_avisos = [f'Este texto deve ser utilizado somente para fins acadêmicos. Para qualquer outro fim entrar em contato com a instituição que produziu e/ou divulgou esta informação: {origem}']
    links = ["stylesheet"]
    ESTILO = dir_estilo
    REFERENCIAS = dir_referencias
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8" />')
            for l in links:
                #doc.asis(f'<link rel={l} type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css">')
                #doc.asis(f'<link rel={l} type="/home/labri_juliasilveira/codigo/newscloud/template/reset.css">')
                doc.asis(f'<link rel={l} type="text/css" href={ESTILO}>')
                #doc.asis(f'<link rel={l} type="text/css" href="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/style.css">')
            doc.asis(f'<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
            doc.asis(f'<meta name="origem" content="{origem}">') 
            doc.asis(f'<meta name="classificado" content="{classificado}">') 
            doc.asis(f'<meta name="titulo" content={titulo}>') 
            doc.asis(f'<meta name="subtitulo" content={subtitulo}>')
            doc.asis(f'<meta name="link" content={link}>') 
            doc.asis(f'<meta name="link_archive" content={link_archive}>')
            doc.asis(f'<meta name="data" content="{data}">')
            doc.asis(f'<meta name="horario" content="{horario}">')
            doc.asis(f'<meta name="data_atualizado" content="{data_atualizado}">') 
            doc.asis(f'<meta name="horario_atualizado" content="{horario_atualizado}">') 
            doc.asis(f'<meta name="local" content={local}>') 
            doc.asis(f'<meta name="autoria" content={autoria}>') 
            doc.asis(f'<meta name="tags" content="{tags}">') 
            doc.asis(f'<meta name="dir_local" content="{dir_local}">') # meta tag >> dado sobre os dados / dados sobre a pag.
            
        with tag('body'):
            with tag('div', klass='container'):
                with tag('article', klass="texto-conteudo", id="conteudo-principal"):
                    with tag('div', klass='head-noticia'):
                        with tag('h1'):
                            text(titulo)
                        with tag('h2', klass='subtitulo'):
                            if subtitulo != 'NA':
                                text(subtitulo)
                                
                    with tag('div', klass='corpo-noticia'):
                        with tag('p', id='negrito'):
                            if "NA" in autoria:
                                text(f'{origem.title()}, {data}')
                            else: 
                                text(f'{", ".join(autoria)}, {data}')
                        for paragrafo in paragrafos:
                            with tag('p'):
                                text(paragrafo)


                with tag('div', klass='referencia', id='referencias'):
                    with tag('h4'):
                        #text(f'Como citar: {origem}. {titulo}, {data}. Acesso em: ')
                        #doc.asis(f'<span id="dateAndTime">Como citar: {origem}. {titulo}, {data}. Acesso em: </span>')
                        # MINISTERIODACIDADANIA. 12ª Conferência Nacional da Assistência Social tem Início em Brasília, 16/12/2021, Acesso em: 11 jan. 2022
                        text(f'Como citar: ')
                    with tag('h4'):
                        text(f'{origem.upper()}. ')
                        with tag('span', id='negrito'):
                            text(f'{titulo}, ')
                        text(f'{data}. ')
                        text(f'Acesso em: ')
                        with tag('span', id='dateAndTime'):
                            text(f'Acesso em: ')


                with tag('header', klass="negrito", id="metadados"):
                    with tag('h4'):
                        text('Metadados:')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in autoria:
                                text(f'Origem: {origem.title()}')
                            else: 
                                text(f'Autoria: {", ".join(autoria)}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if classificado == "NA":
                                text(f'Classificado como: Não possui esta informação')
                            else: 
                                text(f'Classificado como: {classificado}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if data == "NA":
                                text(f'Data: Não possui esta informação')
                            text(f'Data: {data}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if horario == "NA":
                                text(f'Horario: Não possui esta informação')
                            text(f'Horario {horario}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if data_atualizado == "NA":
                                text(f'Data de atualização: Não possui esta informação')
                            else:
                                text(f'Data de atualização: {data_atualizado}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if horario_atualizado == "NA":
                                text(f'Horario de atualização: Não possui esta informação')
                            else:
                                text(f'Horario de atualização: {horario_atualizado}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if local == "NA":
                                text(f'Local: Não possui esta informação')
                            else: 
                                text(f'Local: {local}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in tags:
                                text(f'Tags: Não possui esta informação')
                            else: 
                                text(f'Tags: {", ".join(tags)}')
                    

                



            with tag('footer', klass="aviso"):
                with tag('div', klass='aviso-texto'):
                    text("AVISOS")
                    for paragrafo in paragrafos_avisos:
                        with tag('h5'):
                            text(paragrafo)
            doc.asis(f'<script type="text/javascript" src={REFERENCIAS}></script>')
    # result = indent(doc.getvalue())
    result = doc.getvalue()
    print(f'DIR HTML ANO: {dir_html_ano}')

    with open(f"{dir_html_ano}/{data[-4:]}-{data[3:5]}-{data[:2]}-{horario}-{titulo}.html", "w") as file:
        file.write(result)


def main():
   consulta = consultar(template = "ok")


if __name__ == '__main__':
    main()

    