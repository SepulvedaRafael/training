'''
1080 - MAIOR E POSIÇÃO

Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
valores = []
x = 1

while(x <= 100):
	valor = int(input())
	valores.append(valor)
	x += 1

x = 0
maior = max(valores)

while(x < len(valores)):
	if valores[x] == maior:
		achou = True
		break
	x += 1

print(maior)

if achou:
	print(x + 1)
