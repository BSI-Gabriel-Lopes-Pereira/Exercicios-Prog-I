# Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o
# ano digitado é válido.

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNascimento

if anoNascimento > anoAtual:
    print("Ano de nascimento inválido")
else:
    print("Idade: ", idade)