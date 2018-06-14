num=int(input("Digite numero da conta:"))
sal_atual=float(input("digite saoldo atual:"))
op=input("Digite D para deposito ou R para retida:")#op igual a operação
#valor_op=float(input("Digite o valor da opercao:"))
if op=="D"or op=="R":
    valor_op=float(input("Digite o valor da opercao:"))
    if op=="D":
        sal_atual=sal_atual+valor_op
    else:
        sal_atual=sal_atual-valor_op
# declarar o paramento faz a ordem de como ira ser impresso
    print("Novo saldo da conta: {0} R$ {1:.2f}".format(num, sal_atual))

    if sal_atual<0:
        print("Conta estourada!!!")

else:
    print("Operação invalida!!!")
#if sal_atual<0:
 # print(sal_atual,"Conta estourada")
#elif op!="D"or"R":
 # print("Operação invalida!")
#else:
 # print("Saldo:", sal_atual)
