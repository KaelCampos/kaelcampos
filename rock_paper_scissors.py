# Escreva o seu código aqui :-)
import random
import time

user_points = 0
computer_points = 0

options = ["R", "T", "P"]

44824093830

while True:
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").upper()

    if user_choice == "Q":
        break

    if user_choice not in options:
        continue

    #0 será pedra, 1 será tesoura e 2 será papel
    computer_choice = random.randint(0,2)
    computer_options = options[computer_choice]

    print("O computador escolheu " + computer_options)

    if user_choice == computer_choice:
        print("Empate")

    elif user_choice == "r" and computer_options == "t":
       print("Você ganhou!")
       user_points = user_points+1
    elif user_choice == "P" and computer_options == "r":
       print("Você ganhou!")
       user_points = user_points+1
    elif user_choice == "t" and computer_options == "p":
       print("Você ganhou!")
       user_points = user_points+1

    else:
        print("Você Perdeu")
        computer_points = computer_points + 1

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if computer_points > user_points:
        print("Derrota!!!!")
elif computer_points == user_points:
        print("Empate")
else:
        print("Vitória!!!")





time.sleep(2)
print("Até a próxima!")


