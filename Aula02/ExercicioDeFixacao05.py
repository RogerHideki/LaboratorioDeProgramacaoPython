import numpy as np

tam = 50

vetorEntrada = np.zeros(tam)
for i in range(tam):
    vetorEntrada[i] = float(input(f"V[{i + 1}]: "))
vetorMedia = np.array([vetorEntrada.mean()] * tam)
vetorDiferenca = abs(vetorEntrada - vetorMedia)
print(f"O valor existente na lista que mais se aproxima do valor médio é: {vetorEntrada[vetorDiferenca.argmin()]}")
