#-----------------------------------------------
'''a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O primeiro valor é o maior!")
if b > a:
    print("O segundo valor é o maior!")'''
#-----------------------------------------------
'''idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo!")
if idade > 3:
    print("Seu carro é velho!")
'''
#-----------------------------------------------
'''salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salário: R${salario:6.2f}")
print(f"Imposto a pagar: R${imposto:6.2f}")'''
#-----------------------------------------------
'''idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo!")
else:
    print("Seu carro é velho!")'''
#-----------------------------------------------
'''minutos = int(input("Quantos minutos você utilizou este mês: "))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f"Você vai pagar este mês: R${minutos * preco:6.2f}")'''
#-----------------------------------------------
'''categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0
print(f"O preço do produto é: R${preco:6.2f}")'''
#-----------------------------------------------
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    preco = 0
print(f"O preço do produto é: R${preco:6.2f}")
#-----------------------------------------------
#-----------------------------------------------