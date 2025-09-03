'''
281A - CAPITALIZAÇÃO DE PALAVRAS (WORD CAPITALIZATION)

Capitalização é escrever uma palavra com sua primeira letra como uma letra maiúscula. Sua tarefa é capitalizar a palavra dada.

Observe que durante a capitalização todas as letras, exceto a primeira, permanecem inalteradas.

Entrada
Uma única linha contém uma palavra não vazia. Esta palavra consiste em letras maiúsculas e minúsculas do inglês. O comprimento da palavra não excederá 10 3 .

Saída
Exibe a palavra fornecida após a capitalização.

Exemplos
Entrada
ApPLe

Saída
ApPLe

-------------

Entrada
konjac

Saída
Konjac
'''
palavra = list(input())

if (palavra[0] == palavra[0].lower()):
	palavra[0] = palavra[0].upper()
	msg = ""
	for i in palavra:
		msg += i
	print(msg)
else:
	msg = ""
	for i in palavra:
		msg += i
	print(msg)
