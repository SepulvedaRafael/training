'''
1047 - TEMPO DE JOGO COM MINUTOS

Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XX HORA(S) E YYY MINUTO(S)” .

horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()

horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)


if (horaFinal - horaInicial) == 1 and (minutoInicial > minutoFinal): #
	auxM = 60 - minutoInicial
	duracaoM = auxM + minutoFinal
	duracaoH = 0

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")

elif (horaInicial == horaFinal) and (minutoInicial == minutoFinal): #
	duracaoH = 24
	duracaoM = 0

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")

elif (horaFinal > horaInicial) and (minutoFinal > minutoInicial): #
	duracaoH = horaFinal - horaInicial
	duracaoM = minutoFinal - minutoInicial

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")

elif (horaFinal > horaInicial) and (minutoInicial > minutoFinal): #
	duracaoH = (horaFinal - horaInicial) - 1

	aux = 60 - minutoInicial
	duracaoM = aux + minutoFinal

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")

elif (horaFinal == horaInicial) and (minutoFinal > minutoInicial): #
	duracaoH = 0

	duracaoM = minutoFinal - minutoInicial

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")

elif (horaInicial > horaFinal): #
	auxH = 24 - horaInicial
	duracaoH = auxH + horaFinal

	if (minutoInicial > minutoFinal):
		duracaoH = duracaoH - 1

		auxM = 60 - minutoInicial
		duracaoM = auxM + minutoFinal

		print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")

	else:
		duracaoM = minutoFinal - minutoInicial

		print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")
'''
horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()

horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)

duracaoInicial = horaInicial * 60 + minutoInicial
duracaoFinal = horaFinal * 60 + minutoFinal

if (duracaoFinal > duracaoInicial):
	duracaoTotal = duracaoFinal - duracaoInicial

	duracaoH = duracaoTotal // 60
	duracaoM = duracaoTotal % 60

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")
else:
	duracaoTotal = (24 * 60 - duracaoInicial) + duracaoFinal

	duracaoH = duracaoTotal // 60
	duracaoM = duracaoTotal % 60

	print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")