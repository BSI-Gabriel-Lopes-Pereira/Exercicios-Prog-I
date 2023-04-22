# Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor
# da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o
# valor do produto e imprimir o valor da venda.

valProduto = float(input("Digite o valor do produto: "))
if valProduto < 20:
    valVenda = valProduto * 1.45
else:
    valVenda = valProduto * 1.30

print(f"O valor da venda foi de: R$ {valVenda:.2f}")