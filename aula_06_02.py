# Programa para tratar erro de entra de dados
nome = input("Informe o nome: ")
while True:
    sexo = input("Informe o sexo (M ou F): ")
    if sexo == "M" or sexo == "F":
        break
    else:
        print("Informe apenas M ou F para o sexo" )
while True:        
    try:
        idade  = int(input("Informe a idade: "))
    except ValueError:
        print("Verifique a idade digitada.") 
    else:
        print(f"Seja bem vindo {nome}")  
        break            
    