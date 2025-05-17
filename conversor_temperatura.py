temperatura_inicial = float(input("Informe a temperatura inicial: "))

opcao=0
while opcao!=3:
   print("Conversor de Temperatura")
   print("[1]- Celsius para Fahrenheint" )
   print("[2]- Celsius para Kelvin")
   print("[3]-SAIR..")
   opcao = float(input("Escolha uma opição: "))
   if opcao == 1:
     temperatura = (temperatura_inicial* 9 / 5)+ 32
     print(f"A temperatura covertida de Celsius para Fahrenheint e {temperatura}")
   elif opcao == 2:
     temperatura = temperatura_inicial + 273.15
     print(f"A temperatura convertida Celsius para Kelvin e {temperatura}")
   elif opcao == 3:
    print("Saindo...")
   else:
    print("Opção invalida")   
   