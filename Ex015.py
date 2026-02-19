def converterParaEuro(dolar):
    return dolar * 0.93

dolares = float(input("Digite o valor em dólares: "))
euro = converterParaEuro(dolares)

print(f"O valor de U${dolares} corresponde a £${euro}.")