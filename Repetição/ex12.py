# Uma turma tem 50 alunos. Faça um algoritmo que:
# • leia para cada aluno o seu nome e idade;
# • escreva os nomes dos alunos que tem 18 anos;
# • escreva a quantidade de alunos que tem idade acima de 20 anos.

alunos18 = []
alunos20 = []

for i in range(1, 51):
    nome = input(f'Nome do aluno {i}: ')
    idade = int(input(f'Idade do aluno {i}: '))
    if idade == 18:
        alunos18.append(nome)
    if idade > 20:
        alunos20.append(nome)

print(f'Alunos com 18 anos: {alunos18}')
print(f'Quantidade de alunos com mais de 20 anos: {len(alunos20)}')