vendas = float(input("Total de vendas do funcionario\n"))

salario=2.200
def bonus_salario(vendas, nome='Carolina'): 
    global salario
    if vendas > 800.00:
        salario +=  1.600
        print(f"{nome} você irá receber {salario}")
    else:
        print(f"{nome} você irá receber {salario}")

bonus_salario(vendas)