# Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1-feminino 2-masculino) de uma pessoa. Depois faça uma função chamada
# pesoideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu
# peso ideal, utilizando as seguintes fórmulas:
# • para homens: (72.7 * h) – 58
# • para mulheres: (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).

def pesoideal(altura, sexo):
    if sexo == 1:
        peso = (62.1 * altura) - 44.7
        return peso
    elif sexo == 2:
        peso = (72.7 * altura) - 58
        return peso
    else:
        print('Sexo inválido')

altura = float(input('Digite sua altura: '))
sexo = int(input('Digite seu sexo (1-feminino 2-masculino): '))
peso = pesoideal(altura, sexo)
print(f'Seu peso ideal é {peso:.2f}kg')