# Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
# caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”.
# Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.

tinta = float(input('Quantidade de tinta da caneta: '))
gastoDeTinta = tinta * 0.02
while tinta > 0:
    print('Enquanto tem tinta a caneta escreve...')
    tinta -= gastoDeTinta
    print(f'Tinta restante: {tinta}')
