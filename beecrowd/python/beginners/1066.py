'''
1066 - PARES, ÍMPARES, POSITIVOS E NEGATIVOS

Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''
i = 1
contadorPar = 0
contadorImpar = 0
contadorPlus = 0
contadorMinus = 0

while(i <= 5):
	valor = int(input())

	if((abs(valor) % 2) == 0):
		contadorPar += 1
	else:
		contadorImpar += 1

	if(valor > 0):
		contadorPlus += 1
	elif(valor == 0):
		pass
	else:
		contadorMinus += 1

	i += 1

print(f'{contadorPar} valor(es) par(es)')
print(f'{contadorImpar} valor(es) impar(es)')
print(f'{contadorPlus} valor(es) positivo(s)')
print(f'{contadorMinus} valor(es) negativo(s)')