import unidecode
import re

def count_digits(lista):
    num_digits_list = [len(str(x)) for x in lista]
    return sum(num_digits_list)

def palindrome(frase):
    frase = unidecode.unidecode(frase).lower()
    frase = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@\[\]\\^_`{}|~\s]',r'',frase)
    return frase[::-1] == frase

print(count_digits([1,5,14,28,1000]))
print(palindrome('Olé! Maracujá, caju, caramelo.'))
print(palindrome('Scripting em PLN'))