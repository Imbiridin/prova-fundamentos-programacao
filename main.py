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

    if valor_bruto >= 1000:
        desconto = 0.15
        desconto_valor = valor_bruto * desconto
    elif valor_bruto < 1000 or valor_bruto >= 500:
        desconto = 0.10
        desconto_valor = valor_bruto * desconto
    elif valor_bruto < 500 or valor_bruto >= 100:
        desconto = 0.05
        desconto_valor = valor_bruto * desconto
    else: 
        print("Não tem desconto!")

elif usuario == 2:
    print("2- Ver resumo Parcial")
elif usuario == 3:
    print("3 - Encerrar Sistema")


print(f"Valor Bruto da venda é: R$ {valor_bruto:.2f}")
print(f"O desconto aplicado é: {desconto:.2f} %"  )
print(f"Valor do desconto é: R$ {desconto_valor:.2f}")



