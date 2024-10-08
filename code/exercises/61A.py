'''
61A - MATEMÁTICO ULTRA-RÁPIDO (Ultra-Fast Mathematician)

Shapur era um aluno extremamente talentoso. Ele era ótimo em tudo, incluindo Combinatória, Álgebra, Teoria dos Números, Geometria, Cálculo, etc. Ele não era apenas inteligente, mas extraordinariamente rápido! Ele conseguia somar 10 18 números em um único segundo.

Um dia, em 230 d.C., Shapur estava tentando descobrir se alguém poderia fazer cálculos mais rápido do que ele. Como resultado, ele fez um grande concurso e pediu a todos que viessem e participassem.

Em seu concurso, ele deu aos concorrentes muitos pares diferentes de números. Cada número é feito de dígitos 0 ou 1 . Os concorrentes devem escrever um novo número correspondente ao par de números fornecido. A regra é simples: O i -ésimo dígito da resposta é 1 se e somente se o i -ésimo dígito dos dois números fornecidos diferirem. No outro caso, o i -ésimo dígito da resposta é 0 .

Shapur fez muitos números e primeiro tentou sua própria velocidade. Ele viu que podia executar essas operações em números de comprimento ∞ (o comprimento de um número é o número de dígitos nele) em um piscar de olhos! Ele sempre dá respostas corretas, então espera que os competidores também dêem respostas corretas. Ele é um bom sujeito, então não dá a ninguém números muito grandes e sempre dá a uma pessoa números do mesmo comprimento.

Agora você vai participar do concurso de Shapur. Veja se você é mais rápido e preciso.

Entrada
Há duas linhas em cada entrada. Cada uma delas contém um único número. É garantido que os números são feitos de 0 e 1 somente e que seu comprimento é o mesmo. Os números podem começar com 0. O comprimento de cada número não excede 100.

Saída
Escreva uma linha — a resposta correspondente. Não omita os 0 s iniciais.

Exemplos
Entrada
1010100
0100101

Saída
1110001

-----------------
Entrada
000
111

Saída
111

----------------
Entrada
1110
1010

Saída
0100

----------------
Entrada
01110
01100

Saída
00010
'''
	n1 = list(input())
	n2 = list(input())
	output = []

	for i in range(len(n1)):
		if(n1[i] == '1' and n2[i] == '1'):
			output.append('0')
		elif((n1[i] == '1' and n2[i] == '0') or (n1[i] == '0' and n2[i] == '1')):
			output.append('1')
		else:
			output.append('0')

	msg = ""
	for i in output:
		msg += i
	print(msg)