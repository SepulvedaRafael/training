'''
HR011 - Grading Students
A HackerLand University tem a seguinte política de classificação:
- Cada aluno recebe uma grade na faixa inclusiva de 0 para 100.
- Qualquer grade menor que 40 é uma nota baixa.

Sam é professor na universidade e gosta de reunir cada aluno grade de acordo com estas regras:
- Se a diferença entre a grade e o próximo múltiplo de 5 é menor que 3, redondo grade até o próximo múltiplo de 5.
- Se o valor de grade é menor que 38, não ocorre arredondamento, pois o resultado ainda será uma nota baixa.

Exemplos
- grade = 84 arredondado para 85 (85 - 84 é menor que 3)
- grade = 29 não arredonda (resultado é menor que 40)
- grade = 57 não arredonda (60 - 57 é 3 ou maior)

Dado o valor inicial de grade para cada um de Sam n alunos, escrevam código para automatizar o processo de arredondamento.

Descrição da função
Complete a função gradingStudents no editor abaixo.

gradingStudents tem o(s) seguinte(s) parâmetro(s):
int grades[n] : as notas antes do arredondamento

Retorna
int[n] : as notas após arredondamento conforme apropriado

Formato de entrada
A primeira linha contém um único inteiro, n, o número de alunos.
Cada linha i do n as linhas subsequentes contêm um único inteiro,grade[i].

Restrições
1 <= n <= 60
0 <= grades[i] <= 100

Entrada de amostra 0
4
73
67
38
33

Saída de amostra 0
75
67
40
33

Explicação 0

+------+----------------+-------------+
|  ID  | Original Grade | Final Grade |
+------+----------------+-------------+
|  01  |       73       |      75     |
+------+----------------+-------------+
|  02  |       67       |      67     |
+------+----------------+-------------+
|  03  |       38       |      40     |
+------+----------------+-------------+
|  04  |       33       |      33     |
+------+----------------+-------------+

1. Estudante 1 recebeu um 73, e o próximo múltiplo de 73 é 75. Desde 75 - 73 < 3, a nota do aluno é arredondada para 75.
2. Estudante 2 recebeu um 67, e o próximo múltiplo de 67 é 70. Desde 70 - 67 = 3, a nota não será modificada e a nota final do aluno será 67.
3. Estudante 3 recebeu um 38, e o próximo múltiplo de 38 é 40. Desde 40 - 38 < 3, a nota do aluno será arredondada para 40.
4. Estudante 4 recebeu uma nota abaixo 33, portanto a nota não será modificada e a nota final do aluno será 33.
'''
grades_count = int(input().strip())
grades = []

for i in range(grades_count):
	grades_item = int(input().strip())

	if((grades_item % 5) != 0):
		j = 0
		while((grades_item % 5) != 0):
			grades_item += 1
			j += 1

		if(j < 3 and grades_item >= 40):
			grades.append(grades_item)
		else:
			grades.append(grades_item - j)
	else:
		grades.append(grades_item)

for j in grades:
	print(j)