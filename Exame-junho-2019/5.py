def toXML(tag,attrs,content):
    xml = ''
    tag_text = ''
    content_text = ''

    if len(attrs.keys()) > 0:
        tag_text = '<' + tag
        for k in attrs.keys():
            tag_text += ' ' + k + '="' + attrs[k] + '"'
        tag_text += '>'
    else:
        tag_text = '<' + tag + '>'

    if isinstance(content,str):
        content_text = content 
        xml = tag_text + content_text + '</' + tag + '>' 

    elif isinstance(content,list):
        for elem in content:
            xml += tag_text + elem + '</' + tag + '>\n'

    elif isinstance(content,dict):
        xml = tag_text + '\n'
        for k in content.keys():
            xml += '\t' + '<' + k + '>' + content[k] + '</' + tag + '>\n'
        xml += '</' + tag + '>'

    elif callable(content):
        xml = tag_text + content(tag) + '</' + tag + '>'

    return xml

attrs = {}

tag = 'cafe'

content = lambda x: 'Vou tomar ' + x

print(toXML(tag,attrs,content))