import forca
import adivinhacao

print("*********************************")
print("*******Escolhe o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
  print("Jogando forca")
elif(jogo == 2):
  print("Jogando adivinhação")
