# Fazer um programa para ler a distância, valor do litro da gasolina, consumo do carro e calcular o gasto total

dist = float(input("\033[032mDigite a distancia em \033[033mKm\033[032m do percurso: "))
valorLitro = float(input("\033[032mDigite o valor do litro da gasolina em \033[034mReais\033[32m: "))
consumoCarro = float(input("\033[032mDigite o valor do consumo do carro em \033[035mKm/L\033[32m: "))
print(f"\033[034mO valor total a ser gasto vai ser de R$ \033[031m{(dist * valorLitro / consumoCarro):.2f}\033[34m reais.")