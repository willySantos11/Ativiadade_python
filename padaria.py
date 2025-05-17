opcao = 0
frances = 0
integral = 0
doce_liso = 0
doce_farofa = 0
forma = 0

valor_frances = 0
valor_integral = 0
valor_doce_liso = 0
valor_doce_farofa = 0
valor_forma = 0
# Valor unitário de cada pão  
valor_unidade_frances = 1.04
valor_unidade_integral = 1.04
valor_unidade_doce_liso = 1.08
valor_unidade_doce_farofa = 1.11 
valor_unidade_forma = 0.95


while opcao != 6:
    print("==== PADARIA ====")
    print(" ---MENU---")
    print("[1] - Pão Frances")
    print("[2] - Pão Integral ")
    print("[3] - Pão doce liso")
    print("[4] - Pão doce farofa")
    print("[5] - Pão de forma ")
    print("[6] - FIM DA COMPRA.")
    print("-----------------------")

    opcao = int(input("Escolha a sua opção: "))
    
    if opcao == 1:
      frances = int(input("Informe a quantidade de pão frances você deseja: "))
      valor_frances = frances * 1.04
      
    elif opcao == 2:
      integral = int(input("Informe a quantidade de pão integral você deseja: "))
      valor_integral = integral * 1.04
      
    elif opcao == 3:
      doce_liso = int(input("Informe a quantidade de pão doce liso você deseja: "))
      valor_doce_liso = doce_liso * 1.08
      
    elif opcao == 4:
       doce_farofa = int(input("Informe a quantidade de pão doce farofa você deseja: "))
       valor_doce_farofa = doce_farofa * 1.11
      
    elif opcao == 5:
       forma = int(input("Informe a quantidade de pão forma você deseja: "))
       valor_forma = forma * 0.95
      
    elif opcao == 6:
        valor_total = valor_frances + valor_integral + valor_doce_liso + valor_doce_farofa + valor_forma
        print(f"Valor total da compra : {valor_total}")
        
        if frances > 0:
            print(f"Pão Frances valor: {valor_unidade_frances} - Quantidade: {frances} | Valor:R$ {valor_frances}")
        if integral > 0:
            print(f"Pão Integral valor: {valor_unidade_integral} - Quantidade: {integral} | Valor:R$ {valor_integral}")
        if doce_liso> 0:
            print(f"Pão Doce liso valor: {valor_unidade_doce_liso} - Quantidade: {doce_liso} | Valor:R$ {valor_doce_liso}")
        if doce_farofa> 0:
            print(f"Pão Doce farofa valor: {valor_unidade_doce_farofa} - Quantidade: {doce_farofa} | Valor:R$ {valor_doce_farofa}")
        if forma > 0:
            print(f"Pão Forma valor: {valor_unidade_forma} - Quantidade: {forma} | Valor:R$ {valor_forma}")
        
    else:
        print("OPÇÃO INVALIDA.")
    