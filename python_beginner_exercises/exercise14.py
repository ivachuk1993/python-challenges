'''14. Escreva um programa Python que leia o valor de dois catetos 
e retorne o valor da hipotenusa, assumindo que seja possível formar um triângulo.

numero1 = float(input("Digite o valor do primeiro cateto: "))
numero2 = float(input("Digite o valor do segundo cateto: "))

hipotenusa = (numero1 ** 2 + numero2 ** 2) ** 0.5

#- fazer assim estaria correto, mas a pergunta pede para que seja validado que é possível 
#formar um triângulo, dessa forma, os catetos precisam ser positivos.
'''

#logo,
numero1 = float(input("Digite o valor do primeiro cateto: "))
numero2 = float(input("Digite o valor do segundo cateto: "))

if numero1 > 0 and numero2 > 0:
    hipotenusa = (numero1 ** 2 + numero2 ** 2) ** 0.5
    print(f"O valor da hipotenusa é: {hipotenusa:.2f}")

else:
    print(f"Os catetos devem ser números positivos para formar um triângulo.")
