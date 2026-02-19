frase = input("Digite uma frase:").strip().lower().replace(" ", "")
fraseinvert =   frase[::-1]

if fraseinvert == frase:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
    