salario = float(input("Digite seu salário atual: "))

if salario > 1250.00:
    salario = round(salario*1.1,2)
    print("Seu novo salário é R$ ", salario)
else:
    salario = round(salario*1.15,2)
    print("Seu novo salário é R$ ", salario)