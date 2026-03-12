s1 = "logica de programacao"
s1 = s1 + " e algoritmos"
print (s1)

s1 = 'a' + "-"*10 + 'b'
print (s1)

nota = 6.9

#composicao classica

s1 = "sua nota %.2f" % nota


# composicao moderna

s1 = "nota {}" .format(nota)

# f-string
s1 = f"sua nota {nota} "

# fatiamento, escolher de onde quer começar o texto

s1 = "logica de programacao"
print (s1[0:7])
 
tamanho = len(s1)
print(tamanho)