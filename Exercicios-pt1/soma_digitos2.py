n = int(input("Digite um número inteiro: "))

i = len(str(n))

j = 10

k = 0

while i != 0:
    k += (n % j)
    n = n // j
    i -= 1
print(k)