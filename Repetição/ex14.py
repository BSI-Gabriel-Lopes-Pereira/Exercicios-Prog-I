# Uma loja de departamentos oferece para seus clientes um determinado desconto de
# acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra
# seja maior que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que
# leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar.
# Um nome de cliente igual a ULTIMO indica o fim da entrada de dados.

nome = ''
endereco = ''
valor = 0
total = 0

while nome != 'ULTIMO':
    nome = input('Nome do cliente: ')
    if nome == 'ULTIMO':
        break
    endereco = input('Endereço do cliente: ')
    valor = float(input('Valor da compra: '))
    if valor > 500:
        total = valor * 0.8
    else:
        total = valor * 0.85
    print(f'Total a pagar: R$ {total:.2f}')
