import datetime
# Pegando dia da semana em formato de número
diaSemana = datetime.date.isoweekday(datetime.date.today())

# Determinando qual é o dia da semana.
if(diaSemana == 1):
	print('Segunda-feira')
elif(diaSemana == 2):
	print('Terça-feira')
elif(diaSemana == 3):
	print('Quarta-feira')
elif(diaSemana == 4):
	print('Quinta-feira')
elif(diaSemana == 5):
	print('Sexta-feira')
elif(diaSemana == 6):
	print('Sábado')
else:
	print('Domingo')

# É possível fazer com match case, mas decidir manter o nível.