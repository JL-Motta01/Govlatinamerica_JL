from yattag import Doc, indent
from tinydb import TinyDB, Query

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.asis('<meta charset="utf-8" />')
        with tag('link', rel="stylesheet", type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css"):
            text('some value1')
        for i in ['a', 'b', 'c']:
            with tag('field2', name='asdfasd'):
                text(i)
    with tag('body'):
        with tag('header'):
            with tag('field1', name='blah'):
                text('some value1')
        with tag('div', klass='container'):
            with tag('article', name='blah'):
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