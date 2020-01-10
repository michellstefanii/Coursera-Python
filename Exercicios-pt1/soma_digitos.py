n = int(input("Digite o valor de n: "))

x = 0
soma = 0

while n > 0:
    x = n % 10
    n = n // 10
    soma = soma + x
print(soma)