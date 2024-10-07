'''
1065 - PARES ENTRE CINCO NÚMEROS

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''
i = 1
contador = 0

while(i <= 5):
	valor = abs(int(input()))

	if((valor % 2) == 0):
		contador += 1

	i += 1

print(f'{contador} valores pares')