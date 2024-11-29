# Programa para calcular a velocidade média
cm = 12
d = int(input("Informe a distância percorrida (Km) :"))
t = float(input("Informe o tempo de viagem (Horas) :"))
vm = d / t
l = d / cm
print(f"A velocidade média do veículo foi {vm} Km/h.")
print(f"A quantidade gasta de combustível foi {l} litros.")