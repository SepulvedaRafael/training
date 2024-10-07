'''
977A - SUBTRAÇÃO ERRADA (WRONG SUBTRACTION)

Menina Tanya está aprendendo a diminuir um número por um, mas ela faz isso errado com um número que consiste em dois ou mais dígitos. Tanya subtrai um de um número pelo seguinte algoritmo:

se o último dígito do número for diferente de zero, ela diminui o número em um;
se o último dígito do número for zero, ela divide o número por 10 (ou seja, remove o último dígito).
Você recebe um número inteiro n
. Tanya subtrairá um dele k
tempos. Sua tarefa é imprimir o resultado, afinal k
subtrações.

É garantido que o resultado será um número inteiro positivo.

Entrada
A primeira linha da entrada contém dois números inteiros n
e k
(2≤n≤109
 1≤k≤50
— O número do qual Tanya subtrairá e o número de subtrações correspondentemente.

Saída
Imprimir um número inteiro — o resultado da diminuição n
por um k
tempos.

É garantido que o resultado será um número inteiro positivo.

Exemplos
Entrada
512 4

Saída
50

-------------
Entrada
1000000000 9

Saída
1

Nota
O primeiro exemplo corresponde à seguinte sequência: 512→511→510→51→50
'''
x = 0

n, k = input().split()

k = int(k)

while(x < k):
	n = str(n)

	if('.' in n):
		while True:
			n = list(n)
			j = n[-1]
			if(n[-1] != '.'):
				n.pop()
			else:
				n.pop()
				msg = ""
				for i in n:
					msg += i
				n = msg
				break

	if(int(n[len(n)-1]) != 0):
		n = int(n)
		n -= 1
	else:
		n = float(n)
		n = n // 10

	x += 1

print(f'{n:.0f}')