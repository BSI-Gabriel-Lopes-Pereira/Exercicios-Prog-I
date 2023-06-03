# Faça um algoritmo que monte uma estrutura de dados homogênea 10 x 30, onde o conteúdo
# de cada elemento é igual à soma dos valores de seus índices.

matriz = []
for i in range(10):
    linha = []
    for j in range(30):
        linha.append(i + j)
    matriz.append(linha)

for i in range(len(matriz)):
    print(matriz[i])
