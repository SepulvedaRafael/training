'''
41A - TRADUÇÃO (TRANSLATION)

A tradução da língua Berland para a língua Birland não é uma tarefa fácil. Essas línguas são muito semelhantes: uma palavra Berlandish difere um pouco de uma palavra Birlandish com o mesmo significado: ela é escrita (e pronunciada) inversamente. Por exemplo, uma palavra Berlandish code corresponde a uma palavra Birlandish edoc . No entanto, cometer um erro durante a "tradução" é fácil. Vasya traduziu a palavra s de Berlandish para Birlandish como t . Ajude-o: descubra se ele traduziu a palavra corretamente.

Entrada
A primeira linha contém a palavra s , a segunda linha contém a palavra t . As palavras consistem em letras latinas minúsculas. Os dados de entrada não contêm espaços desnecessários. As palavras não estão vazias e seus comprimentos não excedem 100 símbolos.

Saída
Se a palavra t for uma palavra s , escrita ao contrário, imprima SIM , caso contrário, imprima NÃO .

Exemplos
Entrada
code
edoc

Saída
YES

-------------
Entrada
abb
aba

Saída
NO

-------------
Entrada
code
code

Saída
NO
'''
i = 1
si = ""

s = input().strip()
t = input().strip()

while(i <= len(s)):
	si += s[-i]
	i += 1

if(si == t):
	print('YES')
else:
	print('NO')