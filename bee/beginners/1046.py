'''
1046 - TEMPO DE JOGO

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
'''
horaInicial, horaFinal = input().split()

horaInicial = int(horaInicial)
horaFinal = int(horaFinal)

if horaInicial > horaFinal:
	aux = 24 - horaInicial
	duracao = aux + horaFinal
	print(f"O JOGO DUROU {duracao} HORA(S)")

elif horaFinal > horaInicial:
	duracao = horaFinal - horaInicial
	print(f"O JOGO DUROU {duracao} HORA(S)")

elif horaInicial == horaFinal:
	duracao = 24
	print(f"O JOGO DUROU {duracao} HORA(S)")