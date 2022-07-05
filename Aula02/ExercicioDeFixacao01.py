lista = []

valor = 0
while valor >= 0:
    valor = float(input("Digite um valor: "))
    if valor >= 0:
        lista.append(valor)
    print(lista)
    print(f"Tamanho: {len(lista)}")
