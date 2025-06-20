'''9.Faça um programa que peça ao usuário para digitar 3 números 
inteiros e exiba a média aritmética desses números. Aproxime para 1 casa decimal.'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

media = (numero1 + numero2 + numero3) / 3

print(f"O valor da média é: {media:.1f}")