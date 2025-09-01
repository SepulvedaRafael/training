# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
velocidade = int(input("Velocidade do carro (Km/h): "))
if (velocidade > 80):
    print("Você foi multado!")
    print(f"Valor a ser pago: R${(velocidade - 80) * 5:5.2f}")
