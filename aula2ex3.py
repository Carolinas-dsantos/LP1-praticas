def match(pessoa1, pessoa2):
    solteiro='s'
    casado='c'
    if (pessoa1 == solteiro) and (pessoa2 == solteiro):
        return print("Match")
    else:
        return print(" Not Match")


print("S = Solteiro e C = Casado")
pessoa1 = input("Estado Civil=> ") 
pessoa2 = input("Diga o seu Estado Civil=> ")

match(pessoa1,pessoa2)