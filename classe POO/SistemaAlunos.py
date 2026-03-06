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
        print("Valor incorreto!")

    if opcao == 1:

        condicao = True

        while condicao:
            print ("Cadastro Alunos")
            print ("-----------------------------------")
            nome = input("Nome: ")
            matricula = input("Matricula: ")
            nota = float(input("Nota: "))

            alun = aluno(nome, matricula, nota)
            cadastro_alunos.append (alun)

            try: 
                opcaoLista = input("Deseja continuar: s/n ")
            except ValueError:
                print("Valor incorreto! ")

            if (opcaoLista.lower == 's'):
                continue
            elif (opcaoLista.lower == 'n'):
                condicao = False
            else:
                print("Valor incorreto! ")
                continue

    elif opcao == 2:
            print("Listar Alunos")
            print ("-----------------------------------")

            for r in cadastro_alunos :
                r.mostra_info()

    elif opcao == 3:
        print("ola")

    elif opcao == 4:
        break
    