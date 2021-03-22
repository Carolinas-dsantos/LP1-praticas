def dic1():
    dicionario01 = {x:x for x in range(0,11)}
    return dicionario01

def dic2():
    dicionario02 ={x:x for x in range(11,21)}
    return dicionario02

def dic3():
    dicionario03 ={x:x for x in range(21,31)}

    return dicionario03
    
def dic_unidas(dic1, dic2, dic3):
    dic1.update(dic2)  #dic1 recebe dic2
    dic1.update(dic3)  #dic1 recebe dic3
    print(dic1)

dic_unidas(dic1(), dic2(), dic3())