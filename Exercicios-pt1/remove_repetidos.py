
def remove_repetidos(lista):
    x = 0
    repet = 0
    while x < len(lista):
        i = 0
        while i < len(lista):
            if lista[x] == lista[i]:
                repet += 1
                if repet > 1:
                    lista.remove(lista[x])
            i += 1
        x = x - repet + 1
        repet = 0
        x += 1
    lista.sort()
    return lista