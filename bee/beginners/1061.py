'''
1061 - TEMPO DE UM EVENTO [NÃO CONCLUIDO]

Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''
diasI = input().split(" ")

horasI, minutosI, segundosI = input().split(":")

diasI = int(diasI[1])
horasI = int(horasI)
minutosI = int(minutosI)
segundosI = int(segundosI)

diasF = input().split(" ")

horasF, minutosF, segundosF = input().split(":")

diasF = int(diasF[1])
horasF = int(horasF)
minutosF = int(minutosF)
segundosF = int(segundosF)

dias = diasF - diasI
horas = horasF - horasI
minutos = minutosF - minutosI
segundos = segundosF - segundosI

if(horas < 0):
	horas = 24 + horas
	dias = dias - 1

if(minutos < 0):
	minutos = 60 + minutos
	horas = horas - 1

if(segundos < 0):
	segundos = 60 + segundos
	minutos = minutos - 1

if(dias <= 0):
	dias = 0

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')