# Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é:
# F = ((9 x C) / 5) + 32
celcius = float(input("Temperatura (ºC): "))
print(f"A temperatura de {celcius}ºC é de {((9 * celcius) / 5) + 32}ºF.")