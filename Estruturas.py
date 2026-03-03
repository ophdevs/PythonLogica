numContador = int(input("Digite o número da tabuada: "))
numQuantidade = int(input("Ate qual Numero? "))


for i in range(numQuantidade + 1):  
    resultado = numContador * i
    print(f"{numContador} x {i} = {resultado}")