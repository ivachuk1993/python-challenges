'''1. Faça um programa que realize a soma e subtração de duas variáveis,
 sendo uma do tipo inteiro e outra do tipo decimal, exibindo o valor da
 soma e da subtração no seguinte formato: "O valor da soma é: <soma>"
& "O valor da subtração é: <subtracao>".'''

inteiro = int(input("Digite um número inteiro: "))
decimal = float(input("Digite um número decimal: "))

#Calculo
soma = inteiro + decimal
subtracao = inteiro - decimal
print(f"O valor da soma é: {soma}")
print(f"O valor da subtração é {subtracao}")