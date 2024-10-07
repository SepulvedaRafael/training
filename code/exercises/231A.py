'''
231A - EQUIPE (TEAM)

Um dia, três melhores amigos Petya, Vasya e Tonya decidiram formar uma equipe e participar de concursos de programação. Os participantes geralmente recebem vários problemas durante os concursos de programação. Muito antes do início, os amigos decidiram que implementariam um problema se pelo menos dois deles tivessem certeza da solução. Caso contrário, os amigos não escreverão a solução do problema.

Este concurso oferece n problemas aos participantes. Para cada problema que conhecemos, qual amigo tem certeza sobre a solução. Ajude os amigos a encontrar o número de problemas para os quais eles escreverão uma solução.

Entrada
A primeira linha de entrada contém um único número inteiro n (1 ≤ n ≤ 1000) — o número de problemas no concurso. Então n as linhas contêm três inteiros cada, cada inteiro é 0 ou 1. Se o primeiro número da linha for igual 1então Petya tem certeza sobre a solução do problema, caso contrário, ele não tem certeza. O segundo número mostra a visão de Vasya sobre a solução, o terceiro número mostra a visão de Tonya. Os números nas linhas são separados por espaços.

Saída
Imprimir um único inteiro — o número de problemas que os amigos irão implementar no concurso.

Exemplos

Entrada
3
1 1 0
1 1 1
1 0 0

Saída
2
-----------------------
Entrada
2
1 0 0
0 1 1

Saída
1


Nota
Na primeira amostra Petya e Vasya têm certeza de que eles sabem como resolver o primeiro problema e todos os três sabem como resolver o segundo problema. Isso significa que eles vão escrever soluções para esses problemas. Apenas Petya tem certeza sobre a solução para o terceiro problema, mas isso não é suficiente, então os amigos não vão aceitar.

Na segunda amostra, os amigos só implementarão o segundo problema, já que Vasya e Tonya têm certeza da solução.
'''
casos = 0
n = int(input())

for i in range(1, n+1):
	petya, vasya, tonya = input().split()

	petya = int(petya)
	vasya = int(vasya)
	tonya = int(tonya)

	if(petya == 1 and vasya == 1 and tonya == 1):
		casos += 1
	elif(petya == 1 and vasya == 1 and tonya == 0):
		casos += 1
	elif(petya == 1 and vasya == 0 and tonya == 1):
		casos += 1
	elif(petya == 0 and vasya == 1 and tonya == 1):
		casos += 1

print(casos)
