'''
HR006 - Plus Minus
Dada uma matriz de inteiros, calcule as proporções de seus elementos que são positivo negativo, e zero. Imprima o valor decimal de cada fração em uma nova linha com locais após o decimal.

Nota: Este desafio introduz problemas de precisão. Os casos de teste são dimensionados para seis casas decimais, embora as respostas com erro absoluto de até são aceitáveis.

Exemplo
arr = [1, 1, 0, -1, -1]
Existem n = 5 elementos, dois positivos, dois negativos e um zero. Suas proporções são 2/5 = 0.400000, 2/5 = 0.400000 e 1/5 = 0.200000. Os resultados são impressos como:
	0.400000
	0.400000
	0.200000

Descrição da Função
Completar o plusMinus função no editor abaixo.

plusMinus tem o seguinte parâmetro(s):
int arr[n]: uma matriz de inteiros

Imprimir
Imprima as proporções de valores positivos, negativos e zero na matriz. Cada valor deve ser impresso em uma linha separada com dígitos após o decimal. A função não deve retornar um valor.

Formato de Entrada
A primeira linha contém um número inteiro , o tamanho da matriz.
A segunda linha contém inteiros separados por espaço que descrevem .

Restrições
0 < n <= 100
-100 <= arr[i] <= 100

Formato de Saída
Imprimir o seguinte linhas, cada uma para decimais:
1. proporção de valores positivos
2. proporção de valores negativos
3. proporção de zeros

Entrada de Amostra
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Saída da Amostra
0.500000
0.333333
0.166667

Explicação
Existem 3 números positivos, 2 números negativos e 1 zero na matriz.
As proporções de ocorrência são positivas: 3/6 = 0.5000000, negativo: 2/6 = 0.333333 e zeros: 1/6 = 0.166667.
'''
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

pos = 0
neg = 0
zero = 0

for i in arr:
	if(i > 0):
		pos += 1
	elif(i == 0):
		zero += 1
	else:
		neg += 1

print(f'{pos/n:.6f}')
print(f'{neg/n:.6f}')
print(f'{zero/n:.6f}')