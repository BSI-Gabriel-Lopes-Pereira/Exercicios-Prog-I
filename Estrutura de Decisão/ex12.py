# Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores
# e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem
# salário total maior.

qtAulas1 = int(input("Digite a quantidade de aulas do professor 1: "))
valHora1 = float(input("Digite o valor da hora do professor 1: "))

qtAulas2 = int(input("Digite a quantidade de aulas do professor 2: "))
valHora2 = float(input("Digite o valor da hora do professor 2: "))

salario1 = qtAulas1 * valHora1
salario2 = qtAulas2 * valHora2

if salario1 > salario2:
    print("O professor 1 tem o salário total maior.")
elif salario2 > salario1:
    print("O professor 2 tem o salário total maior.")
else:
    print("Os professores tem o mesmo salário total.")