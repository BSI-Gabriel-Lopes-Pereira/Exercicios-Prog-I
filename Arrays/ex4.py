# Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior
# valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.

nota = []

for i in range(30):
    nota.append(float(input("Digite a nota: ")))

print("A maior nota é:", max(nota))
print("A menor nota é:", min(nota))
print("A média é:", sum(nota)/len(nota))

media = sum(nota)/len(nota)
for i in range(len(nota)):
    if nota[i] < media:
        print("A nota", nota[i], "está abaixo da média.")