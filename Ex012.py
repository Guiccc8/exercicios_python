palavra = input("Digite a palavra para saber a quantidade de vogais:").lower()
vogais = 'aeiou'
contagemDeVogais = 0
for letra in palavra:
    if letra in  vogais:
        contagemDeVogais += 1
print(f"Na palavra '{palavra}' há {contagemDeVogais} vogais.")