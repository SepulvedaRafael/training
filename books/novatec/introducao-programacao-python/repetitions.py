# Contador + Input
'''fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
    print(x)
    x += 1'''

# Números pares
'''fim = int(input("Digite um número: "))
x = 0
while x <= fim:
    print(x)
    x += 2'''

# Tabuada
'''n = int(input("Tabuada de: "))
x = 1
while x <= 10:
    print(f"{x} x {n} = {n * x}")
    x += 1'''

# Acumuladores
'''x = 1
soma = 0
while x <= 5:
    n = int(input(f"{x} Digite o número: "))
    soma += n
    x += 1
print(f"Média: {soma / 5:5.2f}")'''

# Contagem de cédulas
'''valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0'''

# Tabuada toda
tabuada = 1
while tabuada <= 10:
    num = 1
    while num <= 10:
        print(f"{tabuada:2.0f} x {num:2.0f} = {tabuada * num}")
        num += 1
    tabuada += 1