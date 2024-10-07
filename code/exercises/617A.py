'''
617A - ELEFANTE (ELEPHANT)

Um elefante decidiu visitar seu amigo. Descobriu-se que a casa do elefante está localizada no ponto 0 e a casa de seu amigo está localizada no ponto x(x > 0) da linha coordenada. Em um passo, o elefante pode se mover 1 2 3 4 ou 5 posições para a frente. Determine, qual é o número mínimo de passos que ele precisa fazer para chegar à casa de seu amigo.

Entrada
A primeira linha da entrada contém um inteiro x (1 ≤ x ≤ 1 000 000) — A coordenada da casa do amigo.

Saída
Imprima o número mínimo de passos que o elefante precisa fazer para chegar do ponto 0 apontar x.

Exemplos
Entrada
5

Saída
1

------------
Entrada
12

Saída
3

Nota
Na primeira amostra, o elefante precisa dar um passo de comprimento 5 para chegar ao ponto x.

Na segunda amostra, o elefante pode chegar ao ponto x se ele passar 3 5 e 4. Existem outras maneiras de obter a resposta ideal, mas o elefante não pode alcançar x em menos de três movimentos.
'''
passos = 0
y = True

x = int(input())

while y:
	if(x > 0):
		for i in range(5, 1, -1):
			num = x // i
			if(x != 0):
				passos += num

				if(x / i > 0 and x / i < 1):
					passos += 1
					y = False
					break
			else:
				y = False
				break
			x = x % i

print(passos)