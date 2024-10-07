'''
1043 - TRIÂNGULO

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''
A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if abs(B-C) < A < (B+C):
	perimetro = A + B + C
	print(f"Perimetro = {perimetro:.1f}")
elif abs(A-C) < B < (A+C):
	perimetro = A + B + C
	print(f"Perimetro = {perimetro:.1f}")
elif abs(A-B) < C < (A+B):
	perimetro = A + B + C
	print(f"Perimetro = {perimetro:.1f}")
else:
	area = ((A+B) * C) / 2
	print(f"Area = {area:.1f}")