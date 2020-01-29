def computador_escolhe_jogada(n, m):
    jg = 0
    i = 0
    while(i < m):
        jg = m - i
        v = n - jg
        if(checa_multiplos(v,m)):
            if jg == 1:
                print("\nO computador tirou uma peça.")
                if v == 1:
                    print("Agora resta apenas uma peça no tabuleiro.\n")
            if v == 0:
                print("\nO computador tirou",jg,"peças.")
                print("Fim do jogo! O computador ganhou!")
            else:
                print("\nO computador tirou",jg,"peças.")
                print("Agora restam",v,"peças no tabuleiro.\n")
            return jg
        i = i + 1
    print("\nO computador tirou",m,"peças.")
    print("Agora restam",m,"peças no tabuleiro.\n")
    if (n - m) == 0:
        print("Fim do jogo! O computador ganhou!")
    return m

def checa_multiplos(n,m):
    if (n % (m + 1) == 0):
        return True
    else:
        return False

def usuario_escolhe_jogada(n, m):
    p = 0
    while p == 0: 
        p = int(input("Quantas peças você vai tirar?: "))
        if p > m:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            p = 0
        elif p <= 0:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            p = 0
    if p == 1:
        print("\nVoce tirou uma peça.")
    elif p != 1:
        print("\nVoce tirou",p,"peças.")
    if (n - p) == 0:
        print("Fim do jogo! Voce ganhou!")
    elif (n - p) == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    elif (n - p) != 1:
        print("Agora restam",(n-p),"peças no tabuleiro.\n")
    return p

def partida():
    n = 0
    m = 0
    while (n <= 0):
        n = int(input("Quantas Peças?: "))
    while (m <= 0):
        m = int(input("Limite de peças por jogada?: "))
    if (n % (m + 1)):
        print("\nComputador Começa!")
        while n != 0:
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                return 1
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                return 2   
    else:
        print("\nVocê Começa!")
        while n != 0:
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                return 2
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                return 1

def campeonato():
    cont = 3
    pc = 0
    user = 0
    while not cont == 0:
        if cont == 3:
            print("\n**** Rodada 1 ****\n")
        elif cont == 2:
            print("\n**** Rodada 2 ****\n")
        elif cont == 1:
            print("\n**** Rodada 3 ****\n")
        pontos = partida()
        if pontos == 1:
            pc += 1
        elif pontos == 2:
            user += 1
        cont -= 1
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Voce",user,"X",pc,"Computador")

def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada!")
    print("2 - para jogar um campeonato")
    escolha = int(input(""))
    if escolha == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()
    elif escolha == 1:
        print("\nVoce escolheu uma partida!")
        partida()
    elif escolha != 1 and escolha != 2:
        inicio()

inicio()