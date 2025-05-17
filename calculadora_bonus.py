print ("========================")
nome = (input("Informe o nome do vendedor: "))
salario_fixo = float(input("Informe o valor do seu salario fixo: "))
total_de_vendas = int(input("Informe a quantidade de vendas: "))
print ("========================")
bonus = 0.15
total_bonus = salario_fixo * bonus
salario_recebido = salario_fixo + total_bonus

if total_de_vendas >= 20:
    print("PARABENS!! Meta atingida ")
    print(f"Valor do bonus: R${total_bonus} salario final: R${salario_recebido}")
else:
    print("Meta não atingida ")
   
    
