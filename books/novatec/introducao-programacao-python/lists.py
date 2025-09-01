# Cálculo da média
'''notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:5.2f}")'''

# Cálco da média com notas digitadas
'''notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma / x:5.2f}")'''

# Apresentação de números
'''numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f"Número {x + 1}: "))
    x += 1

while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido - 1]}")'''

# Cópia e Fatiamento
'''L = [1, 2, 3, 4, 5]
V = L[:] # Realiza uma cópia dos valores e não atribui uma referência da lista na memória
V[0] = 6
print(L)
print(V)'''

# Fila
'''ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S): ")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")'''

# Pilha
'''prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha.")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S): ")
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")'''

# Pesquisa sequencial
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não foi encontrado.")