import random

numero_magico = random.randint(1, 10)

while True: 

  user = int(input("Digite o numero que eu estou pensando: "))

  if user == numero_magico:
    print("Acertou!")
    break
  else:
    print("Errou!")
  if user > numero_magico:
    print("O numero magico é menor!")
  elif user < numero_magico:
    print("O Numero magico é maior!")