#Carolina Silva dos Santos
#Atendente Lanchonete

class Prato:                                   # Inicializando classe prato
    def init(self, comida, bebida):             # Método para instanciar os atributos comida e bebida
        self.comida = comida
        self.bebida = bebida

    def fazer_pedido(self):                         # Método para fazer o pedido 
        self.comida = print("O que vai comer: ")
        self.bebida = print("O que vai beber: ")

class Cliente:                                        # Inicializando classe cliente 
    def init(self, nomeCliente):                       # Método para instanciar o atributo nomeCliente
        self.nomeCliente = nomeCliente

    def cadastrar(self):                              # Método para cadastrar cliente
        self.nomeCliente = input("Digite seu nome: ")

    def fazer_pedido(self):                             # Método para o cliente fazer seu pedidio 
        self.comida = input("O que vai comer: ")
        self.bebida = input("O que vai beber: ")

class Atendente:                                   # Inicializando classe atendente
    def init(self, nome, taxaDeServico):            # método para instanciar os atributos nome e taxaDeServico
        self.nome = nome
        self.taxaDeServico = taxaDeServico


    def comissão(self):                             # método para comissão da atendente
        self.taxaDeServico = "5%"
        print("Será cobrado 5% como taxa de serviço !")

    def atender(self):                                  # método para atendimento
        self.nome = "Carol"
        print(f'Olá meu nome é {self.nome} e irei te atender! ')


class Lanchonete(Prato, Atendente, Cliente):        # classe pai, inicializando classe Lanchonete 
    def init(comida, bebida, nome, nomeCliente, taxaDeServico):     # método para instanciar os atributos comida, bebida, nomeCliente, taxaDeServico
        super()._init_(comida, bebida, nome, nomeCliente, taxaDeServico)
        self.comida = comida
        self.bebida = bebida
        self.nome = nome
        self.nomeCliente = nomeCliente
        self.taxaDeServico = taxaDeServico

    def mostrar_fatura(self):                           # método para finalizar valor total do pedido do cliente 
        self.cadastrar()
        self.comissão()
        print("------ fatura-----")
        print("Nome do cliente: " + self.nomeCliente)
        print("Taxa de Serviço: " + self.taxaDeServico)
        


carol = Atendente()     # objeto carol para acessar a classe atendente
carol.atender()         # método para o objeto carol poder acessar a classe atendente para atender o cliente
pizza = Prato()         # objeto pizza para acessar a classe prato
joao = Cliente()        # objeto joao para acessar a classe cliente
joao.fazer_pedido()     # método para o objeto joao poder acessar a classe cliente e fazer pedido
s1 = Lanchonete()       # objeto s1 para acessar a classe lanchonete
s1.mostrar_fatura()     # método para o obeto s1 acessar a classe lanchonete e mostrar o valor total da fatura