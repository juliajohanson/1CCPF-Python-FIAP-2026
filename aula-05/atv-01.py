nomes = ["leo", "ju", "caio", "ana"]
for i in range(len(nomes)): #lens é capaz de fazer o range se 'adaptar' ao formato de uma lista ja existente

    for j in range(i+1, len(nomes)):

        print(f"{nomes[i]} e {nomes[j]} são uma dupla")