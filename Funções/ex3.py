# Escreva um programa para ler as notas das duas avaliações de um aluno no
# semestre. Faça uma função que receba as duas notas por parâmetro e calcule e
# escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!”
# somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print(f'PARABÉNS! Você foi aprovado! Sua média foi {media:.2f}')
    else:
        print(f'Sua média foi {media:.2f}')
    
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media(nota1, nota2)