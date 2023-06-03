# Faça um algoritmo qualquer que leia uma matriz A de 15 linhas por 25 colunas e imprima o
# seu conteúdo.

import random

matriz = []
for i in range(15):
    linha = []
    for j in range(25):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

for i in range(len(matriz)):
    print(matriz[i])
