# Faça um programa para ler o nome do aluno, ler 4 notas, ler faltas e calcular a média e imprimir
#obs: Média => 7 Aprovado, Faltas <= 5 Aprovado
NomeAluno = input("Digite o nome do Aluno: ")
QtdNotas = int(input("Digite a quantidade de notas do aluno: "))
media = 0

for i in range(QtdNotas):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    media += nota

media /= QtdNotas
QtdFaltas = int(input(f"Quantas faltas {NomeAluno} possui nessa matéria?"))
if media < 7 or QtdFaltas > 5:
    situacao = "reprovado"
else:
    situacao = "aprovado"
print(f"A média do alino {NomeAluno} é igual a {media}. Situação: {situacao}")