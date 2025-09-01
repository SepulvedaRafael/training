'''Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de código a seguir para obter o preço de cada produto:

+--------------------------------+
|     Código     |     Preço     |
+----------------+---------------+
|       1        |     0,50      |
+----------------+---------------+
|       2        |     1,00      |
+----------------+---------------+
|       3        |     4,00      |
+----------------+---------------+
|       5        |     7,00      |
+----------------+---------------+
|       9        |     8,00      |
+----------------+---------------+

Seu programa deve exibir o total de compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".
'''
total = 0
while True:
    codigo_produto = int(input("Digite o código do produto (1, 2, 3, 5, 9): "))
    if codigo_produto == 0:
        break
    elif codigo_produto == 1 or codigo_produto == 2 or codigo_produto == 3 or codigo_produto == 5 or codigo_produto == 9:
        qtd_produto = int(input("Quantidade do produto: "))
        if codigo_produto == 1:
            preco = 0.5
        elif codigo_produto == 2:
            preco = 1
        elif codigo_produto == 3:
            preco = 4
        elif codigo_produto == 5:
            preco = 7
        else:
            preco = 8
        total +=  preco * qtd_produto
    else:
        print("Código inválido!")
print(f"O total da compra foi: R${total:8.2f}")
