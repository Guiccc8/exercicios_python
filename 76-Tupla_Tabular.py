produto_preço = "Batata", "Leite", "Uva","Banana", "Picanha", 8, 9, 10, 5, 0
produto = []
preço = []

print("="*20)
print("Lista de preços".center(20))
print("="*20)


for pos, prod in enumerate(produto_preço):

    if pos < len(produto_preço)/2:
        produto.append(prod)
    else:
        preço.append(prod)

preço = tuple(preço)
produto = tuple(produto)


for n in range(0, len(preço)):
    print(produto[n], f"{"."*7}R$ ", preço[n])





