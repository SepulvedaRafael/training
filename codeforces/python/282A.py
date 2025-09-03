'''
282A - BIT++

A linguagem de programação clássica do Bitland é Bit++. Essa linguagem é tão peculiar e complicada.

A linguagem é tão peculiar como tem exatamente uma variável, chamada x. Além disso, existem duas operações:

Operação ++ aumenta o valor da variável x por 1.
Operação - diminui o valor da variável x por 1.
Uma instrução na linguagem Bit++ é uma sequência, consistindo exatamente em uma operação e uma variável x. A declaração é escrita sem espaços, ou seja, só pode conter caracteres "+", "-", "X". Executar uma instrução significa aplicar a operação que ela contém.

Um programa em Bit++ é uma sequência de instruções, cada uma delas precisa ser executada. Executar um programa significa executar todas as instruções que ele contém.

Você recebe um programa na linguagem Bit++. O valor inicial de x é 0. Executar o programa e encontrar o seu valor final (o valor da variável quando este programa é executado).

Entrada
A primeira linha contém um único número inteiro n (1 ≤ n ≤ 150) — o número de declarações no programa.

Próximo n as linhas contêm uma declaração cada. Cada instrução contém exatamente uma operação (++ ou -) e exatamente uma variável x (denotado como letra «X»). Assim, não há declarações vazias. A operação e a variável podem ser escritas em qualquer ordem.

Saída
Imprimir um único inteiro — o valor final de x.

Exemplos
Entrada
1
++X

Saída
1
------------------
Entrada
2
X++
--X

Saída
0
'''
x = 0
n = int(input())

for i in range(1, n+1):
	declaracao = input().strip()

	if(declaracao == '++X' or declaracao == 'X++'):
		x += 1
	else:
		x -= 1

print(x)