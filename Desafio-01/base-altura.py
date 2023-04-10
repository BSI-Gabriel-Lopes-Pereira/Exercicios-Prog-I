# Fazer um algoritmo para ler os valores da base e altura de um retângulo e mostrar
# seu perímetro ( 2 x ( base + altura ) ) e sua área ( base x altura ).

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
perimetro = 2 * (base + altura)
area = base * altura
print("O perímetro do retângulo é: ", perimetro)
print("A área do retângulo é: ", area)
