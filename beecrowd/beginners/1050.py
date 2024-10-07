'''
1050 - DDD

Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

		+---------+-------------------+
		|	DDD	  |	  Destination     |
		|	61	  |	  Brasilia        |
		|	71	  |	  Salvador        |
		|	11	  |	  Sao Paulo       |
		|	21	  |	  Rio de Janeiro  |
		|	32	  |	  Juiz de Fora    |
		|	19	  |	  Campinas        |
		|	27	  |	  Vitoria         |
		|	31	  |	  Belo Horizonte  |
	    +---------+-------------------+

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.
'''
ddd = int(input())

match ddd:
    case 11:
        print('Sao Paulo')
    case 19:
        print('Campinas')
    case 21:
        print('Rio de Janeiro')
    case 27:
        print('Vitoria')
    case 31:
        print('Belo Horizonte')
    case 32:
        print('Juiz de Fora')
    case 61:
        print('Brasilia')
    case 71:
        print('Salvador')
    case default:
        print("DDD nao cadastrado")
