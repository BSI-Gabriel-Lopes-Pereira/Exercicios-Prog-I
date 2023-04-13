# Faça um algoritmo que calcule o volume de uma lata de óleo. 
# Escreva o resultado.
# FÓRMULA: volume = p * raio2 * altura

vol = float(input("Digite o volume da lata: "))
raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))
pi = 3.1415
volume = pi * raio ** 2 * altura
print("O volume da lata é", volume)
