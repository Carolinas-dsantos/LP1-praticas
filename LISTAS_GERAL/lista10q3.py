class Aluno:
    def __init__(self,nome, mat, notas = {}, situacao = "Em andamento" ):
      self.nome = nome 
      self.mat = mat
      self.notas = notas 
      self.situacao = situacao

    def receber_notas(self, n1, n2, n3):
        self.notas.append(n1)
        self.notas.append(n2)
        self.notas.append(n3)
        print(self.notas)

    def mostrar_notas(self):
        print(f"""
                NOTA1: {self.notas[0]}
                NOTA2: {self.notas[1]}
                NOTA3: {self.notas[2]}
~
              """)

    def calcula_media(self):
        soma = 0
        for i in self.notas:
         soma += i
        media = soma/3
        print(f' Sua média {media:.2f}')

    def definir_situacao(self, media):
        if media >= 7:
          self.situacao = "Aprovado"
          print(self.situacao)
        else:
          self.situacao = "Reprovado"
          print(self.situacao)


a1 = Aluno("Jão", 1234)
a1.receber_notas(3.0, 5.0, 5.0)
a1.mostrar_notas()
a1.calcula_media()
a1.definir_situacao(4.0)