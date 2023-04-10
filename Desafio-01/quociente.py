# Elaborar um algoritmo para ler dois números e mostrar o quociente e o resto da
# divisão inteira do primeiro pelo segundo número.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

quociente = num1 // num2
resto = num1 % num2

print("O quociente da divisão é: ", quociente)
print("O resto da divisão é: ", resto)
