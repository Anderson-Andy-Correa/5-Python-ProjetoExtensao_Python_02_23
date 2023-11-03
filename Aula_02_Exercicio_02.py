'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
float1 = float(input("Digite o número real: "))

print(f"{int1 * 2} * {int2 / 2} = {(int1 * 2) * int2 / 2}")
print(f"{int1 * 3} + {float1} = {(int1 * 3) + float1}")
print(f"{float1}³ = {float1 ** 3}")