from yattag import Doc, indent
from tinydb import TinyDB, Query

def consultar():
    db = TinyDB('/home/lantri_rafael/codigo/govlatinamerica/template/db_artigo.json')
    myDBQuery = Query()
    for dado in iter(db):
        origem = dado['origem']
        classificado = dado['classificado']
        data = dado['data']
       #TODO horario =  
        atualizado_em = dado['atualizado em'] 
        titulo = dado['titulo']
        subtitulo = dado['subtitulo']
        autor = dado['autor']
        link = dado['link']
        tags = dado['tags']
        conteudo = dado['conteudo']
        #TODO dir_local = 
        print(data)
        template_html(origem,classificado,data,atualizado_em,titulo,subtitulo, autor, link,tags,conteudo)
        
        print("#################")
        print("#################")

def template_html(origem="NA",classificado="NA",data="NA",atualizado_em="NA",titulo="NA",subtitulo="NA", autor="NA", link="NA",tags="NA",conteudo="NA"):
    doc, tag, text = Doc().tagtext()
    links = ["stylesheet"]
    infos=['subtitulo', 'autores']
    paragrafos = "NA"
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8" />')
            for l in links:
                doc.asis(f'<link rel={l} type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css">')
                doc.asis(f'<link rel={l} type="template/reset.css">')
                doc.asis(f'<link rel={l} type="text/css" href="template/style.css">')
                doc.asis(f'<link rel={l} type="text/css" href="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/style.css">')
            doc.asis(f'<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
            doc.asis(f'<meta name="origem" content="{origem}">') 
            doc.asis(f'<meta name="titulo" content={titulo}>') 
            doc.asis(f'<meta name="subtitulo" content="CONTEUDO">') 
            doc.asis(f'<meta name="autores" content="CONTEUDO">') 
            doc.asis(f'<meta name="data" content="{data}">') 
            doc.asis(f'<meta name="atualizado_em" content="{atualizado_em}">') 
            doc.asis(f'<meta name="classificado" content="{classificado}">') 
            doc.asis(f'<meta name="tags" content="{tags}">')  
            doc.asis(f'<meta name="link" content="CONTEUDO">')
        with tag('body'):
            with tag('div', klass='container'):
                with tag('header', klass="negrito", id="conteudo-principal"):
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Origem: {origem.title()}')
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Classificado como : {classificado}')
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Data: {data}')
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Atualizado em: {atualizado_em}')
        
                with tag('article', klass="texto-conteudo", id="conteudo-principal"):
                    with tag('div', klass='head-noticia'):
                        with tag('h1'):
                            text(titulo)
                        with tag('p'):
                             text(subtitulo)
                        with tag('p'):
                             text(autor)
                                
                    with tag('div', klass='corpo-noticia'):
                        for paragrafo in conteudo:
                            with tag('p'):
                                text(paragrafo)
                with tag('div', klass='referencia'):
                    with tag('h2'):
                        text("Como citar")



            with tag('footer', klass="aviso"):
                with tag('div', klass='aviso-texto'):
                    text("AVISOS")
                with tag('field1', name='blah'):
                    text('some value1')


    result = indent(
        doc.getvalue(),
        indentation = ' '*4,
        newline = '\r\n'
    )


    with open(f"/home/lantri_rafael/codigo/govlatinamerica/template/html/{titulo}.html", "w") as file:
        file.write(result)
    


def main():
    consulta = consultar()


if __name__ == '__main__':
    main()