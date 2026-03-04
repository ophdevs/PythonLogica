class Carro:
    def __init__(self, marca, modelo, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def Mostrar_Info(self):
        print("marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("ano", self.ano)


marcaCarro = input("marca do seu carro: ")
modeloCarro = input ("modelo do seu carro: ")
anoCarro = input ("ano do seu carro: ")
    
carro1 = Carro(marcaCarro, modeloCarro, anoCarro)

carro1.Mostrar_Info()