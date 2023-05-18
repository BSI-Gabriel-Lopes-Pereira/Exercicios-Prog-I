# Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das
# alturas.

soma = 0

for i in range(1, 21):
    altura = float(input(f'Altura da pessoa {i}: '))
    soma += altura

media = soma / 20

print(f'Média das alturas: {media:.2f}')