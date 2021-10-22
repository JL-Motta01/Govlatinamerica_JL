from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

with tag('root'):
    with tag('doc'):
        with tag('field1', name='blah'):
            text('some value1')
        for i in ['a', 'b', 'c']:
            with tag('field2', name='asdfasd'):
                text(i)

result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline = '\r\n'
)

print(result)

with open('test.html', "w") as file:
    file.write(result)