class Requisicao:
    def __init__(self, numero,recebidor,entregador,data):
        self.numero = numero
        self.recebidor = recebidor
        self.entregador = entregador
        self.data = data

    def Mostrar_Info (self):
        print(f"numero: {self.numero}")
        print(f"recebidor: {self.recebidor}")
        print(f"entregador: {self.entregador}")
        print(f"data: {self.data}")

lista_requisicoes = []
condicao = True

while condicao:

    continuar = 's'

    if(continuar.lower != 's'):

        try:
            print("-----------------------------------")
            numero = int(input("Numero Req: "))
            recebidor = input("Quem Recebeu: ")
            entregador = input("Quem Entregou: ")
            data = input("Data de entrega: ")
            print("-----------------------------------") 

            req = Requisicao(numero,recebidor,entregador,data)
            lista_requisicoes.append(req)

            continuar = input("deseja continuar? s/n ")
            if (continuar == 's'):
                continue
            else:
                condicao = False



        except:
            print("erro de digitacao")
            continuar = input("Deseja Continuar? s/n")

            if continuar.lower() == 's':
                continue
            else:
                condicao = False


print("\nREQUISICOES CADASTRADAS\n")

for r in lista_requisicoes:
    print("------------------------")
    print()
    r.Mostrar_Info()
    print("------------------------")
