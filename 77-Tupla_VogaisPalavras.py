Escrito = input("Digite uma palavra (não frase):").lower()
Vogais = []
Escrito=Escrito.replace("", " ")
Escrito = Escrito.split()

for letra in Escrito:

    if letra in "aeiou" :
        Vogais.append(letra)
Vogais = sorted(Vogais)

Vogais = tuple(Vogais)

print("Vogais:", end="")

for vogal in Vogais:
    print(vogal, end=" ")
    


