from random import randint

numero = randint(1, 100)
print("--------JOGO DE ADIVINHAÇÃO-------")
print("Eu pensei em um número de 0 a 100, tente adivinhar!")

numeroDePalpites = 1
pontuacao = 100

while pontuacao > 0:
    try: 
        chute = int(input("Digite seu palpite: "))
        if (chute >= 0 and chute <= 100):
            if chute == numero:
                print(f"Parabéns! Você acertou. O número que eu havia pensado era {numero}. Você conseguiu a pontuação de {pontuacao}.")
                break
            elif chute > numero:
                print(f"Você errou! O número que eu pensei é menor que {chute}.")
                pontuacao -= 10
            elif chute < numero:
                print(f"Você errou! O número que eu pensei é maior que {chute}.")
                pontuacao -= 10
        else: 
            print("Digite um número de 0 a 100.")
    except:
        print("Digite um número inteiro, o qual esteja no intervalo de 0 a 100.")

print("Número pensado: ", numero)