from random import randint 
NumAleatório = []

#É possível criar um novo valores com input dentro da tupla : (input("Digite algo:"))


print("Números aleatórios:", end=" ")


for n in range(0, 5):
     x = randint(0, 1000)
     NumAleatório.append(x)
NumAleatório = tuple(NumAleatório) #transforma uma lista em tupla
'''NumAleatório = list(NumAleatório)''' #transforma uma lista em tupla

print(NumAleatório)
print(":"*20)
print("Maior valor:",max(NumAleatório)) #valor máximo
print(":"*20)
print("Menor valor:",min(NumAleatório)) #valor mínimo
 






   
