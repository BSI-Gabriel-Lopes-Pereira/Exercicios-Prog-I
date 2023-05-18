# Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos
# números ímpares entre 1 e 100.

soma_par = 0
soma_impar = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma_par += i
    else:
        soma_impar += i

print(f'Soma dos números pares: {soma_par}')
print(f'Soma dos números ímpares: {soma_impar}')