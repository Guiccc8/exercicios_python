while True:
    try:
        numero = int(input("Insira um número: "))
        print(f"Os números pares de 0 a {numero}: ")
        for n in range(0, numero+1, 1):
            if n % 2 == 0:
                print(n, end=" ")
        break
    except:
        print("Digite um número inteiro maior que 0.")
print("FIM")
