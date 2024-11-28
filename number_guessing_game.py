import random

random = random.randint(1 , 100)
guess = 0

while guess != random:
    guess = int(input("Enter Your Guess: "))
    
    if guess < random:
        print("Guess Higher!")
    elif guess > random:
        print("Guess Lower!")
    else:
        print("You Won!")