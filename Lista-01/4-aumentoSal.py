# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do seu salário: "))
aumentoPc = float(input("Valor do aumento em porcentagem: "))
aumento = salario * (1 + aumentoPc/100)
print(f"Salário com aumento: {aumento}")