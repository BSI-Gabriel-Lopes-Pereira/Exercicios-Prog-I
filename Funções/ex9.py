# Escreva uma função que receba dois números inteiros x e y. Essa função deve
# verificar se x é divisível por y. No caso positivo, a função deve retornar 1, caso
# contrário zero. Escreva também um programa para testar tal função.

def divisivel(x, y):
    if x % y == 0:
        return 1
    else:
        return 0

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if divisivel(x, y) == 1:
    print(f'{x} é divisível por {y}')
else:
    print(f'{x} não é divisível por {y}')
