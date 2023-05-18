# Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
# inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
# • o número de inscrição e a altura do atleta mais alto;
# • o número de inscrição e a altura do atleta mais baixo;
# • a altura média do grupo de atletas.

n = int(input('Quantos atletas você quer cadastrar? '))
maior_altura = 0
menor_altura = 0
soma_altura = 0

for i in range(1, n + 1):
    numero = int(input(f'Número de inscrição do atleta {i}: '))
    altura = float(input(f'Altura do atleta {i} (em cm): '))
    if altura > maior_altura:
        maior_altura = altura
        numero_maior = numero
    if altura < menor_altura or i == 1:
        menor_altura = altura
        numero_menor = numero
    soma_altura += altura

media_altura = soma_altura / n

print(f'Número de inscrição do atleta mais alto: {numero_maior}')
print(f'Altura do atleta mais alto: {maior_altura} cm')
print(f'Número de inscrição do atleta mais baixo: {numero_menor}')
print(f'Altura do atleta mais baixo: {menor_altura} cm')
print(f'Altura média dos atletas: {media_altura:.2f} cm')