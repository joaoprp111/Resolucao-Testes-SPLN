def max_diff(lista):
    min_elem = min(lista)
    max_elem = max(lista)

    return max_elem - min_elem

def count_char_occur(sentence):
    occurrences = dict()

    for c in sentence:
        occurrences.setdefault(c,0)
        occurrences[c] += 1

    return occurrences

if __name__ == "__main__":
    r = count_char_occur('Teste de SPLN!!!')
    print(r)