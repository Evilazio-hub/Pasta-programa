# Programa para calcular a soma e a média das idades de 10 pessoas
soma = 0
media = 0
num_maior = 0
nome_maior = ""
for i in range(3):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    if idade > num_maior:
        num_maior = idade
        nome_maior = nome
    soma = soma + idade
media = soma / (i + 1)
print(f"A soma das idades é: {soma}")
print(f"A média das idades é: {media}")
print(f"A pessoa mais velha é: {nome_maior}")