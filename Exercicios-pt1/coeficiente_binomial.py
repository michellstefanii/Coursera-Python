a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

def binomial(a, b):
    if a == b:
        z = 1
    elif b == 0:
        z = 1
    elif b == 1:
        z = a
    else:
        return fatorial(a) // (fatorial(b) * fatorial(a-b))

    return z

def fatorial(f):
    x = 1
    i = 2
    while i <= f:
        x = x*i
        i = i + 1
    return x

print(binomial(a, b))

def testa_fatorial():
    if fatorial(1) == 1:
        print("funciona para 1")
    else:
        print("nao funciona para 1")
    if fatorial(2) == 2:
        print("funciona para 2") 
    else:
        print("não funciona para 2")

testa_fatorial()