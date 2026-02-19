numeros = []
pares = []
impares = []
while True:
    number = input("Digite um valor (aperte 'n' para parar):").lower()
    if number == "n":
        print(numeros)
        print(":"*20)
        for  val in numeros:
            if val%2 == 0:
                pares.append(val)
            else:
                impares.append(val)
        break
    numeros.append(int(number))


    
        

print("Números totais:",numeros)
print(":"*20)

print("Números pares", pares)
print(":"*20)

print("Números impares", impares)

