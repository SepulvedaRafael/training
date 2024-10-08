'''
1164 - NÚMERO PERFEITO

Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”, de acordo com a especificação fornecida.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           3            |         6 eh perfeito          |
|           6            |       5 nao eh perfeito        |
|           5            |        28 eh perfeito          |
|          28            |                                |
+------------------------+--------------------------------+
'''
n = int(input())

for i in range(n):
	x = int(input())

	soma = 0
	for j in range(x-1, 0, -1):
		if((x % j) == 0):
			soma += j

	if(x == soma):
		print(f'{x} eh perfeito')
	else:
		print(f'{x} nao eh perfeito')
