'''
486A - FUNÇÃO DE CÁLCULO (CALCULATING FUNCTION)

Para um número inteiro positivo n vamos definir uma função f:

f(n) = - 1 + 2 - 3 + .. + ( - 1)^n n

Sua tarefa é calcular f(n) para um dado inteiro n.

Entrada
A linha única contém o inteiro positivo n (1 ≤ n ≤ 1015).

Saída
Imprimir f(n) em uma única linha.

Exemplos
Entrada
4

Saída
2

-------------

Entrada
5

Saída
-3


Nota
f(4) = - 1 + 2 - 3 + 4 = 2

f(5) = - 1 + 2 - 3 + 4 - 5 = - 3

'''
def funcaoN(num):
	if(num % 2 == 0):
		return num * 0.5
	else:
		ant = (n-1) * 0.5
		return ant - num

n = int(input())
print(f'{funcaoN(n):.0f}')