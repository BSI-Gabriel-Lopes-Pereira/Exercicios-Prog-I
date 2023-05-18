# Construir um algoritmo que calcule o fatorial de um número N.

n = int(input('Digite um número: '))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f'{n}! = {fatorial}')