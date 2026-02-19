
entrada = []
pares = []
for cont in range(1,5):
    x = int(input("Digite um valor(es) do teclado:"))
    entrada.append(x)
    

entrada = tuple(entrada)

print("Valores: ", entrada)

if 9 in entrada:
    print(entrada.count(9), ": Número(s) 9 na lista.")

if 3 in entrada:
    print(entrada.index(3), ": A posição do primeiro 3.")

print("Pares:", end=" ")
for x in entrada:
    if x%2 == 0:
        print(f"{x}", end=" ")


        



