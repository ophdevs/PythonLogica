class Biblioteca:
    def __init__(self, titulo, autor, numPaginas):
        self.titulo = titulo
        self.autor = autor
        self.numPaginas = numPaginas

    def Mostrar_Livro(self):
        print(f"titulo: {self.titulo}")
        print (f"Autor: {self.autor}")
        print(f"Numero de Paginas: {self.numPaginas}")

lista_livros = []

while (True):

    try: 
        titulo = input("digite o titulo: ")
        autor = input("digite o autor: ")
        numPaginas = int(input("digite o numero de paginas: "))

        livro = Biblioteca(titulo, autor, numPaginas)
        lista_livros.append(livro)

    except:
        print("erro na digitacao")

    
