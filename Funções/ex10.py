# Criar uma função que calcule e retorne o MAIOR entre dois valores recebidos como
# parâmetros. Um programa para testar tal função deve ser criado.

def maior(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
print(f'O maior número entre {x} e {y} é {maior(x, y)}')