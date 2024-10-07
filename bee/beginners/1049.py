'''
1049 - ANIMAL

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

	VERTEBRADO = AVE > CARNIVORO = AGUIA
				     > ONIVORO = POMBA

			   = MAMIFERO > ONIVORO = HOMEM
			   			  > HERBIVORO = VACA

	INVERTEBRADO = INSETO > HEMATOFAGO = PULGA
						  > HERBIVORO = LAGARTA

			     = ANELIDEO > HEMATOFAGO = SANGUESSUGA
				 			> ONIVORO = MINHOCA

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''
grupo = input()
classe = input()
habito = input()

if (grupo == 'vertebrado'):
	if(classe == 'ave'):
		if(habito == 'carnivoro'):
			print("aguia")
		else:
			print("pomba")
	else:
		if(habito == 'onivoro'):
			print("homem")
		else:
			print("vaca")

else:
	if(classe == 'inseto'):
		if(habito == 'hematofago'):
			print("pulga")
		else:
			print("lagarta")
	else:
		if(habito == 'hematofago'):
			print("sanguessuga")
		else:
			print("minhoca")