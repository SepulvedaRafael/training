'''
1179 - PREENCHIMENTO DE VETOR IV

Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           1            |           par[0] = 4           |
|           3            |           par[1] = -4          |
|           4            |           par[2] = 2           |
|          -4            |           par[3] = 8           |
|           2            |           par[4] = 2           |
|           3            |          impar[0] = 1          |
|           8            |          impar[1] = 3          |
|           2            |          impar[2] = 3          |
|           5            |          impar[3] = 5          |
|          -7            |          impar[4] = -7         |
|          54            |          impar[0] = 789        |
|          76            |          impar[1] = 23         |
|          789           |           par[0] = 54          |
|          23            |           par[1] = 76          |
|          98            |           par[2] = 98          |
+------------------------+--------------------------------+
'''
par = []
impar = []

for i in range(15):
	x = int(input())

	if((x % 2) == 0):
		par.append(x)
	else:
		impar.append(x)

	if(len(par) == 5):
		for i in range(5):
			print(f'par[{i}] = {par[i]}')
		par.clear()
	elif(len(impar) == 5):
		for i in range(5):
			print(f'impar[{i}] = {impar[i]}')
		impar.clear()

if(len(impar) != 0):
	for i in range(len(impar)):
		print(f'impar[{i}] = {impar[i]}')
if(len(par) != 0):
	for i in range(len(par)):
		print(f'par[{i}] = {par[i]}')
