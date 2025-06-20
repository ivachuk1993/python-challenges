'''4.Faça um programa que receba os seguintes dados de um funcionário:
# nome, idade e salario. Na empresa que esse funcionário trabalha,
# seu salário é aumentado de ano em ano em R$ 800,90.'''

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
salario = float(input("Qual é o seu salário? "))

#Aumento_anual_fixo
aumento = 800.90
#Salário_atualizado_com_aumento
salario_atualizado = salario + aumento

print(f"O funcionário {nome}, com {idade} anos, teve um aumento salarial para {salario_atualizado:.2f}")

