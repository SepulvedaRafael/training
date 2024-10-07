'''
HR007 - Staircase
Detalhe da escada

Esta é uma escada de tamanho n = 4:
   #
  ##
 ###
####

Sua base e altura são iguais a . É desenhado usando # símbolos e espaços. A última linha não é precedida por nenhum espaço.

Escreva um programa que imprime uma escada de tamanho n.

Descrição da Função
Completar o escada função no editor abaixo.

a escada tem o seguinte parâmetro(s):
int n: um número inteiro

Imprimir
Imprima uma escada como descrito acima.

Formato de Entrada
Um único número inteiro , denotando o tamanho da escada.

Restrições
0 < n <= 100.

Formato de Saída
Imprima uma escada de tamanho  usando # símbolos e espaços.
Nota: A última linha deve ter espaços nele.

Entrada de Amostra
6

Saída da Amostra
     #
    ##
   ###
  ####
 #####
######

Explicação
A escada está alinhada à direita, composta por # símbolos e espaços, e tem uma altura e largura de .
'''
i = 1
n = int(input().strip())

while (i <= n):
	print(' ' * (n - i) + '#' * i)
	i += 1