# Dada uma tabela de 4 x 5 elementos, calcular a soma de cada linha e a soma de todos os
# elementos.

import random

matriz = []
for i in range(4):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

soma = 0
for i in range(len(matriz)):
    soma += sum(matriz[i])
    print("A soma dos elementos da linha", i,"é:", sum(matriz[i]))

print("A soma de todos os elementos é:", soma)
