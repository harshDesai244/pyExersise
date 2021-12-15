import random

user_wins = 0
computer_wins = 0
tye = 0
option = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue

    random_number = random.randint(0, 2)
    # rock: 0 paper: 1  scissior: 2
    compputer_pick = option[random_number]
    print("Computer pick", compputer_pick + ".")

    if user_input == "rock" and compputer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and compputer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and compputer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("Computer won!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("computer win", computer_wins, "times.")
print("Goodbye")
