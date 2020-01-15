n = int(input("Digite um número inteiro: "))

i = len(str(n))
j = 0
k = 0
l = False

while i != 0 and n != 0 and not l:
    k = (n % 10)
    n = (n // 10)
    j = (n % 10)
    if (k == j):
        l = True
    else:
        i -= 1
if l:
    print("sim")
else:
    print("não")