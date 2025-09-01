# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
quantidade_cigarros = int(input("Quantidade de cigarros por dia: "))
anos = float(input("Anos que fuma: "))
reducao_minutos = anos * 365 * quantidade_cigarros * 10
print(f"Total de dias perdidos: {reducao_minutos / (24 * 60):.2f} dias.")