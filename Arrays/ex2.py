# Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável
# composta chamada NOTA e calcule e imprima a sua média.

nota = []

for i in range(10):
    nota.append(float(input("Digite a nota: ")))

print("A média é:", sum(nota)/len(nota))