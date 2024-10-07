'''
1149 - SOMANDO INTEIROS CONSECUTIVOS

Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|          3 2           |               7                |
+------------------------+--------------------------------+
+------------------------+--------------------------------+
|      3 -1 0 -2 2       |               7                |
+------------------------+--------------------------------+
'''
soma = 0

valores = list(map(int, input().split(" ")))
a = valores[0]
n = valores[len(valores) - 1]

for i in range(0, n):
	soma += (a + i)

print(soma)