nome =  (input("Informe o seu nome: "))
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / (altura * 2)

if imc < 18.5:
   print(f"{nome} você esta abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
   print(f"{nome}seu peso esta normal")
elif imc >= 25.0 and imc <= 29.9:
    print (f"{nome} você esta com sobrepeso")
elif imc >= 30.0:
    print(f"{nome} você esta Obeso")