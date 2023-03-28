# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o
# total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digitte a quantidade de horas: "))
minutos = int(input("Digitte a quantidade de minutos: "))
segundos = int(input("Digitte a quantidade de segundos: "))
total = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print(f"O total de segundos é: {total}s")