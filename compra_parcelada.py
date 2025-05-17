valor_da_compra = float(input("Informe o valor da compra: "))
resposta = input ("Deseja parcelar (s para sim n para não)? ")
opcao = 0 
while opcao != 4:
    if resposta == "s":
        print ("Escolha uma opção")
    elif resposta == "n":
        print ("Compra Finalizada!")
    else:
        print ("Opção invalida.")        
        
    print ("=== Compra parcelada ===")
    print ("--- opções de parcelamento ---")
    print ("[1] - 2x sem juros")
    print ("[2] - 3x sem juros")
    print ("[3] - 5x sem juros")
    print ("[4] - Finalizar compra")
    
    opcao = int (input(""))
    
    if opcao == 1:
        numero_parcelas = valor_da_compra / 2 
        arredondado = round (numero_parcelas, 2)
        print (f"Sua compra de R${valor_da_compra} foi dividida em 2x de R${arredondado}")
        break
    elif opcao == 2:
        numero_parcelas = valor_da_compra / 3
        arredondado = round (numero_parcelas, 2)
        print (f"Sua compra de R${valor_da_compra} foi dividida em 3x de R${arredondado}")
        break
    elif opcao == 3:
        numero_parcelas = valor_da_compra / 5 
        arredondado = round (numero_parcelas, 2)
        print (f"Sua compra de R${valor_da_compra} foi dividida em 5x de R${arredondado}")
        break
    elif opcao == 4:
        print ("Compra finalizada!")
        break
    else:
        print ("Opção invalida.")