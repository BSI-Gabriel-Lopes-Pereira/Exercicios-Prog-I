# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

qtKm = float(input("Quantidade de km percorridos: "))
qtDias = float(input("Quantidade de dias alugado: "))
totalPag = qtKm*0.15 + qtDias*60
print(f"Total a pagar: {totalPag}")