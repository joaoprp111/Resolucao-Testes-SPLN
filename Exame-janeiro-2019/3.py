#!/usr/bin/env python

import re 
from sys import argv 

xml_file_1 = argv[1]
xml_file_2 = argv[2]

xml1 = open(xml_file_1,'r',encoding='UTF-8').read()
xml2 = open(xml_file_2,'r',encoding='UTF-8').read()

dict_linguas = dict()

tus = re.findall(r'<tu>\n\s+(<seg xml:lang="\w\w">.+?</seg>)\n\s+(<seg xml:lang="\w\w">.+?</seg>)\n\s*</tu>', xml1)
for l1, l2 in tus:
    dict_linguas[l2] = l1 
c = 0
xml3 = ''
for k,v in dict_linguas.items():
    if c == 0:
        xml3 = re.sub(k,v,xml2)
    else:
        xml3 = re.sub(k,v,xml3)
    c += 1

print(xml3)