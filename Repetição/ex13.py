# Faça um algoritmo que:
# • leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e
# sexo = 'F' ou sexo = 'f' para feminino);
# • escreva a média da altura das mulheres;
# • escreva a média da altura da turma.

n = int(input('Quantas pessoas você quer cadastrar? '))
soma_altura = 0
soma_altura_mulheres = 0
quantidade_mulheres = 0

for i in range(1, n + 1):
    altura = float(input(f'Altura da pessoa {i} (em cm): '))
    sexo = input(f'Sexo da pessoa {i} (M/F): ')
    soma_altura += altura
    if sexo == 'F' or sexo == 'f':
        soma_altura_mulheres += altura
        quantidade_mulheres += 1

media_altura = soma_altura / n
media_altura_mulheres = soma_altura_mulheres / quantidade_mulheres

print(f'Média da altura das mulheres: {media_altura_mulheres:.2f} cm')
print(f'Média da altura da turma: {media_altura:.2f} cm')