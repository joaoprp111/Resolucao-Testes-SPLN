def sum_next_is_10(lista):

    def fun(item):
        index = item[0]
        elem = item[1]
        if index + 1 < len(lista) and elem + lista[index+1] == 10:
            return item

    return [i[1] for i in list(filter(fun,enumerate(lista)))]

print(sum_next_is_10([1,5,7,3,6,4,8,2,10,0,3]))