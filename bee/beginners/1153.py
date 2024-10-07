'''
1153 - FATORIAL SIMPLSE

Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           4            |               24               |
+------------------------+--------------------------------+
'''
resultado = 1

n = int(input())

if(n > 0 and n < 13):
	for i in range(1, n+1):
		resultado *= i

print(resultado)