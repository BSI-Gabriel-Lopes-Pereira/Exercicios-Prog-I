# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a
# pagar.

prod = float(input("Digite o valor da mercadoria: "))
descPc = float(input("Valor do desconto em porcentagem: "))
desc = prod * (1 - descPc/100)
print(f"Valor do produto com desconto: {desc}")
