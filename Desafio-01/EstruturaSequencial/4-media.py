# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

for i in range(4):
    nota = float(input(f"Digite a nota do {i + 1}º bimestre: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média das notas é {media}")
