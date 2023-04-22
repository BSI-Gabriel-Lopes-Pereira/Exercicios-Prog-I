# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a
# pessoa nasceu).

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNascimento

if anoNascimento > anoAtual:
    print("Ano de nascimento inválido")
else:
    if idade >= 16:
        print("Pode votar")
    else:
        print("Não pode votar")