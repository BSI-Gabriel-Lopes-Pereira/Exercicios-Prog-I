# Faça uma função que calcule a hipotenusa. Os catetos são os dados de entrada e
# a hipotenusa é o dado de saída.

def hipotenusa(cateto1, cateto2):
    return (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print(hipotenusa(3, 4))