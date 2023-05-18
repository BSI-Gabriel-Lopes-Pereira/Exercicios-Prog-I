# Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são
# negativos.

n = int(input('Quantos valores você quer ler? '))
negativos = 0

for i in range(1, n + 1):
    valor = int(input(f'Valor {i}: '))
    if valor < 0:
        negativos += 1

print(f'Quantidade de valores negativos: {negativos}')