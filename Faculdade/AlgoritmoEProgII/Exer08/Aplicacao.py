from Alunos import Alunos, Colegio, Faculdade

Aluno = Alunos (1, 'Rodrigo', 20200110)
AlunoColeg = Colegio (2, 'Joao', 20200111, 2020)
AlunoFacul = Faculdade (3, 'Joana', 88803, 4)

opcao = "" 
while( opcao != "0" ):
    print("\n----------------------")
    print("1 - Aluno")
    print("2 - Aluno Colegio")
    print("3 - Aluno Faculdade")
    print("0 - Sair")
    print("\n----------------------")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        Aluno.imprimiAluno()
        print ('#'*15)
        break

    if opcao == "2":
        AlunoColeg.imprimirDadosAluno()
        print('#'*15)
        break

    if opcao == "3":
        AlunoFacul.imprimirDadosFacul()
        print('-'*15)
        break

    if opcao == "0":
        print('-' * 15)
        print('ByeBye')
        print('-'*15)
        break

