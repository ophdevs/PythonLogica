numContador = int(input("Digite o número da tabuada: "))
numQuantidade = int(input("Ate qual Numero? "))
contador = 0

print("repeticao usando for (laço)")

for i in range(numQuantidade + 1):  
    resultado = numContador * i
    print(f"{numContador} x {i} = {resultado}")


print ("Repeticao usando while")
print ("---------------------------------")
while  contador < numQuantidade :
    resultado2 = numContador * contador
    contador = contador + 1
    print(f"{numContador} x {contador} = {resultado2}")