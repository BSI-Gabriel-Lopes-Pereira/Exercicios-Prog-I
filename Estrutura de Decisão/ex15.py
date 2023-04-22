# Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca,
# Paulista, Mineiro ou Outros”

siglaEstado = input("Digite a sigla do estado: ")

if siglaEstado == "RJ":
    print("Carioca")
elif siglaEstado == "SP":
    print("Paulista")
elif siglaEstado == "MG":
    print("Mineiro")
else:
    print("Outros")
