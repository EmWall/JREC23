import random

playing = input("Wanna play rock paper scissors? (type yes or no)\n")
while(playing == "yes"):
    print("Rock... Paper... Scissors...")
    moves = ["rock", "paper", "scissors"]
    robot_choice = random.choice(moves);

    print("I have saved my move! What's yours?")
    user_choice = input("(Type rock, paper, or scissors)\n")

    if(robot_choice == user_choice):
        print("Matchies! We tied.")
    if(robot_choice == "rock"):
        if(user_choice == "scissors"):
            print("Rock crushes scissors, I won! Better luck next time.")
        if(user_choice == "paper"):
            print("Paper covers rock, you won! Congrats!")
    if(robot_choice == "paper"):
        if(user_choice == "rock"):
            print("Paper covers rock, I won! Better luck next time.")
        if(user_choice == "scissors"):
            print("Scissors cut paper, you won! Congrats!")
    if(robot_choice == "scissors"):
        if(user_choice == "paper"):
            print("Scissors cut paper, I won! Better luck next time.")
        if(user_choice == "rock"):
            print("Rock crushes scissors, you won! Congrats!")
    playing = input("That was fun! Wanna play again? (type yes or no)\n")
print("Okay! Byeeeeeeeee")
