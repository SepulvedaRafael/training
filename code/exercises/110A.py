'''
110A - NÚMERO QUASE DA SORTE (NEARLY LUCKY NUMBER)

Petya adora números da sorte. Todos nós sabemos que números da sorte são os inteiros positivos cujas representações decimais contêm apenas os dígitos da sorte 4 e 7 . Por exemplo, os números 47 , 744 , 4 são da sorte e 5 , 17 , 467 não são.

Infelizmente, nem todos os números são da sorte. Petya chama um número de quase da sorte se o número de dígitos da sorte nele for um número da sorte. Ele se pergunta se o número n é um número quase da sorte.

Entrada
A única linha contém um inteiro n ( 1 ≤  n  ≤ 10 18 ).

Por favor, não use o especificador %lld para ler ou escrever números de 64 bits em С++. É preferível usar os fluxos cin, cout ou o especificador %I64d.

Saída
Imprima na linha única " SIM " se n for um número quase da sorte. Caso contrário, imprima " NÃO " (sem as aspas).

Exemplos
Entrada
40047

Saída
NÃO

-------------
Entrada
7747774

Saída
SIM

-------------
Entrada
1000000000000000000

Saída
NÃO

Observação
Na primeira amostra há 3 dígitos da sorte (o primeiro e os dois últimos), então a resposta é " NÃO ".

Na segunda amostra, há 7 dígitos da sorte, 7 é um número da sorte, então a resposta é " SIM ".

Na terceira amostra não há dígitos da sorte, então a resposta é " NÃO ".
'''
#A QUANTIDADE DE NÚMEROS DA SORTE DEVEM SER 4 OU 7

sorte = 0

n = list(input())

for i in n:
	if(i == '4' or i == '7'):
		sorte += 1


if(sorte == 4 or sorte == 7):
	print('YES')
else:
	print('NO')
