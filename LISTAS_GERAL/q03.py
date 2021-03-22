#Escreva uma função que receba uma lista com itens repetidos e retorne a
# mesma lista com itens únicos

lista = [1,3,3,7,9,0,0,0,10,4,4,6,6]

def remove_repetidos(lista):
    lista2=[]
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    print(lista2)

remove_repetidos(lista)