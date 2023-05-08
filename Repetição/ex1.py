# Faça um algoritmo que:
# • leia 20 números inteiros;
# • escreva os números que são negativos;
# • escreva a média dos números positivos.

soma = 0
cont = 0
for i in range(20):
    n = int(input("Digite um número: "))
    if n < 0:
        print(n)
    else:
        soma += n
        cont += 1

print(f"A média dos números positivos é {soma/cont}")