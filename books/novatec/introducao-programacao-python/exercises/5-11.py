# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
deposito = float(input("Depósito inicial: R$"))
tx_juros = int(input("Taxa de Juros (%): "))

mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (tx_juros / 100))
    print(f"Mês {mes}: R${saldo:5.2f}")
    mes += 1
print(f"O valor total obtido com juros foi: R${saldo-deposito:5.2f}")