numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
            "Doze","Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    val = int(input("Digite um número de 0 a 20:"))
    if   0 >= val or val <= 20:
        print("Número por extenso:",numeros[val])
        break
    
   