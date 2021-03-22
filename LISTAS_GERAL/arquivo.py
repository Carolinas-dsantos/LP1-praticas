arquivo2 = open("numero.txt", "W")

for linha in range(1, 101):

arquivo2.write(f"{linha}\n")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
       
       arquivo2.write(f"{nome}\n")
       arquivo2.write(f"{idade}\n")
        arquivo2.close()
"""