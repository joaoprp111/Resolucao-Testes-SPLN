#!/usr/bin/env python

from sys import argv 
import re 

def fix_lines(str):
    str = re.sub(r'(\w|\s)\n(\w|\s)',r'\1 \2',str)
    str = re.sub(r'(\w)-\n(\w)',r'\1\2',str)
    str = re.sub(r'(\w)-\n-(\w)',r'\1-\2',str)
    return str

if __name__ == '__main__':
    file = argv[1]
    with open(file,'r') as f:
        content = f.read()
        print(fix_lines(content))
