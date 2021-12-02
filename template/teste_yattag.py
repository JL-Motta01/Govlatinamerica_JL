from yattag import Doc, indent
from tinydb import TinyDB, Query

doc, tag, text = Doc().tagtext()
links = ["stylesheet"]
doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.asis('<meta charset="utf-8" />')
        for link in links:
            doc.asis(f'<link rel={link} type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css">')
            doc.asis(f'<link rel={link} type="template/reset.css">')
            doc.asis(f'<link rel={link} type="text/css" href="template/style.css">')
            doc.asis(f'<link rel={link} type="text/css" href="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/style.css">')
        doc.asis(f'<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
        doc.asis(f'<meta name="local" content="CONTEUDO">') 
        doc.asis(f'<meta name="titulo" content="CONTEUDO">') 
        doc.asis(f'<meta name="subtitulo" content="CONTEUDO">') 
        doc.asis(f'<meta name="autores" content="CONTEUDO">') 
        doc.asis(f'<meta name="data" content="CONTEUDO">') 
        doc.asis(f'<meta name="atualizado_em" content="CONTEUDO">') 
        doc.asis(f'<meta name="categoria" content="CONTEUDO">') 
        doc.asis(f'<meta name="tags" content="CONTEUDO">') 
        doc.asis(f'<meta name="classificado_como" content="CONTEUDO">') 
        doc.asis(f'<meta name="link" content="CONTEUDO">')
    with tag('body'):
        with tag('div', klass='container'):
            with tag('header', klass="negrito", id="conteudo-principal"):
                with tag('h2'):
                    with tag('span', klass="info-head"):
                        text("Local")
                with tag('h2'):
                    with tag('span', klass="info-head"):
                        text("Classificado como:")
                with tag('h2'):
                    with tag('span', klass="info-head"):
                        text("Data")
                with tag('h2'):
                    with tag('span', klass="info-head"):
                        text("Atualizado em:")
            with tag('article', klass="texto-conteudo" id="conteudo-principal"):
                    text('some value1')
        with tag('footer'):
            with tag('field1', name='blah'):
                text('some value1')


result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline = '\r\n'
)

print(result)

with open('test.html', "w") as file:
    file.write(result)