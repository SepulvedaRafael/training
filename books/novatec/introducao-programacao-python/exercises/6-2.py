# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
l1 = []
l2 = []
while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    l1.append(valor)

while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    l2.append(valor)

l3 = l1[:] # Copia a l1
l3.extend(l2) # Extende uma lista na outra

i = 0
while i < len(l3):
    print(f"L3[{i}] = {l3[i]}")
    i += 1