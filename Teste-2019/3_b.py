import spacy
from sys import argv

'''
O dicionário retornado contém todas as palavras maiúsculas e minúsculas do texto grande
Nas maiúsculas a chave de acesso é essa palavra mas em minúscula
Desta forma, quando for percorrido o texto das palavras minúsculas, pode ser encontrada a correspondente palavra maiúscula na estrutura,
utilizando para tal a chave de acesso para fazer a substituição'''

def lower_and_upper_words(tgrande):
    occurrences = dict()
    occurrences.setdefault('upper',dict())
    occurrences.setdefault('lower',list())

    nlp = spacy.load('en_core_web_md')
    doc = nlp(tgrande)
    for token in doc:
        if not token.text.islower() and token.text not in ['[',']',',',';',':','(',')','?','!','.','/','|']:
            occurrences['upper'].setdefault(token.text.lower(), None)
            occurrences['upper'][token.text.lower()] = token.text
        else:
            occurrences['lower'].append(token.text)

    return occurrences

if __name__ == '__main__':
    file = argv[1]
    with open(file,'r',encoding='UTF-8') as f:
        content = f.read()
        r = lower_and_upper_words(content)
        output = open('output_3_b.txt','w',encoding='UTF-8')
        output.write(str(r))