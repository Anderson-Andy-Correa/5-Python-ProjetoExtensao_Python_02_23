"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes"""

clientes = {}

verificador = 1
cont = 0
maisAlto = {"", 0, 0}
maisBaixo = {"", 0, 0}
maisGordo = {"", 0, 0}
maisMagro = {"", 0, 0}
mediaAlturas = 0
mediaPeso = 0

while verificador != "0":
    clientes[cont] = [input("Nome: "), float(input("Peso: ")), float(input("Altura: "))]
    mediaPeso += clientes[cont][1]
    mediaAlturas += clientes[cont][2]

    if cont < 1:
        maisAlto = maisBaixo = maisGordo = maisMagro = clientes[cont]
    else:
        if clientes[cont][2] > maisAlto[2]:
            maisAlto = clientes[cont]
        if clientes[cont][2] < maisBaixo[2]:
            maisBaixo = clientes[cont]
        if clientes[cont][1] > maisGordo[1]:
            maisGordo = clientes[cont]
        if clientes[cont][1] < maisMagro[1]:
            maisMagro = clientes[cont]
    cont += 1

    verificador = input("Continuar inserindo? (Digite 0 para parar) ")

mediaPeso /= (cont)
mediaAlturas /= (cont)
print("---------")
print(f"Clientes")
print("---------")
for c in clientes:
    print(f"Nome: {clientes[c][0]}, Peso: {clientes[c][1]:.2f}kg, Altura: {clientes[c][2]:.2f}")

print("---------")
print(f"Mais alto  - Nome: {maisAlto[0]}, Peso: {maisAlto[1]:.2f}kg, Altura: {maisAlto[2]:.2f}")
print(f"Mais baixo - Nome: {maisBaixo[0]}, Peso: {maisBaixo[1]:.2f}kg, Altura: {maisBaixo[2]:.2f}")
print(f"Mais gordo - Nome: {maisGordo[0]}, Peso: {maisGordo[1]:.2f}kg, Altura: {maisGordo[2]:.2f}")
print(f"Mais magro - Nome: {maisMagro[0]}, Peso: {maisMagro[1]:.2f}kg, Altura: {maisMagro[2]:.2f}")
print(f"Media Peso: {mediaPeso:.2f}kg")
print(f"Media Altura: {mediaAlturas:.2f}m")
