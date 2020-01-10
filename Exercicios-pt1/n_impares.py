n = int(input("Digite o valor de n: "))

x = 1

while x <= n:
    if x % 2 != 0:
        print(x)
        n = n + 1
    x = x + 1