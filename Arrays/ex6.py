# Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável
# composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo
# de entrada.

import random

vetor = []
for i in range(100):
    vetor.append(random.randint(0, 100))

print("O somatório dos valores é:", sum(vetor))