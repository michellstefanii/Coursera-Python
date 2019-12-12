def main():

    import math

    a = int(input("Insira o valor de a: "))
    b = int(input("Insira o valor de b: "))
    c = int(input("Insira o valor de c: "))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("esta equação não possui raízes reais")
    elif delta == 0:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        print("a raiz desta equação é",r1)
    else:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)
        if r1 > r2:
            print("as raízes da equação são",r2,"e",r1)
        else: print("as raízes da equação são",r1,"e",r2)

main()