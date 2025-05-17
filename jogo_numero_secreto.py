import random
numero_aleatorio = random.randint(1, 10)
print ("=== jogo da adivinhação ===")
print ("Tente acertar o número secreto de 1 a 10. ")

tentativa = 0
contagem_tentativas = 0

while tentativa != numero_aleatorio:
    numero = int (input("Digite sua tentativa: "))
    contagem_tentativas = contagem_tentativas + 1
    if numero == numero_aleatorio:
        print ("Parabéns, você acerto número! ")
        print (f"Foram feitas {contagem_tentativas} tentaviva para acertar.") 
          
    elif  numero < numero_aleatorio:
        print ("O número secreto é maior. ")
    else:
        print ("O número secreto é menor. ") 
