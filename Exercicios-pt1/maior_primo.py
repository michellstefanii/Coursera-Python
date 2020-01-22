def ePrimo(k):
    primos = []
    for i in range(k):
        c = 0
        for j in range(k):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)
    return(max(primos))

def maior_primo(y):
    cont = 2
    x = True
    while (cont < y and x):
        x = not ((y % cont) == 0)
        cont += 1
    if (x):
        return y
    else:
        return ePrimo(y)