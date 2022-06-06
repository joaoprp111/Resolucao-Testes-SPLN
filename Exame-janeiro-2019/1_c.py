def count_char_occur(frase):
    occur = dict()
    for index in range(len(frase)):
        if index + 1 < len(frase):
            occur.setdefault(frase[index]+frase[index+1],0)
            occur[frase[index]+frase[index+1]] += 1 

    return occur

print(str(count_char_occur('TESTE DE SPLN')))