numeros = []



while True:
    num = input("Digite um valor numérico[Digite 'n' para parar]:")
    if num == "n":
        print(numeros)
        
        for pos, val in enumerate(numeros):
            print(pos, "-", val)
            if numeros.count(val) > 1:
               numeros.pop(pos
               
        break
    numeros.append(int(num))
    
    
print(numeros)
                


        



