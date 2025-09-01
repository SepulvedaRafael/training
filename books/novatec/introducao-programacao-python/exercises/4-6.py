# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas.
distancia = int(input("Distância (km): "))
preco = 0.5
if distancia > 200:
    preco = 0.45
print(f"O preço total é: R${distancia * preco:5.2f}")