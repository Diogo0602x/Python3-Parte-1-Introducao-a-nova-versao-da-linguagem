print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
  print("Tentativa {} de {}".format(rodada, total_de_tentativas))
  chute_str = input("Digite o seu número: ")
  print("Você digitou", chute_str)
  chute = int(chute_str)

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if (acertou):
    print("Você acertou!")
  else:
    if(maior):
      print("Você errou! O seu chute foi maior do que o número secreto.")
    if(menor):
      print("Você errou! O seu chute foi menor do que o número secreto.")    

print("Fim do jogo")