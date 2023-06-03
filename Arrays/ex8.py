# Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos do
# teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do
# segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10
# elementos. Imprimir os três vetores conforme layout de impressão abaixo:

import random

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor1.append(random.randint(0, 100))
    vetor2.append(random.randint(0, 100))
    vetor3.append(vetor1[i] + vetor2[i])

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor 3:", vetor3)