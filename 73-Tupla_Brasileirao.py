times = "Bota Fogo", "Palmeiras", "Flamengo", "Bahia", "São Paulo", "Cruzeiro", "Fortaleza","Athletico-PR", "Bragantino", "Atlético-MG", "Vasco da Gama", "Internacional", "Juventude", "Criciúma", "EC Vitória", "Cuiabá", "Corinthians", "Grêmio", "Atlético-GO", "Fluminense"


#1°

print(":"*20)
print("Os principais:")
for pos in range(1, 6):

    print(pos, "-", times[pos])
print(":"*20)
    

#2°
print("Os últimos:")
for pos in range(0, 20):
    
        if pos >= 16:
            print(pos+1, "-", times[pos])
print(":"*20)

#3°
print("Ordem alfabética:")
for pos, time in enumerate(sorted(times)):
     print(pos+1, "-", time), 
print(":"*20)

#4°

if "Chapecoense" in times:
     print(times.index("Chapecoense"))
    
else:
     print("Chapecoense não está no placar. Série B, kkkk.")
     




   
