import random

options = ("rock" , "paper" , "scissors") #why did we use tuple instead of list

computer = random.choice(options)
player = None 

while True:
    computer = random.choice(options)
    player = input("rock/paper/scissors?: ")
    
    print("Player = " , player)
    print("Computer = " , computer)
    
    if player not in options:
        print("Invalid Choice!")
    elif player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors": # why cant we name our files with / , also what things are not allowed in file naming
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!") 
    else:
        print("You Lose!")
        
    if input("Do you want to play again? (y/n)").lower()  == "n":
        print("Goodbye!")
        break