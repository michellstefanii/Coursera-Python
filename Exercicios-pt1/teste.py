def main():
    '''
    Programa para converter segundos em dias horas minutos e segundos restantes
    '''

    print("Conversão de segundos em dias horas minutos e segundos restantes \n")

    # leia os segundos
    segundos = int(input("Por Favor, entre com o número de segundos que deseja converter: "))

    # calculo de dias
    dias = segundos // 86400
    # calculo de horas
    dias_rest = segundos % 86400
    horas = dias_rest // 3600
    # calculo de segundos
    segs_rest = segundos % 3600
    segs_final = segs_rest % 60
    # calculo de minutos
    minutos = segs_rest // 60
    
    print(dias, "dias, ", horas, "horas, ", minutos, "minutos e ", segs_final, "segundos.")     

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
