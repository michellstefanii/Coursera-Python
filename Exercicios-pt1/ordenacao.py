def main():

    x = int(input("Digite o 1º número inteiro: "))
    y = int(input("Digite o 2º número inteiro: "))
    z = int(input("Digite o 3º número inteiro: "))

    if x < y < z:
        print("crescente")
    else:
        print("não está em ordem crescente")

main()