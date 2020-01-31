l = int(input("digite a largura "))
a = int(input("digite a altura "))
cont = 0

while a != 0:
    while cont < l:
        print("#", end="")
        cont += 1
    cont = 0
    print("")
    a -= 1