opcao = 0
while opcao != 5:
    print("CALCULADORA")
    print("1- Somar ")
    print("2- Subitrair ")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Sair")
    opcao = int(input("Digite qual calculo deseja fazer: "))
    
    if opcao == 1:
        numero1 = float(input("Digite seu primeiro numero: "))
        numero2 = float(input("Digite seu segundo numero: "))
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")
    elif opcao == 2:
        numero1 = float(input("Digite seu primeiro numero: "))
        numero2 = float(input("Digite seu segundo numero: "))
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")
    elif opcao == 3:
        numero1 = float(input("Digite seu primeiro numero: "))
        numero2 = float(input("Digite seu segundo numero: "))
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2}  = {resultado}")
    elif opcao == 4:
        numero1 = float(input("Digite seu primeiro numero: "))
        numero2 = float(input("Digite seu segundo numero: "))
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")
    elif opcao == 5:
        print("Saindo.. ")
        break
    else:
        print("OPÇÃO INALIDA.")
       
    