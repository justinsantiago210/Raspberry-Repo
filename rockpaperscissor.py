from random import choice

choice_list = ["rock", "paper", "scissors"]
player_choice = input("Please Choose either Rock, Paper or Scissors!: ")
computer_choice = choice(choice_list)

outcome = {"scissors": {"win":"paper", "lose":"rock"},
            "paper": {"win":"rock", "lose":"scissors"},
            "rock": {"win":"scissors", "lose":"paper"}}

if outcome[player_choice]["win"] == computer_choice:
    print("The computer has chosen: ", computer_choice)
    print("You win!")
elif outcome[player_choice]["lose"] == computer_choice:
    print("The computer has chosen: ",computer_choice)
    print("You Lose!")
else:
    print("The computer has chosen: ",computer_choice)
    print("It's a tie. Go again!")