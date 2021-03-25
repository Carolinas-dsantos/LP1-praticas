regiões = ('Norte', 'Nordeste', 'Centro_Oeste', 'Sul', 'Sudeste')
estados = ['Amazonas', 'Ceará', 'Mato_Grosso', 'Paraná', 'São_Paulo']
cidades = {'Manaus', 'Maranguape', 'Sinop', 'Maringá', 'São Paulo'}

def junção (regiões,estados,cidades):
    t_estados = tuple(estados)
    t_cidades = tuple(cidades)
    cer_est = (regiões + t_estados)
    lugares = (cer_est + t_cidades)
    elemento_unico = list(lugares)
    print(elemento_unico)

junção(regiões, estados, cidades)