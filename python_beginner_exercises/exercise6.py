'''6. Faça um programa que peça ao usuário o raio de um círculo e
 exiba na tela a área e o perímetro desse círculo (considere pi = 3.14).
 Aproxime para 2 casas decimais.'''

raio = float(input("Qual o raio do círculo? "))
pi = 3.14
area = pi * (raio**2)
perímetro = 2 * pi * raio

print(f"O valor da área do círculo é: {area:.2f}")
print(f" O valor do perímetro é: {perímetro:.2f}")