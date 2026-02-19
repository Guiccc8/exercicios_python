def fatorial(numero):
    while True:
        try:
            fat = 1
            for n in range(numero, 0, -1):
                fat *= n
            return fat
        except ValueError:
            print("Digite um número inteiro maior que 0.")

numero = int(input("Digite um número: "))
fatorial = fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}.")