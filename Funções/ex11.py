# Crie uma função que realize a conversão de Polegadas (pol) para Centímetros
# (cm), onde pol é passado como parâmetro e cm é retornado. Sabe-se que 1
# polegada tem 2.54 centímetros. Crie também um programa para testar tal função.

def polegadas2cm(pol):
    cm = pol * 2.54
    return cm

pol = float(input('Digite o valor em polegadas: '))
print(f'{pol} polegadas equivalem a {polegadas2cm(pol):.2f} centímetros')