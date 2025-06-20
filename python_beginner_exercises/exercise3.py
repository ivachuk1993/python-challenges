'''3. Faça um programa que leia algo digitado pelo usuário,
# mostre seu tipo e tudo a respeito dele (dica: utiliza as funções is).'''

dado = input("Digite algo aqui: ")


print(f"O tipo primitivo desse valor é {type(dado)}")
print(f"Só tem espaços? {dado.isspace()}")
print(f"É um número? {dado.isnumeric()}")
print(f"É alfabético? {dado.isalpha()}")
print(f"É um alfanumérico? {dado.isalnum()}")
print(f"Está em maiúsculas? {dado.isupper()}")
print(f"Está em minúsculas? {dado.islower()}")
print(f"Está capitalizado? (Primeira letra maiúscula) {dado.istitle()}")