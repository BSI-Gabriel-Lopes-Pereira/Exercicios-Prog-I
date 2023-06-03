# Repita o algoritmo acima, porém imprima quantos valores estão acima da média.

nota = []

for i in range(10):
    nota.append(float(input("Digite a nota: ")))

media = sum(nota)/len(nota)
print("A média é:", media)

for i in range(len(nota)):
    if nota[i] > media:
        print("A nota", nota[i],"está acima da média.")