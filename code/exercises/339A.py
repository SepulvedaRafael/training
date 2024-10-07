'''
339A - MATEMÁTICA ÚTIL (HELPFUL MATHS)

Xenia, a matemática iniciante, é uma estudante do terceiro ano do ensino fundamental. Ela agora está aprendendo a operação de adição.

O professor escreveu a soma de vários números. Os alunos devem calcular a soma. Para facilitar o cálculo, a soma contém apenas os números 1, 2 e 3. Ainda assim, isso não é suficiente para a Xenia. Ela está apenas começando a contar, então ela pode calcular uma soma somente se os summands seguirem em ordem não decrescente. Por exemplo, ela não pode calcular a soma 1+3+2+1, mas pode calcular as somas 1+1+2 e 3+3.

Você tem a soma que foi escrita no quadro. Reorganize os somatórios e imprima a soma de tal forma que Xenia possa calcular a soma.

Entrada
A primeira linha contém uma string não vazia s — a soma Xenia precisa de contar. Cordas s não contém espaços. Ele contém apenas dígitos e caracteres "+". Além disso, corda s é uma soma correta dos números 1, 2 e 3. Cordas s tem no máximo 100 caracteres.

Saída
Imprimir a nova soma que Xenia pode contar.

Exemplos
Entrada
3+2+1

Saída
1+2+3

-----------

Entrada
1+1+3+1+3
Saída
1+1+1+3+3

-----------

Entrada
2
Saída
2
'''
aux = 0
numeros = []

soma = input().strip()
soma = list(soma)

for i in soma:
	if(i != '+'):
		numeros.append(int(i))

numeros.sort()
for j in numeros:
	if(aux == len(numeros)-1):
		print(j)
	else:
		print(j, end="+")
	aux += 1