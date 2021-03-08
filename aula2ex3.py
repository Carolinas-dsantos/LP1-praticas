def match(pessoa1, pessoa2):
    solteiro='s'
    casado='c'
    if (pessoa1 == solteiro) and (pessoa2 == solteiro):
        return print("Matchados")
    else:
        return print("Próximo")


print("s = solteiro e c = casado")
pessoa1 = input("Estado Civil=> ") 
pessoa2 = input("Diga o seu Estado Civil=> ")

match(pessoa1,pessoa2)