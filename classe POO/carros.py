class carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def MostrarInfo(self):
        print("marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("ano", self.ano)


marcaCarro = input("marca do seu carro: ")
modeloCarro = input ("modelo do seu carro: ")
anoCarro = input ("ano do seu carro: ")
    
carro1 = carro(marcaCarro, modeloCarro, anoCarro)

carro1.MostrarInfo()