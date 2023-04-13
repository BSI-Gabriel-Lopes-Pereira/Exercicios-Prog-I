# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))
print(f"a. {2 * num1 * (num2 / 2)}")
print(f"b. {3 * num1 + num3}")
print(f"c. {num3 ** 3}")
