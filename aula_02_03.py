# Programa prestação em atraso
prestacao = float(input("informe o valor da prestacao: "))
taxa = float(input("informe a taxa mensal: "))
tempo = float(input("informe a quantidade de meses em atraso: " ))
valor_final = prestacao+(prestacao*(taxa/100)*tempo)
print(f"o valor final da prestacao é R$ {valor_final:.2f}") 
