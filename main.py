print("-" * 50)
print("SISTEMA DE VENDAS")
print("-" * 50)

print("1 - Registrar Vendas")
print("2- Ver resumo Parcial")
print("3 - Encerrar Sistema")

print("-" * 50)

usuario = int(input("Digite a opção desejada: "))

if usuario == 1:
    produto = input("Digite o nome do produto: ")
    valor_u = float(input("Digite o valor unitário do produto: "))
    quant = int(input("Digite a quantidade de produtos vendidos: "))

    
    valor_bruto = valor_u * quant

elif usuario == 2:
    print("2- Ver resumo Parcial")
elif usuario == 3:
    print("3 - Encerrar Sistema")


print("Valor Bruto da venda é: " , valor_bruto)


