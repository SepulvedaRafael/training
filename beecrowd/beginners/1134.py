'''
1134 - TIPO DE COMBUSTÍVEL

Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           8            |         MUITO OBRIGADO         |
|           1			 |           Alcool: 1            |
|           7 			 |           Gasolina: 2          |
|           2            |           Diesel: 0            |
|           2			 |                                |
|           4 			 |                                |
+------------------------+--------------------------------+
'''
x = True

alcool = 0
gasolina = 0
diesel = 0

while x:
	tipo = int(input())

	match tipo:
		case 1:
			alcool += 1
		case 2:
			gasolina += 1
		case 3:
			diesel += 1
		case 4:
			x = False

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')