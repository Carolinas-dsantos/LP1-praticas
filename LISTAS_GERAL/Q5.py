nome="Carolina"

def estrutura(nome):
    dic = {x : [x for x in range(7) ] for x in nome}   
   
estrutura(nome) 

lista_vogais=['A','E','I','O','U'] # o upper dentro do for desobriga a referencia aki de minpusculas
def vogais(nome,lista_vogais):
    for i in nome:
        if i.upper() in lista_vogais:
            print(i, end =" -") # o end = permite que os intens sejam mostrados na mesma linha

vogais(nome,lista_vogais)
print("\n")
def numeros(nome):
    
    dic = {x : [x for x in range(7) ] for x in nome} 
    for k in dic.values(): # Percorre apenas os valores
      for i in k:  # Percorre as listas (valores)
        if i % 2 == 0:
          print(i, end = "- ")
    

numeros(nome)