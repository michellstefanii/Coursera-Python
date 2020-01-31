l = int(input("digite a largura "))
a = int(input("digite a altura "))
cont = 0
cont2 = 0

while cont2 < a:
    if cont2 == 0 or cont2 == (a-1):
        while cont < l:
            print("#", end="")
            cont += 1
    else:
        print("#", end=" ")
        while cont < (l-3):
            print("", end=" ")
            cont += 1
        print("#", end="")
    cont = 0
    print("")
    cont2 += 1