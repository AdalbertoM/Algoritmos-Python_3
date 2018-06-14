nome=(input("Digite nome do funcionario:"))
cat=(input("Digite categoria:"))
sal=float(input("Digite salario:"))
# operador in "ACFH": substitui as varias repetiçoes de or
if cat == "A"or cat =="C"or cat =="F"or cat =="H":
    sal=sal*1.10
    print(nome, cat, "{0:.2f}".format(sal))
elif cat == "B"or cat =="D"or cat =="E"or cat =="I"or cat =="J"or cat =="T":
    sal=sal*1.15
    print(nome, cat, "{0:.2f}".format(sal))
elif cat == "K"or cat =="R":
    sal=sal*1.25
    print(nome, cat, "{0:.2f}".format(sal))
elif cat == "L"or cat =="M"or cat =="N"or cat =="O"or cat =="P"or cat =="Q"or cat =="S":
    sal=sal*1.35
    print(nome, cat, "{0:.2f}".format(sal))
elif cat == "U"or cat =="V"or cat =="X"or cat =="Y"or cat =="W"or cat =="Z":
    sal=sal*1.50
    print(nome, cat, "{0:.2f}".format(sal))
