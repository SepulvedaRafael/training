import datetime

# Data de hoje
print(datetime.date.today())

# Acessando dia, mês e ano individualmente.
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

# Data em formato de string
print(datetime.date.isoformat(datetime.date.today()))