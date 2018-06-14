''' Escrever um programa em linguagem Python que controle as retiradas de dinheiro de um cofre.
    Aluno: Adalberto Marques da Costa.
    E-mail: adalbertonatal@hotmail.com '''
valor_total = int(input("Digite o valor total de retirada do cofre: R$ "))
saque = 0
valor_res = valor_total 
while True:
    n100 =n50 = n20 = n10 = n5 = 0
    saque = int(input("Digite o valor de saque: R$ "))
    print()

    if saque < 0 or saque == 0 :
        exit()
    elif saque > valor_res :
        print("Não é possível sacar este valor!")
        continue

    elif saque %  5 > 0 :
        print("Retirada de R$", saque)
        print("Não é possível sacar este valor!")
        print()
        continue

    while saque >= 100:
        valor_res -= 100
        saque -= 100
        n100 += 1

    while saque >= 50:
        valor_res -= 50
        saque -= 50
        n50 += 1

    while saque >= 20:
        valor_res -= 20
        saque -= 20
        n20 += 1

    while saque >= 10:
        valor_res -= 10
        saque -= 10
        n10 += 1

    while saque >= 5:
        valor_res -= 5
        saque -= 5
        n5 += 1


    print(" Notas sacadas: ")
    print(" R$ 100 - %d"% (n100))
    print(" R$  50 - %d"% (n50))
    print(" R$  20 - %d"% (n20))
    print(" R$  10 - %d"% (n10))
    print(" R$  05 - %d"% (n5))

    print(" Valor restante no cofre: R$ ", valor_res)
    print()
