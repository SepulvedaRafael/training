'''
236A - MENINO OU MENINA (BOY OR GIRL)

Naqueles dias, muitos meninos usam fotos de meninas bonitas como avatares em fóruns. Portanto, é muito difícil dizer o sexo de um usuário à primeira vista. No ano passado, nosso herói foi a um fórum e teve uma boa conversa com uma beleza (ele pensou assim). Depois disso, eles conversaram com muita frequência e, eventualmente, se tornaram um casal na rede.

Mas ontem, ele veio ver "ela" no mundo real e descobriu que "ela" é realmente um homem muito forte! Nosso herói está muito triste e ele está cansado demais para amar novamente agora. Então, ele criou uma maneira de reconhecer os gêneros dos usuários por seus nomes de usuário.

Este é o seu método: se o número de caracteres distintos no nome de usuário é ímpar, então ele é um homem, caso contrário, ela é uma mulher. Você recebe a string que denota o nome de usuário, por favor, ajude nosso herói a determinar o sexo desse usuário pelo seu método.

Entrada
A primeira linha contém uma string não vazia, que contém apenas letras minúsculas em inglês — o nome de usuário. Esta string contém no máximo 100 letras.

Saída
Se for uma mulher pelo método do nosso herói, imprima "CONVERSA COM ELA!" (sem as citações), caso contrário, imprima "IGNORA-O!" (sem as citações).

Exemplos
Entrada
wjmzbmr

Saída
CHAT WITH HER!

-----------

Entrada
xiaodao

Saída
IGNORE HIM!

-----------

Entrada
sevenkplus

Saída
CHAT WITH HER!

Nota

Para o primeiro exemplo. Existem 6 personagens diferentes em "wjmzbmr". Esses personagens são: "w", "j", "m", "z", "b", "r". Então wjmzbmr é uma fêmea e você deve imprimir "CHAT WITH HER!".
'''
nome = set(input())

if((len(nome) % 2) == 0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')



