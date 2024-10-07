'''
HR013 - Kangaroo
Você está coreografando um show de circo com vários animais. Por um ato, você recebe dois cangurus em uma linha numérica pronta para pular na direção positiva (ou seja, em direção ao infinito positivo).

- O primeiro canguru começa no local x1 e se move a uma taxa de v1 metros por salto.
- O segundo canguru começa no local x2 e se move a uma taxa de v2 metros por salto.

Você tem que descobrir uma maneira de obter ambos os cangurus no mesmo local, ao mesmo tempo, como parte do show. Se possível, retorne YES, caso contrário, retorne NO.

Exemplo
x1 = 2
v1 = 1
x2 = 1
v2 = 2

Depois de um salto, ambos estão em x = 3, (x1 + v1 = 2 + 1 | x2 + v2 = 1 + 2), então a resposta é YES.

Descrição da Função
Complete a função canguru no editor abaixo.

canguru tem o seguinte parâmetro(s):
int x1, int v1: posição inicial e distância de salto para canguru 1
int x2, int v2: posição inicial e distância de salto para canguru 2

Retorna
corda: qualquer um YES ou NO

Formato de Entrada
Uma única linha de quatro inteiros separados por espaço, denotando os respectivos valores de x1, v1, x2 e v2.

Restrições
0 <= x1 < x2 <= 10000
1 <= v1 <= 10000
1 <= v2 <= 10000

Entrada da amostra 0
0 3 4 2

Saída da amostra 0
SIM

Explicação 0

Os dois cangurus saltam através da seguinte sequência de locais:

A partir da imagem, fica claro que os cangurus se encontram no mesmo local (número 12 na linha numérica) após o mesmo número de saltos (4 saltos), e imprimimos YES.

Entrada da amostra 1
0 2 5 3

Saída da amostra 1
NÃO

Explicação 1
O segundo canguru tem um local inicial que está à frente (mais à direita) do local inicial do primeiro canguru (ou seja, x2 > x1). Porque o segundo canguru se move a um ritmo mais rápido (o que significa v2 > v1) e já está à frente do primeiro canguru, o primeiro canguru nunca será capaz de alcançar. Assim, imprimimos NÃO.
'''
x1, v1, x2, v2 = map(int, input().rstrip().split())

while True:
	x1 += v1
	x2 += v2

	if(x1 == x2):
		print('YES')
		break
	elif(x2 > x1 and v2 > v1):
		print('NO')
		break
	elif(v1 == v2):
		print('NO')
		break
	elif(x1 > x2):
		print('NO')
		break