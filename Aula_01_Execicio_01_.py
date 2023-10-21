# Faça um programa para ler o nome do aluno, ler 4 notas e calcular a média e imprimir

NomeAluno = input("Digite o nome do Aluno: ")
QtdNotas = int(input("Digite a quantidade de notas do aluno: "))
media = 0

for i in range(QtdNotas):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    media += nota

media /= QtdNotas
print(f"A média do alino {NomeAluno} é igual a {media}")