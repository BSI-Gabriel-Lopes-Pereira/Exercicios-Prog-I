# Fazer um algoritmo que:
# a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
# b) intercale os elementos desses dois conjuntos formando uma nova variável composta
# unidimensional de 50 elementos;
# c) Escreva o resultado obtido.

import random

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(25):
    vetor1.append(random.randint(0, 100))
    vetor2.append(random.randint(0, 100))

for i in range(25):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor 3:", vetor3)