x = 0

while x == 0:
    n = int(input("Digite um número inteiro: "))
    if n < 0:
        x = 1
    else:
        j = 1
        i = 2
        while i <= n:
            j = j*i
            i = i + 1
        print(j)