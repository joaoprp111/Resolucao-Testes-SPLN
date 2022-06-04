from sys import argv
import spacy

def fix_sent(sent):
    return sent.replace(sent[0],sent[0].upper(),1)

def fix_sent_start(tmin):
    nlp = spacy.load('en_core_web_md')
    doc = nlp(tmin)
    sents = doc.sents
    fixed_sents = [fix_sent(s.text) for s in sents]
    fixed_text = ' '.join(fixed_sents)

    return fixed_text

if __name__ == '__main__':
    file = argv[1]
    with open(file,'r',encoding='UTF-8') as f:
        content = f.read()
        r = fix_sent_start(content)
        output = open('output_3.txt','w',encoding='UTF-8')
        output.write(r)