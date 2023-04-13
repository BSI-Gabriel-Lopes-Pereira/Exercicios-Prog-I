# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a. comprar apenas latas de 18 litros;
# b. comprar apenas galões de 3,6 litros;

areaPintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litrosNecessarios = areaPintada / 6
latasNecessarias18 = litrosNecessarios / 18
precoTotal18 = latasNecessarias18 * 80
galoesNecessarios36 = litrosNecessarios / 3.6
precoTotal36 = galoesNecessarios36 * 25


print(f"a. Você precisará de {latasNecessarias18} latas de tinta, que custarão R$ {precoTotal18}")
print(f"b. Você precisará de {galoesNecessarios36} galões de tinta, que custarão R$ {precoTotal36}")
