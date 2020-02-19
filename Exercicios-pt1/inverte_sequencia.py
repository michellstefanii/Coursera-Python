x = 1
lista = []
while x > 0:
    n = int(input("Digite um número: "))
    if n != 0:
        lista.append(n)
    else:
        x = 0

lista.reverse()

x = 0

while x < len(lista):
    print(lista[x])
    x += 1 