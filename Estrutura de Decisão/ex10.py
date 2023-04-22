# Ler as notas da 1a e 2a avaliações de um aluno. Calcular a média aritmética simples e
# escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a
# nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média
# calculada.

avaliacao1 = float(input("Digite a nota da primeira avaliação: "))
avaliacao2 = float(input("Digite a nota da segunda avaliação: "))
media = (avaliacao1 + avaliacao2) / 2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")