# Programa para tratar erro de divisão 
while True:
    try:
        n1 = int(input("Informe o primeiro valor: "))
        n2 = int(input("Informe o segundo valor: "))
        divisão = n1 /n2
    except ZeroDivisionError: 
        print("Verique o segundo valor digitado, pois ele não pode ser zero")
    else:
        print(f"O resultado da divisão é {divisão})")  
        break
