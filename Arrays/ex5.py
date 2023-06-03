# Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se
# existirem, escrever as posições em que estão armazenados.

import random

vetor = []
for i in range(100):
    vetor.append(random.randint(27, 32))

for i in range(len(vetor)):
    if vetor[i] == 30:
        print("O elemento", vetor[i], "está na posição", i)