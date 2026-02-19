numeros = []

for c in range(1, 4, 1):
    numero = float(input(f'Digite a nota do {c}º bimestre:'))
    numeros.append(numero)

media = sum(numeros)/len(numeros)
if media >= 6.0:
    print(f"O aluno foi aprovado, ele obteve uma média final de {media}.")
else:
    print(f"O aluno foi reprovado, ele obteve uma média final de {media}")