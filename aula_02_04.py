# Programa Calcular Idade
import datetime # Importa a biblioteca datetime
data_atual = datetime.date.today() # Armazena na variável a data completa
nasc = int(input("Informe o ano de nascimento: "))
ano_atual = data_atual.year # Armazena na variável o ano atual
idade = ano_atual - nasc
print(f"A sua idade é {idade} anos.")