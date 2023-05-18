# Faça um algoritmo que leia n números inteiros e escreva, para cada número lido, os
# divisores e quantidade de divisores.
# EXEMPLO: número lido = 12
# divisores = 1, 2, 3, 4, 6, 12

# quantidade divisores = 6

n = int(input('Quantos números você quer ler? '))
for i in range(1, n + 1):
    numero = int(input(f'Número {i}: '))
    divisores = []
    for j in range(1, numero + 1):
        if numero % j == 0:
            divisores.append(j)
    print(f'Divisores de {numero}: {divisores}')
    print(f'Quantidade de divisores: {len(divisores)}')