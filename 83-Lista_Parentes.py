expressao = input("Digite uma expressão:")
expressao = expressao.replace("", " ")
aberto = 0
fechado = 0
expressao = expressao.split()


for val in expressao:
    if val == "(":
        aberto += 1
    elif val == ")":
        fechado += 1
if aberto == fechado:
    print("A expressão está correta.")

else:
    print("A expressão está incorreta.")



