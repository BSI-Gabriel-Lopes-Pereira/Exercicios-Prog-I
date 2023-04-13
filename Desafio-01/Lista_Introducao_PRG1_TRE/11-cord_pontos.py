# Faça um algoritmo que leia as coordenadas de dois pontos, P1 (x1, y1) e P2 (x2, y2)
# respectivamente, e calcule e escreva a distância entre eles.

import math

x1 = float(input("Digite a coordenada x do ponto 1: "))
y1 = float(input("Digite a coordenada y do ponto 1: "))
x2 = float(input("Digite a coordenada x do ponto 2: "))
y2 = float(input("Digite a coordenada y do ponto 2: "))
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"A distância entre os pontos é {distancia:.2f}")
