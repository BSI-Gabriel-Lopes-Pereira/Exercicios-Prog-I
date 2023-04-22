# Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra
# “Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja
# inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta
# média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário
# deve escrever “Reprovado”.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
else:
    notaExame = float(input("Digite a nota do exame: "))
    mediaFinal = (media + notaExame) / 2
    if mediaFinal >= 5:
        print("Aprovado")
    else:
        print("Reprovado")