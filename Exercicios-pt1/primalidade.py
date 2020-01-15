n = int(input("Digite um número inteiro: "))

cont = 2

x = True

while (cont < n and x):
    x = not ((n % cont) == 0)
    cont += 1

if (x):
    print("primo")
else:
    print("não primo")