# Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:
# S = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/100

soma = 0

for i in range(1, 101):
    soma += 1/i

print(f'Soma da série: {soma:.2f}')