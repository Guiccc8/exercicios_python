while True:
    try:
        escala = input("Digite a unidade de medida:[C/F]:").lower()
        if escala == "c":
            C = int(input("Digite a temperatura em °C:"))
            F =  (C * 9/5) + 32
            print(f"A temperatura de {C}°C para {F}°F")            
        elif escala == "f":
            F = int(input("Digite a temperatura em °F:"))
            C =  (F -32) * 5/9
            print(f"A temperatura de {F}°F para {C}°C")      
        break
    except ValueError as error:
        print(error)
        print("Digite um valor válido para a escala de temperatura respectiva.")