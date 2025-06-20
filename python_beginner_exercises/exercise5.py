'''5. Faça um programa que peça ao usuário para digitar dois números
# e mostre na tela o resultado da soma, subtração, multiplicação,
# divisão e resto da divisão desses números.'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtração = numero1 - numero2
multiplicação = numero1 * numero2
divisão = numero1 / numero2
resto = numero1%numero2

print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
print(f"Multiplicação: {multiplicação}")
print(f"Divisão: {divisão}")
print(f"Resto: {resto}")
