'''13. Escreva um programa Python que leia um número e retorne seu quadrado,
 sua raíz quadrada e sua raíz cúbica, com aproximação em 2 casas decimais.'''

numero = float(input("Digite um número: "))

quadrado = numero ** 2
raiz_quadrada = numero ** 0.5
raiz_cubica = numero ** (1/3)

print(f"O valor do quadrado é: {quadrado:.2f} ")
print(f"O valor da raíz quadrada é: {raiz_quadrada:.2f}")
print(f"O valor da raíz cúbica é: {raiz_cubica:.2f}")