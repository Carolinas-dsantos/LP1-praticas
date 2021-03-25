#Questão2. Gere 2 arquivos um contendo múltiplos 5 e o outro com múltiplos de 3 dentro de
#uma range de 0 a 200

with open("multiplos03.txt", "w") as numeros:
    for i in range(0,200):
        if int(i) % 3 == 0:
            numeros.write(f"{i}\n")
           
with open("multiplos05.txt", "w") as numeros:
    for i in range(0,200):
        if int(i) % 5 == 0:
            numeros.write(f"{i}\n")