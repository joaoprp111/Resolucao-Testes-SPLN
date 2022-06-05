import unidecode 

def is_pangram(frase,alfabeto):
    return all([True if c in unidecode.unidecode(frase).lower() else False for c in alfabeto])

print(is_pangram('Blitz prende ex-vesgo com cheque fajuto.','abcdefghijlmnopqrstuvxz'))
print(is_pangram('Juiz faz com que whisky de malte baixe logo preço de venda.','abcdefghijklmnopqrstuvwxyz'))
print(is_pangram('432109876533312315','0123456789'))
print(is_pangram('UMinho', 'UM Gualtar'))