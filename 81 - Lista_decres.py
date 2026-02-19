numeros = []
while True:
    number = input("Digite um valor (aperte 'n' para parar):").lower()
    if number == "n":
        print(numeros)
        print(":"*20)

        if 5 in numeros:
            print("O número 5 está na lista.")

        numeros.sort(reverse=True)

        print(numeros)
        print("Número de valores:", len(numeros))
        break
    numeros.append(int(number))
