# Ler duas matrizes A e B, cada uma com 7 linhas e 1 coluna. Construir uma matriz C de 7 x 2,
# onde a primeira coluna deverá ser formada pelos elementos da matriz A e a segunda coluna
# deverá ser formada pelos elementos da matriz B.

import random

matrizA = []
matrizB = []
matrizC = []

for i in range(7):
    linha = []
    for j in range(1):
        linha.append(random.randint(0, 100))
    matrizA.append(linha)

for i in range(7):
    linha = []
    for j in range(1):
        linha.append(random.randint(0, 100))
    matrizB.append(linha)

for i in range(7):
    linha = []
    for j in range(2):
        if j == 0:
            linha.append(matrizA[i])
        else:
            linha.append(matrizB[i])
    matrizC.append(linha)

for i in range(len(matrizC)):
    print(matrizC[i])