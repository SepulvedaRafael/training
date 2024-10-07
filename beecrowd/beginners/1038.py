'''
1038 - LANCHE

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

CÓDIGO    ESPECIFICAÇÃO      PREÇO
1		  Cachorro Quente	 R$4.00
2		  X-Salada			 R$4.50
3		  X-Bacon			 R$5.00
4		  Torrada simples	 R$2.00
5		  Refrigerante		 R$1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''
codigo, qtd = input().split()

codigo = int(codigo)
qtd = int(qtd)

if codigo == 1:
	total = qtd * 4
	print(f"Total: R$ {total:.2f}")
elif codigo == 2:
	total = qtd * 4.5
	print(f"Total: R$ {total:.2f}")
elif codigo == 3:
	total = qtd * 5
	print(f"Total: R$ {total:.2f}")
elif codigo == 4:
	total = qtd * 2
	print(f"Total: R$ {total:.2f}")
elif codigo == 5:
	total = qtd * 1.5
	print(f"Total: R$ {total:.2f}")