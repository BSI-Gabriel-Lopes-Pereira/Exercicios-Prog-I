# Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o
# maior valor do conjunto. Um número com valor “0” (zero) indica o fim dos dados e
# não deve ser considerado.

valores = []
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    valores.append(n)
print(f"O maior valor é {max(valores)} e o menor valor é {min(valores)}")