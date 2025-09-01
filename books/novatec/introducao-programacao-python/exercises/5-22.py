# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabela da operação escolhida. Repita até que a opção sair deseja escolhida.
while True:
    print("+------------------------------+")
    print("|      MENU DAS OPERAÇÕES      |")
    print("+------------------------------+")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    opcao = int(input("Digite uma das opções: "))

    if opcao == 0:
        break
    elif opcao < 5:
        num = int(input("Tabuada de: "))
        x = 1
        while x <= 10:
            if opcao == 1:
                print(f"{num} + {x} = {num + x}")
            elif opcao == 2:
                print(f"{num} - {x} = {num - x}")
            elif opcao == 3:
                print(f"{num} * {x} = {num * x}")
            elif opcao == 4:
                print(f"{num} / {x} = {num / x}")
            x += 1
    else:
        print("Opções inválida! Tente de 1 a 5.\n")