def maior_elemento(lista):
    x = 0
    j = lista[x]
    while x < len(lista):
        if j <= lista[x]:
            j = lista[x]
        x += 1
    return j

print(maior_elemento([6,2,3]))