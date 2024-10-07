'''
266B - FILA NA ESCOLA (QUEUE AT THE SCHOOL)

Durante o intervalo os escolares, meninos e meninas, formaram uma fila de n pessoas na cantina. Inicialmente, as crianças estavam na ordem em que entraram na cantina. No entanto, depois de um tempo, os meninos começaram a se sentir desconfortáveis por ficarem na frente das meninas na fila e começaram a deixar as meninas avançarem a cada segundo.

Vamos descrever o processo com mais precisão. Digamos que as posições na fila são numeradas sequencialmente por inteiros de 1 para n, em que a pessoa no número da posição 1 é servido primeiro. Então, se no momento x um menino está no eua posição e uma menina está no (eu + 1)a posição, então no momento x + 1 o eua posição terá uma menina e o (eu + 1)a posição terá um menino. O tempo é dado em segundos.

Você tem a posição inicial das crianças, no momento inicial do tempo. Determine como a fila vai cuidar t segundos.

Entrada
A primeira linha contém dois inteiros n e t (1 ≤ n t ≤ 50), que representam o número de filhos na fila e o tempo após o qual a fila se transformará no arranjo que você precisa encontrar.

A próxima linha contém string s, que representa o arranjo inicial dos escolares. Se o eua posição na fila contém um rapaz, depois o eu- o caráter da corda s igual a "B", caso contrário, o euo caractere é igual a "G".

Saída
Corda de impressão a, que descreve o arranjo depois t segundos. Se o eua posição tem um menino após o tempo necessário, então o eu- o personagem a deve ser igual a "B", caso contrário, deve ser igual a "G".

Exemplos
Entrada
5 1
BGGBG

Saída
GBGGB

------------

Entrada
5 2
BGGBG

Saída
GGBGB

------------

Entrada
4 1
GGGB

Saída
GGGB
'''
i = 0

n, t = map(int, input().split())
s = input()

'''
ATTEMPT SOLO

while(i < t):
	s = list(s)
	for j in range(n-1, 0, -1):
		if(s[j] == 'G' and s[j - 1] == 'B'):
			s[j] = 'B'
			s[j - 1] = 'G'

	i += 1
'''

while(i < t):
	s = list(s)
	j = 1
	while j < n:
		if(s[-j] == 'G' and s[-j - 1] == 'B'):
			s[-j] = 'B'
			s[-j - 1] = 'G'
			j += 2
		else:
			j += 1
	i += 1

msg = ""
for k in s:
	msg += k
print(msg)