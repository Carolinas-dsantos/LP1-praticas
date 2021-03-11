#Crie uma função que receba duas strings e retorne True se o número de elementos de uma for igual o da outra , e retorne o número de carateres dela.
#Caso contrário
#Pesquise o método 'len()' na documentação Python.

string1 = ("amor\n")
string2 = ("roma\n")

def tamanho_string(string1, string2):
    if len(string1) == len(string2):
        return True
    else:
        return False

print(tamanho_string(string1, string2))
tamanho_string(string1,string2)