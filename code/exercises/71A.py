'''
71A - PALAVRAS MUITO LONGAS (WAY TOO LONG WORDS)

Algumas vezes algumas palavras como "localização"ou "internacionalização"são tão longos que escrevê-los muitas vezes em um texto é bastante cansativo.

Vamos considerar uma palavra muito tempo, se o seu comprimento é estritamente mais do 10 personagens. Todas as palavras muito longas devem ser substituídas por uma abreviatura especial.

Esta abreviatura é feita assim: escrevemos a primeira e a última letra de uma palavra e entre elas escrevemos o número de letras entre a primeira e a última. Esse número está no sistema decimal e não contém zeros à esquerda.

Assim, "localização"será escrito como "l10n", e "internacionalização» será escrito como "i18n".

Sugere-se que você automatize o processo de alteração das palavras com abreviaturas. Em que todas as palavras muito longas devem ser substituídas pela abreviatura e as palavras que não são muito longas não devem sofrer quaisquer alterações.

Entrada
A primeira linha contém um número inteiro n (1 ≤ n ≤ 100). Cada um dos seguintes n linhas contém uma palavra. Todas as palavras consistem em letras latinas minúsculas e possuem os comprimentos de 1 para 100 personagens.

Saída
Imprimir n linhas. O eua linha deve conter o resultado da substituição do eu- a palavra dos dados de entrada.

Exemplos
Entrada
4
palavra
localização
internacionalização
pneumonoultramicroscópicosilicovolcanoconiose

Saída
palavra
l10n
i18n
p43
'''
listaPalavras = []

n = int(input())

for i in range(1, n+1):
	palavra = input()

	letras = 0
	for i in palavra:
		letras += 1

	if(letras > 10):
		listaPalavras.append(f"{palavra.lower()[0]}{letras-2}{palavra.lower()[letras-1]}")
	else:
		listaPalavras.append(palavra)

for j in listaPalavras:
	print(j)