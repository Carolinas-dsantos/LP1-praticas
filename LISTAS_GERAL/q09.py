lista = [x for x in range(1,11)]
def par(lista,par):
   for x in range(len(lista)):
       if lista[x] % 2 == 0:
           lista[x] = par
   print(lista)

par(lista,'Par')