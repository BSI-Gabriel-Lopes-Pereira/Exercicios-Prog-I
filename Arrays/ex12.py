# Escreva um algoritmo que leia duas matrizes reais de dimensão 3 x 5, calcule e imprima a sua
# soma.

import random

matriz1 = []
matriz2 = []
matriz3 = []

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 100))
    matriz1.append(linha)

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 100))
    matriz2.append(linha)

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(linha)

for i in range(len(matriz3)):
    print(matriz3[i])
