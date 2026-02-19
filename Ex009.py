while True:
    try:
        print(''' Escolhas:
        [1]: Adição
        [2]: Subtração
        [3]: Multiplicação
        [4]: Divisão''')
        n = input("Digite qual deseja:")
        if n == "1":
            n1 = int(input("Digite o primeiro número:"))
            n2 = int(input("Digite o segundo número:"))

            soma = n1 + n2
            print("O valor da soma foi de", soma)

        elif n == "2":
            n1 = int(input("Digite o primeiro número:"))
            n2 = int(input("Digite o segundo número:"))

            diferenca = n1 - n2
            print("O valor da diferença foi de", diferenca)

        elif n == "3":
            n1 = int(input("Digite o primeiro número:"))
            n2 = int(input("Digite o segundo número:"))

            multiplicação = n1 * n2
            print("O valor da multiplicação foi de", multiplicação)


        elif n == "4":
            n1 = int(input("Digite o primeiro número:"))
            n2 = int(input("Digite o segundo número:"))

            divisao = n1/n2
            print("O valor da divisão foi de", divisao)
        
        escolha = str(input("Deseja continuar [S/N]?")).lower()
        if escolha == 'n':
            break
    except:
            print("Digite o número inteiro.")