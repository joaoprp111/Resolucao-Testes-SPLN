#!/usr/bin/env python

from sys import argv 
import re 

def words_tags(texto):
    tags = re.findall(r'(.+?)\/(.+?)\s', texto)
    last_tag = re.search(r'^.+\s(.+?)\/(.+?)$', texto)
    occurrences = dict()
    tags_occ = dict()

    for word, word_tag in tags:
        occurrences.setdefault(word,0)
        occurrences[word] += 1
        tags_occ.setdefault(word,dict())
        tags_occ[word].setdefault(word_tag,0)
        tags_occ[word][word_tag] += 1

    #Last tag
    word = last_tag.group(1)
    word_tag = last_tag.group(2)
    occurrences.setdefault(word,0)
    occurrences[word] += 1
    tags_occ.setdefault(word,dict())
    tags_occ[word].setdefault(word_tag,0)
    tags_occ[word][word_tag] += 1

    items = sorted(occurrences.items(), key=lambda i: i[1], reverse=True)
    for k,v in items:
        tags = tags_occ[k].keys()
        print(f'{k} ({v}):', end=' ')

        for i,t in enumerate(tags):
            t_count = tags_occ[k].get(t)
            print(f'{t} ({t_count})', end='')
            if i < len(tags)-1:
                print(',',end=' ')
        
        print('\n',end='')

if __name__ == '__main__':
    file = argv[1]
    with open(file,'r',encoding='UTF-8') as f:
        content = f.read()
        words_tags(content)