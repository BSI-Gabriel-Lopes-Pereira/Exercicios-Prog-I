# Escreva uma função que receba um número inteiro e imprima o mês
# correspondente ao número. Por exemplo, 2 corresponde a “fevereiro”. O
# procedimento deve mostrar uma mensagem de erro caso o número recebido não
# faça sentido. Gere também um programa que leia um valor e chame a função
# criada.

def mes(n):
    match n:
       case 1:
           print('Janeiro')
       case 2:
           print('Fevereiro')
       case 3:
           print('Março')
       case 4:
           print('Abril')
       case 5:
           print('Maio')
       case 6:
           print('Junho')
       case 7:
           print('Julho')
       case 8:
           print('Agosto')
       case 9:
           print('Setembro')
       case 10:
           print('Outubro')
       case 11:
           print('Novembro')
       case 12:
           print('Dezembro')
       case _:
           print('Número inválido')

n = int(input('Digite um número inteiro: '))
mes(n)