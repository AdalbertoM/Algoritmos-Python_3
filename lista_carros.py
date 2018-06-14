Nomes_carros = []
menu = True
while menu:
    print()
    print("""Menu lista de carros

1.Cadastrar novos carros.
2.Consultar carros.
3.inserção de carros.
4.Excluir carro.
5.Sair """)
    print()

    menu = input("escolha uma opção: ")
    print()

    while menu == "1":
        N = int(input("Digite a quantidade de carros: "))
        for i in range(N):
            nomes = (input("Digite o nome do carro: "))
            Nomes_carros.append(nomes)
        if i == N-1:
            op = input("Deseja Continuar com o Cadastro? (S/N): ")
            print()
            if op == "S":
                menu == "1"
            else:
                break
    while menu == "2":
        N = int(input("Digite a quantidade de carros: "))
        for i in range(N):
            nomes = (input("Digite o nome do carro: "))
            if nomes in Nomes_carros:
                print(nomes)
            else:
                print("Carro não Cadastrado")
        if i == N-1:
            op = input("Deseja Continuar com a consulta? (S/N): ")
            print()
            if op == "S":
                menu == "2"
            else:
                break
    while menu == "3":
        N = int(input("Digite a quantidade de carros: "))
        if len(Nomes_carros) == 10:
            print("Não há espaço para gravar o novo carro! ")
            break
        for j in range(N):
            i = int(input("Digite a posição na lista: "))
            nomes = (input("Digite o nome do carro: "))
            Nomes_carros.insert(i, nomes)
        if j == N-1:
            op = input("Deseja Continuar com a inserção? (S/N): ")
            print()
            if op == "S":
                menu == "3"
            else:
                break
    while menu == "4":
        N = int(input("Digite a quantidade de carros: "))
        for i in range(N):
            nomes = (input("Digite o nome do carro: "))
        if nomes in Nomes_carros:
            Nomes_carros.remove(nomes)
        else:
            print("Carro não Cadastrado")
        if i == N-1:
            op = input("Deseja Continuar com a exclusão de carros? (S/N): ")
            print()
            if op == "S":
                menu == "4"
            else:
                break
    if menu == "5":
        exit()
