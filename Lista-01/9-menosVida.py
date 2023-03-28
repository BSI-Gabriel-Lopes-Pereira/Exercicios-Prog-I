# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade
#  de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos
# de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

qtCig = int(input("Quantidade de cigarros por dia: "))
qtAnos = int(input("Quantidade de anos que fumou: "))
menosDias = (qtAnos * 365 * qtCig) / 144
print(f"O fumante perdeu {menosDias:.1f} dia(s) de vida.")