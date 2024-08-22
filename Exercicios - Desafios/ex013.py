salario = float(input("Qual é o valor do salário? : "))
novoSalario = salario + (salario * 15 / 100)

print("O novo salario com acrescimo de 15% é igual a R${:.2f}".format(novoSalario))
