# Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na
# ordem contrária em que foi lida.

import random
vetor = []

for i in range(10):
    vetor.append(random.randint(0, 100))

print(vetor)
print(vetor[::-1])
