'''
112A - PETYA E CORDAS (PETYA AND STRINGS)

Petya adora presentes. Sua mãe comprou-lhe duas cordas do mesmo tamanho para o seu aniversário. As cordas consistem em letras latinas maiúsculas e minúsculas. Agora Petya quer comparar essas duas cordas lexicograficamente. O caso das letras não importa, ou seja, uma letra maiúscula é considerada equivalente à letra minúscula correspondente. Ajude Petya a fazer a comparação.

Entrada
Cada uma das duas primeiras linhas contém uma string comprada. Os comprimentos das cordas variam de 1 para 100 inclusivo. É garantido que as cordas são do mesmo comprimento e também consistem em letras latinas maiúsculas e minúsculas.

Saída
Se a primeira string for menor que a segunda, imprima "-1". Se a segunda string for menor que a primeira, imprima "1". Se as cordas forem iguais, imprima "0". Note que o caso das letras não é levado em consideração quando as cordas são comparadas.

Exemplos
Entrada
aaaa
aaaA

Saída
0

---------

Entrada
abs
Abz

Saída
-1

----------

Entrada
abcdefg
AbCdEfF

Saída
1

Nota
Se você quiser informações mais formais sobre a ordem lexicográfica (também conhecida como "ordem do dicionário"ou "ordem alfabética"), você pode visitar o seguinte site:

http://en.wikipedia.org/wiki/Lexicographical_order
'''
contador = 0
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z']

l1 = input()
l2 = input()

for i in range(len(list(l1))):
	l1 = l1.lower()
	l2 = l2.lower()

	if(list(l1[i]) == list(l2[i])):
		contador = 0
	else:
		letral1 = letras.index(l1[i])
		letral2 = letras.index(l2[i])

		if(letral1 > letral2):
			contador = 1
			break
		else:
			contador = -1
			break

print(contador)
