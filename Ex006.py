compras = []
cont = 0
while True:
    cont += 1
    item = input(f"Digite a {cont}° compra do mercado:")
    compras.append(item)
    v = input("Deseja continuar?[S/N]:").lower()

    if v == "n":
        break


print("No seu carrinho de compras teve:")
for compra in compras:
    print(compra)
