# Programa com desvio e conectivo
nome = input("Informe o nome: ")
sexo = input("Informe o sexo (M ou F): ")
idade = int(input("Informe a idade: "))
if (idade >= 18) and (sexo == "M" or sexo == "m"):
    certificado = int(input("Informe o certificado de reservista: "))
elif idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")