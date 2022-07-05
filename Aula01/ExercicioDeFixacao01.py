import math

raio = float(input("Digite um valor para o raio: "))

comprimento = 2 * math.pi * raio
areaCirculo = math.pi * raio ** 2
volume = 4 / 3 * math.pi * raio ** 3

print(f"\nComprimento da circunferência: {comprimento:.2f}")
print(f"Área da círculo: {areaCirculo:.2f}")
print(f"Volume da esfera: {volume:.2f}")
