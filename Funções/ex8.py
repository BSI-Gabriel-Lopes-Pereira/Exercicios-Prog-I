# Escreva uma função que receba um número natural e imprima os três primeiros
# caracteres do dia da semana correspondente ao número. Por exemplo, 7
# corresponde a “SAB”. O procedimento deve mostrar uma mensagem de erro caso
# o número recebido não corresponda a um dia da semana. Gere também um
# programa que utilize essa função, chamando-a, mas antes lendo um valor para
# passagem de parâmetro.

def dia(n):
    match n:
        case 1:
            print('DOM')
        case 2:
            print('SEG')
        case 3:
            print('TER')
        case 4:
            print('QUA')
        case 5:
            print('QUI')
        case 6:
            print('SEX')
        case 7:
            print('SAB')
        case _:
            print('Número inválido')

n = int(input('Digite um número inteiro: '))
dia(n)