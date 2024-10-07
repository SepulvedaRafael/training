'''
HR008 - Mini-Max Sum
Dado cinco inteiros positivos, encontre os valores mínimo e máximo que podem ser calculados somando exatamente quatro dos cinco inteiros. Em seguida, imprima os respectivos valores mínimo e máximo como uma única linha de dois inteiros longos separados por espaço.

Exemplo
arr = [1, 3, 5, 7, 9]

A soma mínima é 1 + 3 + 5 + 7 = 16 e a soma máxima é 3 + 5 + 7 + 9 = 24. A função imprime
16 24

Descrição da Função
Completar o miniMaxSum função no editor abaixo.

miniMaxSum tem o seguinte parâmetro(s):
arr: uma matriz de inteiros

Imprimir
Imprima dois inteiros separados por espaço em uma linha: a soma mínima e a soma máxima de de elementos.

Formato de Entrada
Uma única linha de cinco inteiros separados por espaço.

Restrições
1 <= arr[i] <= 10**9

Formato de Saída
Imprima dois inteiros longos separados por espaço, denotando os respectivos valores mínimos e máximos que podem ser calculados somando exatamente quatro dos cinco inteiros. (A saída pode ser maior que um inteiro de 32 bits.)

Entrada de Amostra
1 2 3 4 5

Saída da Amostra
10 14

Explicação
Os números são 1, 2, 3, 4 e 5. Calcule as seguintes somas usando quatro dos cinco inteiros:

1. Tudo, exceto é a soma 2 + 3 + 4 +5 = 14.
2. Tudo, exceto é a soma 1 + 3 + 4 +5 = 13.
3. Tudo, exceto é a soma 1 + 2 + 4 +5 = 12.
4.Tudo, exceto é a soma 1 + 2 + 3 + 5 = 11.
5. Tudo, exceto é a soma 1 + 2 + 3 + 4 = 10.

Dicas: Cuidado com o transbordamento de inteiros! Usar 64 bits Integer.
'''
arr = list(map(int, input().rstrip().split()))
maior = 0
menor = sum(arr)

for i in arr:
	soma = 0
	for j in arr:
		soma += j
	soma -= i

	if(soma > maior):
		maior = soma

	if(menor > soma):
		menor = soma

print(f'{menor} {maior}')