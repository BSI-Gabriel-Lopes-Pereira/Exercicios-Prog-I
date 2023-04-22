# Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do
# vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
gols1 = int(input("Digite o número de gols do primeiro time: "))
gols2 = int(input("Digite o número de gols do segundo time: "))

if gols1 > gols2:
    print(time1)
elif gols2 > gols1:
    print(time2)
else:
    print("EMPATE")