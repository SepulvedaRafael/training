'''
4A - MELANCIA (WATERMELON)

Um dia quente de verão, Pete e seu amigo Billy decidiram comprar uma melancia. Eles escolheram o maior e o mais maduro, na opinião deles. Depois disso, a melancia foi pesada, e as escamas mostraram w quilos. Eles correram para casa, morrendo de sede, e decidiram dividir a baga, no entanto, eles enfrentaram um problema difícil.

Pete e Billy são grandes fãs de números pares, é por isso que eles querem dividir a melancia de tal forma que cada uma das duas partes pesa um número par de quilos, ao mesmo tempo não é obrigatório que as partes sejam iguais. Os meninos estão extremamente cansados e querem começar sua refeição o mais rápido possível, é por isso que você deve ajudá-los e descobrir, se eles podem dividir a melancia da maneira que quiserem. Com certeza, cada um deles deve obter uma parte do peso positivo.

Entrada
A primeira (e única) linha de entrada contém número inteiro w (1 ≤ w ≤ 100— o peso da melancia comprada pelos rapazes.

Saída
Imprimir SIM, se os meninos puderem dividir a melancia em duas partes, cada uma pesando um número par de quilos; e NÃO no caso contrário.

Exemplos
Entrada
8

Saída
SIM

Nota
Por exemplo, os meninos podem dividir a melancia em duas partes de 2 e 6 quilos, respectivamente (outra variante — duas partes de 4 e 4 quilos).

'''
w = int(input())

if(w == 2):
	print('NO')
elif((w % 2) == 0):
	print('YES')
else:
	print('NO')