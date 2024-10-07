'''
HR010 - Time Conversion
Dado um tempo em 12 formato AM/PM hora, convertê-lo para o tempo militar (24 horas).

Nota: - 12:00:00AM em um relógio de 12 horas é 00:00:00 em um relógio de 24 horas.
- 12:00:00PM em um relógio de 12 horas é 12:00:00 em um relógio de 24 horas.

Exemplo
s = '12:01:00PM'
Retorno '12:01:00'.

s = '12:01:00AM'
Retorno '00:01:00'.

Descrição da Função
Completar o timeConversão função no editor abaixo. Ele deve retornar uma nova string representando o tempo de entrada no formato de 24 horas.

timeConversion tem o seguinte parâmetro(s):
corda s: um tempo em formato de hora

Retorna
corda: o tempo em formato de hora

Formato de Entrada
Uma única corda isso representa um tempo em - formato de relógio de hora (ou seja: ou ).

Restrições
Todos os tempos de entrada são válidos

Entrada da amostra 0
07:05:45PM

Saída da amostra 0
19:05:45
'''
s = input()

if('AM' in s):
	if('12' in s):
		s = s.split(':')
		s[0] = '00'
	else:
		s = s.split(':')

if('PM' in s):
	if('24' in s):
		s = s.split(':')
		s[0] = '00'
	if('12' in s):
		s = s.split(':')
	else:
		s = s.split(':')
		s[0] = int(s[0])
		s[0] = s[0] + 12
		s[0] = str(s[0])

msg = ''
for i in s:
	if(('AM' in i) or ('PM' in i)):
		msg += i
	else:
		msg += i + ':'

if('AM' in msg):
	print(msg.replace('AM', ''))
else:
	print(msg.replace('PM', ''))