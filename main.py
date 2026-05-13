
valor_b = 0
valor_l = 0
desconto_v = 0
vendas_realizadas = 0

try:
    while True:

        print("-" * 50)
        print("SISTEMA DE VENDAS")
        print("-" * 50)

        print("1 - Registrar Vendas")
        print("2 - Ver resumo Parcial")
        print("3 - Encerrar Sistema")

        print("-" * 50)

        usuario = int(input("Digite a opção desejada: "))
        print("-" * 50)

        if usuario == 1:
            produto = input("Digite o nome do produto: ")
            valor_u = float(input("Digite o valor unitário do produto: "))
            quant = int(input("Digite a quantidade de produtos vendidos: "))

            
            valor_bruto = valor_u * quant
            valor_b += valor_bruto

            
            if valor_bruto >= 1000:
                desconto = 0.15
                desconto_valor = valor_bruto * desconto
                valor_liquido = valor_bruto - desconto_valor
                desconto_v += desconto_valor
                

                
            if valor_bruto < 1000 and valor_bruto >= 500:
                desconto = 0.10
                desconto_valor = valor_bruto * desconto
                valor_liquido = valor_bruto - desconto_valor
                desconto_v += desconto_valor

                
            if valor_bruto < 500 and valor_bruto >= 100:
                desconto = 0.05
                desconto_valor = valor_bruto * desconto
                valor_liquido = valor_bruto - desconto_valor
                desconto_v += desconto_valor
                
            else: 
                print("Não tem desconto!")

            
            
            valor_l += valor_liquido
            vendas_realizadas += 1

        elif usuario == 2:
            print("-" * 50)
            print("Resumo Parcial")
            print("-" * 50)
            print(f"Total de vendas realizadas: {vendas_realizadas}")
            print(f"Valor Bruto da venda é: R$ {valor_b:.2f}")
            print(f"O desconto aplicado é: {desconto:.2f} %"  )
            print(f"Valor do desconto é: R$ {desconto_v:.2f}")
            print(f"VALOR TOTAL É: R$ {valor_l:.2f}")
            
        elif usuario == 3:
            print("-" * 50)
            print("RESUMO FINAL")
            print("-" * 50)

            print(f"Total de vendas realizadas: {vendas_realizadas}")
            print(f"Valor Bruto da venda é: R$ {valor_b:.2f}")
            print(f"O desconto aplicado é: {desconto:.2f} %"  )
            print(f"Valor do desconto é: R$ {desconto_v:.2f}")
            print(f"VALOR TOTAL É: R$ {valor_l:.2f}")
            
            print("-" * 50)
            print("FIM DO PROGRAMA")

            break

        else:
            print("Opção inválida. Tente novamente")
            print("-" * 50)

except:
    print("Digite um valor válido")






