'''
1154 - IDADES

Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           34           |              39.25             |
|           56           |                                |
|           44           |                                |
|           23           |                                |
|           -2           |                                |
+------------------------+--------------------------------+
'''
idades = []
soma = 0

x = True

while x:
	idade = int(input())
	idades.append(idade)

	if(idade < 0):
		idades.pop()
		break

for i in idades:
	soma += i

media = soma / (idades.index(idades[-1]) + 1)
print(f'{media:.2f}')