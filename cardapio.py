opcao = 0
while opcao != 5:
    print("Cardapio")
    print("1 - Hamburguer")
    print("2 - Pizza")
    print("3 - Salada")
    print("4 - Refrigerante")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção:"))
    if opcao == 1:
        print("Você escolheu hamburguer.")
    elif opcao == 2:
        print ("Você escolheu a Pizza. ")
    elif opcao == 3:
        print("Você escolheu a Salada. ")
    elif opcao == 4:
        print("Você escolheu o Refrigerante. ")
    elif opcao == 5:
        print("Você escolheu finalizar compra...")
        break
    else:
        print("Opcao invalida.")