"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""


peso = float(input("Peso do Peixe: "))
pesoExcedido = 0

if peso > 50:
    pesoExcedido = peso - 50

multa = pesoExcedido * 4

if peso <= 50:
    print("Sem multa")
else:
    print(f"O peso de {peso}kg excede o limite estabelecido de 50Kg em {pesoExcedido}kg")
    print(f"Muta de {multa:.2f} reais.")
