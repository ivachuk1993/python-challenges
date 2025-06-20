'''10. Faça um programa que leia o peso e a altura de uma pessoa e 
exiba o índice de massa corporal (IMC) dela. A fórmula para calcular 
o IMC é: IMC = peso/altura², com aproximação em 3 casas decimais.'''

peso = float(input("Digite aqui seu peso: "))
altura = float(input("Digite aqui sua altura: "))

IMC = peso/altura**2

print(f"Seu valor de IMC é: {IMC:.3f}")
