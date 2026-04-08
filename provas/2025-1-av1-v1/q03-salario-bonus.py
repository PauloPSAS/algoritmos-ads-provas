salario_fixo = float(input("Informar qual é o salário fixo do vendedor: R$"))
total_de_vendas = float(input("Informar o total de vendas do vendedor esse mês: R$"))

acrescimo = total_de_vendas * 20 / 100

print(f"Salário do vendedor: R${salario_fixo:.2f}")
print(f"Vendas efetuadas no mês: R${total_de_vendas:.2f}")
print(f"Acréscimo de 20% das vendas à incluir no salário: R${acrescimo}")
print(f"Salário com acrescimo de 20% pelo total de vendas: R${salario_fixo + acrescimo}")
