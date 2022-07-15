inicio = input("Digite os 9 dígitos iniciais do CPF: ")
fim = input("Digite os dígitos de controle do CPF: ")
somatorio = 0
for i in range(9):
    somatorio += int(inicio[i]) * (10 - i)
resto = somatorio % 11
if resto >= 2:
    digito1 = 11 - resto
else:
    digito1 = 0
somatorio = 0
for i in range(9):
    somatorio += int(inicio[i]) * (11 - i)
resto = (somatorio + digito1 * 2) % 11
if resto >= 2:
    digito2 = 11 - resto
else:
    digito2 = 0
if digito1 == int(fim[0]) and digito2 == int(fim[1]):
    print("CPF válido")
else:
    print(f"CPF inválido, os dígitos de controle corretos deveriam ser {digito1}{digito2}")
