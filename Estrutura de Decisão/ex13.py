# Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se
# este número é par ou ímpar.

num1 = int(input("Digite um número inteiro: "))
if num1 % 2 == 0:
    print("Par")
else:
    print("Ímpar")