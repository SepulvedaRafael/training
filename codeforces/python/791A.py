'''
791A - URSO E O GRANDE IRMÃO (BEAR AND BIG BROTHER)

Bear Limak quer se tornar o maior dos ursos, ou pelo menos se tornar maior do que seu irmão Bob.

Neste momento, Limak e Bob pesam a e b respectivamente. É garantido que o peso de Limak é menor ou igual ao peso de seu irmão.

Limak come muito e seu peso é triplicado após cada ano, enquanto o peso de Bob é dobrado após cada ano.

Depois de quantos anos completos Limak se tornará estritamente maior (estritamente mais pesado) do que Bob?

Entrada
A única linha da entrada contém dois inteiros a e b (1 ≤ a ≤ b ≤ 10— O peso de Limak e o peso de Bob, respectivamente.

Saída
Imprima um inteiro, denotando o número inteiro de anos após o qual Limak se tornará estritamente maior que Bob.

Exemplos
Entrada
4 7

Saída
2

----------
Entrada
4 9

Saída 
3

----------
Entrada
1 1

Saída
1
'''
x = True
ano = 0
a, b = map(int, input().split())

while x:
    a = a * 3
    b = b * 2
    
    if(a <= b):
        x = True
    else:
        x = False
        
    ano += 1

print(ano)