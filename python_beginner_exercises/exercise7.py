'''7. Faça um programa que peça ao usuário o preço de um produto
# e exiba o preço com um desconto de 10%.'''

preco = float(input("Qual é o preço do produto? "))

preco_final= preco - (preco * 0.10)

print(f"O preço final com 10% de desconto é: R$ {preco_final:.2f}")
