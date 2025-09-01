# Função len()
print("-----------------------------------------------")
print(len("A"))
print(len("AB"))
print(len(""))
print(len("O rato roeu a roupa"))
print("-----------------------------------------------")

# Acessar caractere
print("-----------------------------------------------")
a = "ABCDEF"
print(a[0])
print(a[1])
print(a[5])
print("a[6] dá o erro IndexError: string index out of range")
print("-----------------------------------------------")

# Operação com String: Concatenação
print("-----------------------------------------------")
s = "ABC"
print(s + "C")
print(s + "D" * 4)
print("X" + "-" * 20 + "X")
print(s + "x4 = " + s * 4)
print("-----------------------------------------------")

# Operação com String: Composição
print("-----------------------------------------------")
# %d = int | %s = string | %f = float
idade = 22
print("[%d]" % idade)
print("[%03d]" % idade)
print("[%3d]" % idade)
print("[%-3d]" % idade)
print("-----------------------------------------------")
print("%5f" % 5)
print("%5.2f" % 5)
print("%10.5f" % 1000)
print("-----------------------------------------------")
# Usando %
nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))
print("-----------------------------------------------")
# Usando .format()
nome = "João"
idade = 22
grana = 51.34
print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:12} tem {:03} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("-----------------------------------------------")
# Usando f-string
nome = "Joseph"
idade = 33
grana = 123.45
print(f"{nome} tem {idade} anos e R${grana} no bolso.")
print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso.")
print(f"{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso.")
print(f"{nome:<12s} tem {idade:<3} anos e R${grana:5.2f} no bolso.")
print("-----------------------------------------------")

# Operação com String: Fatiamento
print("-----------------------------------------------")
s = "ABCDEFGHI"
print(s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:5])
print(s[1:8])
print(s[:2])
print(s[1:])
print(s[0:-2])
print(s[:])
print(s[-1:])
print(s[-5:7])
print(s[-2:-1])
print("-----------------------------------------------")