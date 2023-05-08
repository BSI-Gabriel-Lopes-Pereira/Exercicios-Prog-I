# Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é
# par ou ímpar.

for i in range(15):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")