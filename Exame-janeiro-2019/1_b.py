def f(lista1,lista2):
    return [(lista1[index],lista2[index],lista1[index]+lista2[index]) for index in range(len(lista1))]

print(f([1,3,5],[3,4,5]))