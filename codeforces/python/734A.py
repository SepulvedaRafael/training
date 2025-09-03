'''
734A - ANTON AND DANIK

Anton gosta de jogar xadrez, assim como seu amigo Danik.

Depois de jogarem n jogos seguidos. Para cada jogo, sabe-se quem foi o vencedor — Anton ou Danik. Nenhum dos jogos terminou empatado.

Agora Anton se pergunta, quem ganhou mais jogos, ele ou Danik? Ajude-o a determinar isso.

Entrada
A primeira linha da entrada contém um único inteiro n ( 1 ≤  n  ≤ 100 000 ) — o número de jogos disputados.

A segunda linha contém uma string s , consistindo de n letras maiúsculas inglesas ' A ' e ' D ' — o resultado de cada um dos jogos. O i -ésimo caractere da string é igual a ' A ' se Anton venceu o i -ésimo jogo e ' D ' se Danik venceu o i -ésimo jogo.

Saída
Se Anton venceu mais jogos que Danik, imprima " Anton " (sem aspas) na única linha da saída.

Se Danik venceu mais jogos que Anton, imprima " Danik " (sem aspas) na única linha da saída.

Se Anton e Danik venceram o mesmo número de jogos, imprima " Amizade " (sem aspas).

Exemplos
Entrada
6
ADAAAA

Saída
Anton

-------------
Entrada
7
DDDAADA

Saída
Danik

-------------
Entrada
6
DADADA

Saída
Friendship
'''
a = 0
d = 0

n = int(input())
s = input().upper()

for i in s:
	if(i == 'A'):
		a += 1
	else:
		d += 1

if(a > d):
	print('Anton')
elif(a == d):
	print('Friendship')
else:
	print('Danik')