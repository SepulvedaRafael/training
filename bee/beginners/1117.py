'''
1117 - VALIDAÇÃO DE NOTA

Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

+------------------------+----------------------+
|   Exemplo de Entrada   |   Exemplo de Saída   |
+------------------------+----------------------+
|         2  2           |         -1.5         |
|         3 -2			 |	divisao impossivel  |
|        -8 -1			 |          0.0         |
|        -7  1			 |                      |
+------------------------+----------------------+
'''
notas = []

while True:
	nota = float(input())

	if(nota < 0 or nota > 10):
		print('nota invalida')
	else:
		notas.append(nota)

		if(len(notas) == 2):
			media = (notas[0] + notas[1]) / 2
			print(f'media = {media:.2f}')
			break
