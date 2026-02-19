while True:
    try:
        número = int(input("Digite um número para saber se é par ou impar:"))

        if número%2 == 0:
            print(f"O número {número} em questão, é par.")

        else:
            print(f"O número {número} em questão, é ímpar.")

        soun = input("Deseja continuar?[S/N]:").lower()
        if soun == "n":
            break

    except:
        print("Valor inválido")