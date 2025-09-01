'''Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade kWh consumida eo tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

+-------------------+-----------------+---------------+
|       Tipo        |   Faixa (kWh)   |     Preço     |
+-------------------+-----------------+---------------+
|    Residencial    | Até 500         |    R$ 0,40    |
|                   | Acima de 500    |    R$ 0,65    |
+-------------------+-----------------+---------------+
|     Comercial     | Até 1000        |    R$ 0,55    |
|                   | Acima de 1000   |    R$ 0,60    |
+-------------------+-----------------+---------------+
|    Industrial     | Até 5000        |    R$ 0,55    |
|                   | Acima de 5000   |    R$ 0,60    |
+-------------------+-----------------+---------------+
'''
quantidade_kwh = int(input("Quantidade de Kwh: "))
tipo_instalacao = input("Tipo de instalação (R/I/C): ")

if tipo_instalacao == "R":
    if quantidade_kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_instalacao == "C":
    if quantidade_kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo_instalacao == "I":
    if quantidade_kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Tipo inválido, digite R, C ou I.")
    preco = 0
print(f"Preço a pagar: R${quantidade_kwh * preco:5.2f}")