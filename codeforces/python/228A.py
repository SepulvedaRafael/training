'''
228A - SUA FERRADURA ESTÁ NO OUTRO CASCO? (IS YOUR HORSESHOE ON THE OTHER HOOF?)

Valera, o Cavalo, vai à festa com os amigos. Ele vem seguindo as tendências da moda há algum tempo e sabe que é muito popular usar todas as ferraduras de cores diferentes. Valera tem quatro ferraduras restantes do ano passado, mas talvez algumas delas tenham a mesma cor. Nesse caso, ele precisa ir à loja e comprar mais algumas ferraduras, para não perder a cara na frente de seus camaradas estilosos.

Felizmente, a loja vende ferraduras de todas as cores sob o sol e Valera tem dinheiro suficiente para comprar quatro delas. No entanto, para economizar dinheiro, ele gostaria de gastar o mínimo possível, então você precisa ajudar Valera e determinar qual é o número mínimo de ferraduras que ele precisa comprar para usar quatro ferraduras de cores diferentes em uma festa.

Entrada
A primeira linha contém quatro inteiros separados por espaços s 1 ,  s 2 ,  s 3 ,  s 4 (1 ≤  s 1 ,  s 2 ,  s 3 ,  s 4  ≤ 10 9 ) — as cores das ferraduras que Valera tem.

Considere todas as cores possíveis indexadas com números inteiros.

Saída
Imprima um único inteiro — o número mínimo de ferraduras que Valera precisa comprar.

Exemplos
Entrada
1 7 3 3

Saída
1

-------------
Entrada
7 7 7 7

Saída
3
'''
contador = 0
cores = list(map(int, input().rstrip().split()))

for i in range(len(cores) - 1):
	if(cores[i] != cores[i+1]):
		num = i
		for j in range(num, len(cores) - 1):
			if(cores[i] == cores[j + 1]):
				contador += 1
	else:
		contador += 1
print(contador)