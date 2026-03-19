peca1 = str(input("Digite o nome da primeira peça: "))
valorpeca1 = float(input("Digite o valor dessa peça: "))
unidadeP1 = int(input(f"Quantas unidades de {peca1} são requeridas? "))


peca2 = str(input("Digite o nome da segunda peça: "))
valorpeca2 = float(input("Digite o valor da segunda peça: "))
unidadeP2 = int(input(f"Quantas unidades de {peca2} são requeridas? "))

total = (valorpeca1 * unidadeP1) + (valorpeca2 * unidadeP2)
print(total)

