salario = float(input())

def calc(salario, porcentagem):
    aumento = (salario * porcentagem) / 100
    novo_salario = salario + aumento
    
    return f"Novo salario: {(novo_salario):.2f}\n Reajuste ganho: {aumento:.2f}\n Em percentual: {porcentagem} %"

if salario <= 600.00:
    print(calc(salario, 17))
elif salario >= 600.01 and salario <= 900.00:
    print(calc(salario, 13))
elif salario >= 900.01 and salario <= 1500.00:
    print(calc(salario, 12))
elif salario >= 1500.01 and salario <= 2000.00:
    print(calc(salario, 10))
else:
    print(calc(salario, 5))