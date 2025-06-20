'''8. Faça um programa que leia a temperatura em graus Celsius
# e exiba a temperatura em graus Fahrenheit.
# A fórmula para converter de Celsius para Fahrenheit é: F = (9/5)*C + 32.'''

C = float(input("Qual o valor em graus Celsius?"))

F = (9/5)*C + 32

print(f" O valor em Fahrenheit é: {F:.3f} ºF")