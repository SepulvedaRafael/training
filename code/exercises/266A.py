'''
266A - PEDRAS NA MESA (STONES ON THE TABLE)

Existem n pedras na mesa em uma fileira, cada uma delas pode ser vermelha, verde ou azul. Conte o número mínimo de pedras para tirar da mesa para que quaisquer duas pedras vizinhas tenham cores diferentes. Pedras seguidas são consideradas vizinhas se não houver outras pedras entre elas.

Entrada
A primeira linha contém inteiro n (1 ≤ n ≤ 50) — o número de pedras na mesa.

A próxima linha contém string s, que representa as cores das pedras. Vamos considerar as pedras na linha numeradas de 1 para n da esquerda para a direita. Então o eu- o personagem s igual a "R", se o eua pedra é vermelha, "G", se for verde e "B", se for azul.

Saída
Imprimir um único inteiro — a resposta ao problema.

Exemplos
Entrada
3
RRG

Saída
1

-------------
Entrada
5
RRRRR

Saída
4

-------------
Entrada
4
BRBG

Saída
0
'''
diff = 0
x = 1

n = int(input())
pedras = input()

if(n >= 1 and n <= 50):
	for i in range(0, len(pedras) -1):
		if(pedras[i] == pedras[i + 1]):
			diff += 1
		else:
			continue

print(diff)