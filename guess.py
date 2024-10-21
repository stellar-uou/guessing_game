import random 

def adivinhar():
  numero = random.randint(1, 100)
  tentativas = 0

  print("Bem-vindo(a) ao jogo de adivinhação! irei escolher um número de 1 a 100 e você deverá adivinhar.")

  while True:

    palpite = int(input("Qual seu palpite? "))
    tentativas += 1

    if palpite > numero:
      print("Seu palpite é muito alto, tente novamente.")

    elif palpite < numero:
      print("Seu palpite é muito baixo, tente novamente.")

    else:
      print(f"Parabéns! Você adivinhou o número {numero} em {tentativas} tentativas")
      break

adivinhar()
