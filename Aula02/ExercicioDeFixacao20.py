import numpy as np

tam = 3

listaAlturas = []
listaAlturasMulheres = []
listaNotasMulheres = []
listaNotasHomens = []
dicionarioAnosNascimentos = {}


for i in range(tam):
    altura = float(input('Altura: '))
    nota = float(input('Nota: '))
    anoNascimento = int(input('Ano de nascimento: '))
    sexo = input('Código do sexo ("M" ou "F"): ')
    listaAlturas.append(altura)
    dicionarioAnosNascimentos = {}
    if sexo == 'F':
        listaAlturasMulheres.append(altura)
        listaNotasMulheres.append(nota)
    else:
        listaNotasHomens.append(nota)
vetorAlturas = np.array(listaAlturas)
print(f'Maior altura da turma: {vetorAlturas.max()}')
print(f'Menor altura da turma: {vetorAlturas.max()}')
print(f'Quantidade de mulheres com altura acima da média das alturas das mulheres:')
print(f'Quantidade de homens com nota inferior a média das notas das mulheres:')
print(f'Percentual de pessoas que nasceram em cada ano inserido: ')