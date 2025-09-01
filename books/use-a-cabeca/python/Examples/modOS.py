import os

# Diretório da pasta principal
where_am_I = os.getcwd()
print(where_am_I)

# Acessando variáveis de ambiente
print(os.environ)

# Acessando individualmente
print(os.getenv('HOMEPATH'))