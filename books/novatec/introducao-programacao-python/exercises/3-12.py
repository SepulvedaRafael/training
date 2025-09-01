# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = int(input("Distância a percorrer (km): "))
velocidade_media = int(input("Velocidade média (km/h): "))
print(f"O tempo da viagem é de {distancia / velocidade_media:.0f} hora(s).")