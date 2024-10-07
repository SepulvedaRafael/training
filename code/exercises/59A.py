'''
59A - PALAVRA (WORD)

Vasya está muito chateado que muitas pessoas na Net misturam letras maiúsculas e minúsculas em uma palavra. É por isso que ele decidiu inventar uma extensão para seu navegador favorito que alteraria o registro das letras em cada palavra, de modo que consistisse apenas em letras minúsculas ou, vice-versa, apenas em letras maiúsculas. Com isso, o mínimo possível de letras deve ser alterado na palavra. Por exemplo, a palavra HoUse deve ser substituído por casa, e a palavra ViP — com VIP. Se uma palavra contém um número igual de letras maiúsculas e minúsculas, você deve substituir todas as letras por letras minúsculas. Por exemplo maTRIx deve ser substituído por matriz. Sua tarefa é usar o método dado em uma determinada palavra.

Entrada
A primeira linha contém uma palavra s — consiste em letras latinas maiúsculas e minúsculas e possui o comprimento de 1 para 100.

Saída
Imprimir a palavra corrigida s. Se a palavra dada s tem estritamente mais letras maiúsculas, faça a palavra escrita no registro maiúsculo, caso contrário - na minúscula.

Exemplos
Entrada
HoUse

Saída
casa

-----------
Entrada
ViP

Saída
VIP

-----------
Entrada
maTRIx

Saída
matriz
'''
i = 0

upper = 0
lower = 0

s = list(input())

msg = ""
while(i < len(s)):
	if(s[i] == s[i].upper()):
		upper += 1
	else:
		lower += 1

	i += 1

msg = ""
if(upper > lower):
	for j in s:
		msg += j
	print(msg.upper())

else:
	for j in s:
		msg += j
	print(msg.lower())