import random

user = ""
play_again = True

while play_again:
    choices = ["rock", "paper", "scissors"]
    while user not in choices:
        user = input("Choose rock, paper or scissors: ").lower()

    computer = random.choice(choices)

    if user == computer:
        print("You: {}".format(user))
        print("Computer: {}".format(computer))
        print("Tie!")
    elif user == "rock":
        if computer == "paper":
            print("You: {}".format(user))
            print("Computer: {}".format(computer))
            print("Computer wins!")
        elif computer == "scissors":
            print("You: {}".format(user))
            print("Computer: {}".format(computer))
            print("You win!")
    elif user == 'scissors':
        if computer == 'paper':
            print("You: {}".format(user))
            print("Computer: {}".format(computer))
            print("You win!")
        elif computer == 'rock':
            print("You: {}".format(user))
            print("Computer: {}".format(computer))
            print("Computer wins!")
    elif user == "paper":
        if computer == "scissors":
            print("You: {}".format(user))
            print("Computer: {}".format(computer))
            print("Computer wins!")
        elif computer == 'rock':
            print("You: {}".format(user))
            print("Computer: {}".format(computer))
            print("You win!")

    new_game = input("Do you want to play again? (yes/no)").lower()
    if new_game != 'yes':
        play_again = False
        break
    else:
        user = input("Choose rock, paper or scissors: ").lower()


print("You have left the game")




