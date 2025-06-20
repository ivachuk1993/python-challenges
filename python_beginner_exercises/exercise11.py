'''11.Faça um programa que leia dois números inteiros 
do usuário e troque seus valores, ou seja, se o primeiro número for 5 
e o segundo número for 7, o programa deve fazer com que o primeiro número 
seja igual a 7 e o segundo número seja igual a 5.'''

num1 = int(input("Digite um primeiro número: "))
num2 = int(input("Digite um segundo número: "))

num1, num2 = num2, num1

print(f"Após a troca: num1 = {num1}, num2 = {num2}")