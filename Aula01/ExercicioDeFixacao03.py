valor = float(input("Digite o valor de um produto: R$ "))

print("\nCódigo | Desconto (em %)  | Condição")
print("  33   |        10        | Qualquer valor")
print("  77   |        20        | Qualquer valor")
print(" 230   |        30        | Valor do produto maior que R$100,00")
print(" 230   |        25        | Caso contrário")

codigo = int(input("\nDigite um código de desconto: "))

if codigo == 33:
    valor = valor * 0.90
elif codigo == 77:
    valor = valor * 0.80
elif codigo == 230:
    if valor > 100:
        valor = valor * 0.70
    else:
        valor = valor * 0.75
else:
    print("\nDesconto inválido")

print(f"\nValor do produto: R$ {valor:.2f}")
