# Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:
# 1+ 2 + 3 + 4 + ... +100

soma = 0

for i in range(1, 101):
    soma += i

print(f'Soma da série: {soma}')