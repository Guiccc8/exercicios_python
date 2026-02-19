from random import randint 
NumAleatório = [randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000)]

print("Valores:")

for n in NumAleatório:
    print(n) 

print(":" * 10)

print("Posição do maior valor:", NumAleatório.index(max(NumAleatório)),"-",max(NumAleatório))

print("Posição do menor valor:", NumAleatório.index(min(NumAleatório)),"-",min(NumAleatório))




