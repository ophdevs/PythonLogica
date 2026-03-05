class aluno:
    def __init__(self,nome ,matricula, nota,):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
    
    def mostra_info (self):
        print(f"Nome {self.nome}")
        print(f"Matricula {self.matricula}")
        print(f"Nota: {self.nota}")

cadastro_alunos = []

while True:
    print("-----------------------------------")
    print("1-Cadastrar Aluno")
    print("2-Listar Alunos")
    print("3-Procura por Matricula")
    print("4- Sair")
    print("-----------------------------------")

    try:
        opcao = int(input("Digite sua opcao: "))
    except ValueError:
        print("seu valor esta errado")

    if opcao == 1:

        print ("Cadastro Alunos")
        print ("-----------------------------------")
        nome = input("Nome: ")
        matricula = input("Matricula: ")
        nota = float(input("Nota: "))

        aluno = aluno(nome, matricula, nota)
        cadastro_alunos.append = aluno

    elif opcao == 2:
        print("Listar Alunos")
        print ("-----------------------------------")

        for r in cadastro_alunos :
            r.mostra_info
            print ("-----------------------------------")


    elif opcao == 3:
        print("ola")
    elif opcao == 4:
        break
    
