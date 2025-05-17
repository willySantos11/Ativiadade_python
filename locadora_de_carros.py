opcao = 0
while opcao != 5:
    print("====LOCADORA DE CARROS====")
    print(" ---Veiculos Disponiveis---")
    print("[1] - Fiesta: R$90,00")
    print("[2] - Palio: R$85,00 ")
    print("[3] - Corolla: R$150,00 ")
    print("[4] - Civic: R$180,00")
    print("[5] - Sair...")
    print("Valor por km rodado: R$0,20!")
    
    opcao = int(input("Escolha um veiculo: "))
    
    if opcao == 1:
       dias = int(input("Informe a quantidade de dias que o veiculo será alugado: "))
       kms = float(input("Informe a quantidade de kms a serem rodados:"))
       total = (dias * 90.00) + (kms * 0.20) 
       total_diarias = dias * 90.00
       total_kms = kms * 0.20
       print("===== RECIBO =====")
       print(f"Diarias : {dias} | Valor: R${total_diarias}")
       print(f"Kms rodados: {kms} | Valor: R${total_kms}")
       print(f"O veiculo escolhido ficou um total de: R${total}")
       break
   
    elif opcao == 2:
       dias = int(input("Informe a quantidade de dias que o veiculo será alugado: "))
       kms = float(input("Informe a quantidade de kms a serem rodados:"))
       total = (dias * 85.00) + (kms * 0.20)
       total_diarias = dias * 85.00
       total_kms = kms * 0.20
       print("===== RECIBO =====")
       print(f"Diarias : {dias} | Valor: R${total_diarias}")
       print(f"Kms rodados: {kms} | Valor: R${total_kms}")
       print(f"O veiculo escolhido ficou um total de: R${total}")
       break
   
    elif opcao == 3:
       dias = int(input("Informe a quantidade de dias que o veiculo será alugado: "))
       kms = float(input("Informe a quantidade de kms a serem rodados:"))
       total = (dias * 150.00) + (kms * 0.20)
       total_diarias = dias * 150.00
       total_kms = kms * 0.20
       print("===== RECIBO =====")
       print(f"Diarias : {dias} | Valor: R${total_diarias}")
       print(f"Kms rodados: {kms} | Valor: R${total_kms}")
       print(f"O veiculo escolhido ficou um total de: R${total}")
       break  
   
    elif opcao == 4:
       dias = int(input("Informe a quantidade de dias que o veiculo será alugado: "))
       kms = float(input("Informe a quantidade de kms a serem rodados:"))
       total = (dias * 180.00) + (kms * 0.20)
       total_diarias = dias * 180.00
       total_kms = kms * 0.20
       print("===== RECIBO =====")
       print(f"Diarias : {dias} | Valor: R${total_diarias}")
       print(f"Kms rodados: {kms} | Valor: R${total_kms}")
       print(f"O veiculo escolhido ficou um total de: R${total}")
       break
   
    elif opcao == 5: 
        print("Saindo...")
    else:
        print("OPÇÃO INVALIDA.")
    