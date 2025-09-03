'''
HR001  - Solve me First
Complete a função solveMeFirst para calcular a soma de dois inteiros.

Exemplo
a = 7
b = 3

Retorno 10.

Descrição da Função
Completar o solveMeFirst função no editor abaixo.

solveMeFirst tem os seguintes parâmetros:
int a: o primeiro valor
int b: o segundo valor

Retorna
- int: a soma de e

Restrições
1 <= a, b <= 1000

Entrada de Amostra
a = 2
b = 3

Saída
5

Explicação
2 + 3 = 5
'''

def solveMeFirst(a, b):
	return a + b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)