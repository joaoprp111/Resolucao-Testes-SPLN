#!/usr/bin/env python

import spacy
import re 
from sys import argv 

if len(argv) > 2:
    entidade_referencia = argv[1]
    texto = open(argv[2],'r',encoding='UTF-8').read()
    num_frase = 1
    entidades = list()
    entidades_texto = re.findall(r'\{(.+?)\}',texto)
    for e in entidades_texto:
        entidades.append(e)

    texto = re.sub(r'\{|\}','',texto)
    nlp = spacy.load('pt_core_news_lg')
    doc = nlp(texto)
    for sent in doc.sents:
        if entidade_referencia in sent.text:
            for token in sent:
                if token.text != entidade_referencia and token.text in entidades:
                    print(f'{token.text} {num_frase}')
        num_frase += 1
else:
    print('Faltam argumentos!')