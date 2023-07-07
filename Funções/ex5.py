# Escreva um programa para ler o número de lados de um polígono regular e a
# medida do lado (em cm). Faça uma função que receba como parâmetro o número
# de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# • Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu
# perímetro.
# • Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# • Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

def poligono(lados, medida):
    if lados == 3:
        print(f'TRIÂNGULO\nPerímetro: {medida * 3}')
    elif lados == 4:
        print(f'QUADRADO\nÁrea: {medida ** 2}')
    elif lados == 5:
        print('PENTÁGONO')
    else:
        print('Número de lados inválido')

lados = int(input('Digite o número de lados do polígono: '))
medida = float(input('Digite a medida do lado do polígono: '))
poligono(lados, medida)
