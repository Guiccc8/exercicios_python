while True:
    try:

        euro = int(input("Digite a quantia em questão para a conversão de euro para dólar: U$"))
        dolar = euro*1.08

        print(f"O valor de £${euro} para dólar é U${dolar}.")
        soun = input("Deseja continuar?[S/N]:").lower()
        if soun == "n":
            break
    except:
        print("Valor inválido")