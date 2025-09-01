# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
km_percorridos = float(input("Km's percorridos: "))
quantidade_dias_alugado = int(input("Dias alugado: "))
print(f"O preço a pagar é: R${60 * quantidade_dias_alugado + (0.15 * km_percorridos):5.2f}")