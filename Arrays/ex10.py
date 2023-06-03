# Dada uma matriz B, de 10 linhas por 20 colunas, escrever um algoritmo que calcula e imprima
# o somatório dos elementos da quinta linha.

import random

matriz = []
for i in range(10):
    linha = []
    for j in range(20):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

soma = sum(matriz[4])

print("O somatório dos elementos da quinta linha é:", soma)
