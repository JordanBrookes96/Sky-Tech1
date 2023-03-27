import random

user_wins = 0
computer_wins = 0
OPTIONS = ["ROCK", "PAPER", "SCISSORS"]

while True:
    user_pick = input("Type your input: Rock / Paper / Scissors / Quit: ").upper()
    if user_pick == "QUIT":
        break

    if user_pick not in OPTIONS:
        continue

    random_number = random.randint(0, 2)
    # Rock is 0, Paper is 1, Scissors is 2
    computer_pick = OPTIONS[random_number]
    print("Computer picked", computer_pick + ".")

    if user_pick == "ROCK" and computer_pick == "SCISSORS":
        print("You won!")
        user_wins += 1
    elif user_pick == "PAPER" and computer_pick == "ROCK":
        print("You won!")
        user_wins += 1
    elif user_pick == "SCISSORS" and computer_pick == "PAPER":
        print("You won!")
        user_wins += 1
    elif user_pick == computer_pick:
        print("That was a draw!")
    else:
        print("You lost!")
        computer_wins += 1

if user_wins > computer_wins:
    print(f"You beat the computer! {user_wins} : {computer_wins}")
elif user_wins == computer_wins:
    print(f"It was a draw! {user_wins} : {computer_wins}")
else:
    print(f"You lost to the computer! {user_wins} : {computer_wins}")

print("Goodbye!")
