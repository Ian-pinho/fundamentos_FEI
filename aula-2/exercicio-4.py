valor_hora=float(input("Digite valor da hora de trabalho: "))
horas=int(input("Digite o numero de horas trabalhadas no mes: "))

print(f"+ Salario bruto: R$ {valor_hora*horas:.2f}")
print(f"- IR (11%): R$ {valor_hora*horas*0.11:.2f}")
print(f"- INSS (8%): R$ {valor_hora*horas*0.08:.2f}")
print(f"- Sindicato (5%): R$ {valor_hora*horas*0.05:.2f}")
print(f"+ Salario liquido: R$ {(valor_hora*horas)-(valor_hora*horas*0.11)-(valor_hora*horas*0.08)-(valor_hora*horas*0.05):.2f}")