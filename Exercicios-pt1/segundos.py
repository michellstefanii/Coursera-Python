segundos = int(input("Por Favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
dias_rest = segundos % 86400
horas = dias_rest // 3600
segs_rest = segundos % 3600
segs_final = segs_rest % 60
minutos = segs_rest // 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_final,"segundos.")     