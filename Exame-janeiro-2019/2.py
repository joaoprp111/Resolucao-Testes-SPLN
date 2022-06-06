#!/usr/bin/env python
from sys import argv 
import re 

inp_f = argv[1]
dic_metrics = {
    'yards': 'metros',
    'yard': 'metro',
    'inch': 'cm',
    'inches': 'cms',
    'foot': 'cm',
    'foots': 'cms',
    'mile': 'km',
    'miles': 'kms'
}

with open(inp_f, 'r', encoding='UTF-8') as f:
    latex = f.read()

    yards = re.findall(r'(\s(\d+)\s(yards?))', latex)
    for m, value, metric in yards:
        regexp = re.compile(m)
        latex = re.sub(regexp, m + '--footnote{' + str(0.91 * int(value)) + ' ' + dic_metrics[metric] + '}',latex)

    inches = re.findall(r'(\s(\d+)\s(inch(?:es)?))', latex)
    for m, value, metric in inches:
        regexp = re.compile(m)
        latex = re.sub(regexp, m + '--footnote{' + str(2.54 * int(value)) + ' ' + dic_metrics[metric] + '}',latex)

    foots = re.findall(r'(\s(\d+)\s(foots?))', latex)
    for m, value, metric in foots:
        regexp = re.compile(m)
        latex = re.sub(regexp, m + '--footnote{' + str(30.5 * int(value)) + ' ' + dic_metrics[metric] + '}',latex)

    miles = re.findall(r'(\s(\d+)\s(miles?))', latex)
    for m, value, metric in miles:
        regexp = re.compile(m)
        latex = re.sub(regexp, m + '--footnote{' + str(1.61 * int(value)) + ' ' + dic_metrics[metric] + '}',latex)

    print(latex)